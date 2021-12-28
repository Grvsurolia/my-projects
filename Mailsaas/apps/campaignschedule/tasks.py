import random
import time
from datetime import datetime, time, timedelta

import pytz
import requests
from celery import shared_task
from django.core.mail import send_mail
from django.http import JsonResponse

from apps.campaign.models import Campaign, CampaignRecipient
from apps.mailaccounts.models import EmailAccount
from apps.mailaccounts.views import send_mail_with_smtp

from .models import Email_schedule, Schedule
from .serializers import EmailScheduleSerializers
from .views import PostToSchedule


@shared_task
def send_email_task():
    print("schdule start")
    PostToSchedule.post
    email_schedule_data = Email_schedule.objects.all()

    for email_data in email_schedule_data:
        schedule = Schedule.objects.get(user = email_data.user_id)
        today_day = datetime.now().strftime("%A")
        block_days_list = []
        max_email_to_send_today = schedule.max_email
        mail_sent_count = 0
        min_mail_at_a_time = schedule.min_email_send
        max_mail_at_a_time = schedule.max_email_send
        
        random_no_of_mails_at_a_time = random.randint(min_mail_at_a_time, max_mail_at_a_time)

        # for i in list(schedule.block_days.values()):
        if (datetime.now().time().strftime("%H:%M") == email_data.time.strftime("%H:%M")) and (today_day not in block_days_list) and (mail_sent_count < max_email_to_send_today):
            email_account_ob = EmailAccfrom __future__ import print_function
# import pickle
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request

# # If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# def main():
#     """Shows basic usage of the Gmail API.
#     Lists the user's Gmail labels.
#     """
#     creds = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)

#     service = build('gmail', 'v1', credentials=creds)

#     # Call the Gmail API
#     results = service.users().labels().list(userId='me').execute()
#     labels = results.get('labels', [])

#     if not labels:
#         print('No labels found.')
#     else:
#         print('Labels:')
#         for label in labels:
#             print(label['name'])

# if __name__ == '__main__':
#     main()ount.objects.get(email=email_data.mail_account.email)
            if email_account_ob.provider == "SMTP":
                send_mail_with_smtp(email_account_ob.smtp_host, email_account_ob.smtp_port, email_account_ob.smtp_username, email_account_ob.smtp_password, [email_data.recipient_email.email], email_data.subject, email_data.email_body)
                email_data.delete()
                mail_sent_count += 1
                print("Mail Sent")
            # send_mail(email_data.subject, email_data.email_body, email_data.mail_account, [email_data.recipient_email],fail_silently=False)
            
            

        else:
            print("Mail Not Sent")
        # print("Mail Send to "+email_data.recipient_email+" from "+email_data.mail_account+" with subjects "+email_data.subject+" with Email "+email_data.email_body)
    return "Done"
    
