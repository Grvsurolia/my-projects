import base64
import imaplib
import os
import pprint
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import progressbar
from django.conf import settings
from django.core import mail
from django.core.mail.backends.smtp import EmailBackend
from django.shortcuts import render
from Google import Create_Service
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.campaignschedule.models import Schedule
from apps.users.models import CustomUser

from .models import EmailAccount
from .serializers import EmailAccountSerializer


def check_smtp_email(server, port, email, password):
    import smtplib
    import ssl

    smtp_server = server
    port = port  # For starttls
    sender_email = email
    password = password

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        # server.login(sender_email, password)
        login_status = server.login(sender_email, password)
        return login_status
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print("error = ",e)
        return str(e)
    # finally:
    #     server.quit() 


class EmailAccountsView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = EmailAccount.objects.all()

    def post(self,request,*args,**kwargs):
        request.data["user"] = request.user.id
        if request.data['smtp_username'] == request.data['email'] and request.data['imap_username'] == request.data['email']:
            request.data["provider"] = "SMTP"
            serializer = EmailAccountSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    if check_smtp_email(request.data["smtp_host"], request.data["smtp_port"], request.data["email"], request.data["smtp_password"])[1].decode("utf-8") == "Authentication succeeded":
                        serializer.save()
                        email_account_data = EmailAccount.objects.filter(user=request.user.id)
                        count_email_accounts_of_current_user = email_account_data.count()
                        if count_email_accounts_of_current_user==1:
                            user = CustomUser.objects.get(id=request.user.id)
                            mail_account = EmailAccount.objects.get(id=email_account_data.get().id)
                            schedule_ob = Schedule(
                                user=user,
                                mail_account=mail_account,
                                start_time='06:00:00',
                                end_time='11:00:00',
                                time_zone='America/Los_Angeles',
                                max_email=20,
                                strategy='SPACE',
                                mint_between_sends=12,
                                min_email_send=1,
                                max_email_send=1)
                            schedule_ob.save()
                except:
                    return Response({"message":check_smtp_email(request.data["smtp_host"], request.data["smtp_port"], request.data["email"], request.data["smtp_password"])[8:-2],"success":False})
                return Response({"message":serializer.data,"success":True})
            return Response({'message':serializer.errors,"success":False})
        return Response({"message":"Smtp username and Imap username does not match to email"})

    def get(self,request,*args,**kwargs):

        try:

            params = list(dict(request.GET).keys())
            if 'search' in params:
                mail_search = request.GET["search"]
                queryset = EmailAccount.objects.filter(user=request.user.id, email__contains=mail_search)
            elif 'filter_choice_1' and 'filter_choice_2' in params:
                
                filter_choice_1 = request.GET["filter_choice_1"]
                filter_choice_2 = request.GET["filter_choice_2"]
                if filter_choice_1 == "accounttype":
                    if filter_choice_2=='smtp':
                        filter_choice_2='SMTP'
                    if filter_choice_2=='google':
                        filter_choice_2='GOOGLE'
                    if filter_choice_2=='microsoft':
                        filter_choice_2='MICROSOFT'
                    queryset = EmailAccount.objects.filter(user=request.user.id, provider=filter_choice_2)
            else:
                queryset = EmailAccount.objects.filter(user=request.user.id)
            serializer = EmailAccountSerializer(queryset,many = True)
            return Response({"message":serializer.data,"success":True})

        except Exception as e:
            return Response ({"message":"mail account not available \n"+str(e)})


class EmailAccountsUpdateView(generics.UpdateAPIView):

    serializer_class = EmailAccountSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = EmailAccount.objects.all()

    def put(self,request,pk,format=None):
        queryset = EmailAccount.objects.get(id=pk)
        request.data["user"] = request.user.id
        serializer = EmailAccountSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Connection Updated successfully"})
        return Response({"error":serializer.errors})
        
    def delete(self,request,pk,format=None):
        try:
            queryset = EmailAccount.objects.get(id=pk)
        except:
            return Response({"message":"No Mail Account For this Id"})
        queryset.delete()
        return Response({"message":"Connection Delete successfully","success":True})



def send_mail_with_smtp(host, host_port, host_user, host_pass, send_to, subject, msg):
    try:
        con = mail.get_connection()
        con.open()
        print('Django connected to the SMTP server')

        mail_obj = EmailBackend(
            host=host,
            port=host_port,
            password=host_pass,
            username=host_user,
            use_tls=False,
            use_ssl = False,
            timeout=10
        )
        msg = mail.EmailMessage(
            subject=subject,
            body=msg,
            from_email=host_user,
            
            to=send_to,
            connection=con,
        )
        mail_obj.send_messages([msg])

        print('Message has been sent.')

        mail_obj.close()
        con.close()
        print('SMTP server closed')
        return True

    except Exception as _error:
        print('Error in sending mail >> {}'.format(_error))
        return False



# def send_mail_with_gmail():

#     print("In Send email with Gmail")
#     CLIENT_SECRET_FILE = 'client_secret.json'
#     API_NAME = 'gmail'
#     API_VERSION = 'v1'
#     SCOPES = ['https://mail.google.com/']

#     service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
#     print("serviceeeeeee",service)
#     emailMsg = 'You won $100,000'
#     mimeMessage = MIMEMultipart()
#     mimeMessage['from'] = 'developerextern@gmail.com'
#     mimeMessage['to'] = 'ashutoshsharma@externlabs.com'
#     mimeMessage['subject'] = 'You won'
#     mimeMessage.attach(MIMEText(emailMsg, 'plain'))
#     raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()




####################################START GOOGLE#####################################################


import pickle
import base64
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/']

def send_mail_google(to, subject, msg):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            authorization_url, state = flow.authorization_url(
                # Enable offline access so that you can refresh an access token without
                # re-prompting the user for permission. Recommended for web server apps.
                # access_type='offline',
                # Enable incremental authorization. Recommended as a best practice.
                include_granted_scopes='true')
            # print('authorization_url, state', authorization_url, state)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    # print("Servicessssss", service)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    # print("resultsssssssss", results)
    message = MIMEText(msg, "html")
    message['to'] = to
    # message['to'] = [x.encode('utf-8') for x in to_list]
    message['subject'] = subject
    # message["body"] = "message_text"
    # message = create_message("prag066@gmail.com", "gauravsurolia@externlabs.com", "Anything", "message_text")
    message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    send_email = (service.users().messages().send(userId="me", body=message)
            .execute())
    print ('Message Id: %s' % send_email['id'])

######################END GOOGLE################################################


import imaplib
import os
import pprint
import time

import progressbar


def imap():
    mail_setting = EmailAccount.objects.last()
    imap_host = mail_setting.imap_host
    imap_user = mail_setting.imap_username
    imap_pass = mail_setting.imap_password
    imap_port = mail_setting.imap_port
    # connect to host using SSL
    imap = imaplib.IMAP4_SSL(imap_host,imap_port)


    def animated_marker(): 
        widgets = ['Loading: ', progressbar.AnimatedMarker()] 
        bar = progressbar.ProgressBar(widgets=widgets).start() 
        
        for i in range(10): 
            time.sleep(0.1) 
            bar.update(i)
    ## login to server
    imap.login(imap_user, imap_pass)


#   imap.select('Inbox')

    tmp, data = imap.search(None, 'ALL')

    for num in data[0].split():
        animated_marker()
        tmpo, data = imap.fetch(num, '(RFC822)')
        emal = data[0][1].decode('utf-8')
        msg = message_from_string(emal)

        # emailData = str(email_message)

    # for response_part in data:

    # if isinstance(response_part, tuple):

    msges = message_from_string(data[1].decode('utf-8'))

    subject = str(msg).split("Subject: ", 1)[1].split("\nTo:", 1)[0]

    email_subject = msg['subject']

    email_from = msg['from']

    imap.close()


######################Google Mail Account###################

class GoogleAccountsAddView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = EmailAccount.objects.all()

    def post(self,request,*args,**kwargs):
        # from __future__ import print_function
        import pickle
        import os.path
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request

        # If modifying these scopes, delete the file token.pickle.
        SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

        # def main():
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        print("Enter in Mainnnnnnn")
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    os.path.abspath('credentials.json'), SCOPES)
                creds = flow.run_local_server(port=8000)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)
        
        # Call the Gmail API
        results = service.users().labels().list(userId='me').execute()
        print("resultsssssss", results)
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'])
        return Response("Done")

        # if __name__ == '__main__':
        #     main()

class TestGetView(APIView):
    permission_classes = (permissions.AllowAny,)
    # serializer_class = get_serializer_class()

    def get(self,request,*args,**kwargs):
        sg = send_mail_google("gauravsurolia@externlabs.com,prakhargupta@externlabs.com", "This is fargi mail", "<h1><i>This is Fargi mail Bodyyyyyyyyyy</i></h1>")
        return Response({"message":"Mail Sent"})
