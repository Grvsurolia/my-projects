import csv
import email.message
import smtplib
import ssl
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
from django.core import mail
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from .models import *
from .serializer import *

import os
import base64
from django.conf import settings
import json

def check_smtp_email(server, port, username, password):
    smtp_server = server
    port = port  # For starttls
    sender_email = username
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
        return str(e)
    # finally:
    #     server.quit() 

class AddMailAccount(APIView):

    def get(self,request,*args,**kwargs):
        account = SMTPEmailAccount.objects.all()
        serializer = SmtpAccoutSerializer(account, many=True)
        return Response({"data":serializer.data,"success":True})

    def post(self,request,*args,**kwargs):
        try:
            if SMTPEmailAccount.objects.get(smtp_username=request.data['smtp_username']):
                return Response({"message":"this mail account is already registred","sucess":False})
        except:
            serializer = SmtpAccoutSerializer(data=request.data)

            if serializer.is_valid():
                
                serializer.save()
                return Response({"data":serializer.data,"success":True})
            return Response({"message":serializer.errors,"success":False})


class MailAccountDetail(APIView):
    """
    Retrieve, update or delete a mailaccount instance.
    """
    def get_object(self, pk):
        try:
            return SMTPEmailAccount.objects.get(pk=pk)
        except SMTPEmailAccount.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        mail = self.get_object(pk)
        serializer = SmtpAccoutSerializer(mail)
        return Response({"data":serializer.data,"success":True})

    def put(self, request, pk, format=None):
        mail = self.get_object(pk)
        serializer = SmtpAccoutSerializer(mail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"success":True})
        return Response({"message":serializer.errors, "success":False})

    def delete(self, request, pk, format=None):
        mail = self.get_object(pk)
        mail.delete()
        return Response({"message":"mail account successfully deleted"})
    

class AddEmailView(APIView):

    def get(self,request,*args,**kwargs):
        account = MailSentStatus.objects.all()
        serializer = MailSentStatusSerilizer(account, many=True)
        return Response({"data":serializer.data,"success":True})

    
    def post(self,request,*args,**kwargs):
        csvfile = request.FILES["csvfile"]
        subject = request.data["subject"]
        email_body = request.data["email_body"]
       

        csv_ob = Email(csvfile=csvfile)
        csv_ob.save()
                
        mail_accounts = SMTPEmailAccount.objects.all()
        mail_accounts_count = mail_accounts.count()

        if mail_accounts_count != 0:

            with open(str(csv_ob.csvfile)) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                email_list = []
                line_count = 0
                for row in csv_reader:
                    if line_count==0:
                        line_count += 1
                    else:
                        email_list.append(row[0])
            count = 0
            for i in range(0, len(email_list), mail_accounts_count):
                for j in range(0, mail_accounts_count):
                    if(i+j <= len(email_list) - 1):
                        print(count+1)
                        try:
                            sent_mails_db = MailSentStatus.objects.all().values_list('receiver', flat=True)
                            if email_list[i + j] not in sent_mails_db:
                                now = datetime.now()
                                now_plus_2 = now + timedelta(minutes = 2)
                                mailsend_celery_ob = MailSentCelery(sender=mail_accounts[j], receiver=email_list[i + j], at_time=now_plus_2,subject=request.data['subject'],body=request.data['email_body'],csv_name=str(csv_ob.csvfile).split("/")[-1])
                                mailsend_celery_ob.save()
                            else:
                                print("Mail not sent to ",email_list[i + j], "\n\n\n")
                        except Exception as E:
                            print(E,"exception me hu")
            
            return Response({"data":"serializer.data","success":True})
        return Response({"data":"please configure sending email account","success":False})



class DeleteEmails(APIView):

    """
    Retrieve, update or delete a mailaccount instance.
    """
    def get_object(self, pk):
        try:
            return Email.objects.get(pk=pk)
        except Email.DoesNotExist:
            raise Http404


    def delete(self, request, pk, format=None):
        email = self.get_object(pk)
        email.delete()
        return Response({"message":"emails successfully deleted"})


    
def send_mail_with_smtp(from_email,to_email, subject, email_body):
  

    try:
        print("i am in try")
        fromaddr = from_email.smtp_username
      
        password = from_email.smtp_password
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = to_email
        msg['Subject'] = subject

        to_pass_with_url = {"to":to_email}
        base64_message = base64.b64encode(json.dumps(to_pass_with_url).encode()).decode()
        base64_message = base64.b64encode(json.dumps(base64_message).encode()).decode()
        open_tracking_url = (os.path.join(settings.SITE_URL + "/mail/email/open/")) + base64_message
        # emailData = email_body + " <img width=0 height=0 src='"+open_tracking_url+"' />"


        email_body_links = re.findall(r'(https?://\S+)', email_body)
        if email_body_links:
            #URL is Present
            
            emailData = email_body
            for i, val in enumerate(email_body_links):
           
              

                to_pass_with_url = {"to": to_email,"url":val}
                
                base64_message = base64.urlsafe_b64encode(json.dumps(to_pass_with_url).encode()).decode()
                base64_message = base64.urlsafe_b64encode(json.dumps(base64_message).encode()).decode()

                click_tracking_url = "<a href='" + (settings.SITE_URL + "/mail/email/click/") + base64_message  + "'>" + val + "  </a>"
                new_emailData = re.sub(val, click_tracking_url, emailData)
                emailData = new_emailData + " <img width=0 height=0 src='"+open_tracking_url+"' />"
        else:
            #No URL Present
        
            emailData = email_body + " <img width=0 height=0 src='"+open_tracking_url+"' />"


        body = emailData
        msg.attach(MIMEText(body, 'html'))
        if ('@gmail.com' in from_email.smtp_username):

            server_ssl = smtplib.SMTP(from_email.smtp_host,from_email.smtp_port)
        else:
            server_ssl = smtplib.SMTP(from_email.smtp_host)
        server_ssl.ehlo()
        server_ssl.starttls()
        server_ssl.login(fromaddr, password)

        text = msg.as_string()
        server_ssl.sendmail(fromaddr, msg['To'], text)
        server_ssl.close()

    except Exception as _error:
        print(_error)
        raise Exception('Error in sending mail >> {}'.format(_error))



class TrackEmailOpen(APIView):

    def get(self, request, format=None, id=None):
        try:
            full_url = settings.SITE_URL + request.get_full_path()

            base64_message = full_url.split('/')[-1]

            base64_bytes = base64_message.encode('ascii')

            message_bytes = base64.b64decode(base64_bytes)

            message_bytes = base64.b64decode(message_bytes)

            trackData = message_bytes.decode('ascii')

            trackData = eval(trackData)

        
            mail_sent_status = MailSentStatus.objects.get(receiver=trackData['to'])

            mail_sent_status.is_open = True
            mail_sent_status.open_count += 1

            mail_sent_status.save()
            
            return Response({"message":"Saved Successfully"})
        except Exception as e:
            print(e)
            return Response({"message":e})



class TrackEmailClick(APIView):


    def get(self, request, format=None, id=None):

        full_url = settings.SITE_URL + request.get_full_path()


        base64_message = full_url.split('/')[-1]

        base64_bytes = base64_message.encode('ascii')

        message_bytes= base64.b64decode(base64_bytes)

        message_bytes = base64.b64decode(message_bytes)

        trackData = message_bytes.decode('ascii')

        trackData = eval(trackData)

        mail_sent_status = MailSentStatus.objects.get(receiver=trackData['to'])
        mail_sent_status.is_linked_clicked = True
        mail_sent_status.link_count += 1
        mail_sent_status.save()
        return redirect(trackData['url'])

