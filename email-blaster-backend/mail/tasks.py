import random
import time
from datetime import datetime, time, timedelta

import pytz
import requests
from celery import shared_task
from django.core.mail import send_mail
from django.http import JsonResponse

from .models import Email, MailSentCelery, MailSentStatus, SMTPEmailAccount
from .views import send_mail_with_smtp


@shared_task
def send_email_task():
    mail_obj = MailSentCelery.objects.first()
    if mail_obj != None:
        try:
            send_mail_with_smtp(mail_obj.sender, mail_obj.receiver, mail_obj.subject, mail_obj.body)
            mail_send_status = MailSentStatus(sender=mail_obj.sender, receiver=mail_obj.receiver, status=True,csv_name=mail_obj.csv_name)
            print("Send mail to ",mail_obj.receiver)
        except Exception as E:
            print('Error = ', E)
            mail_send_status = MailSentStatus(sender=mail_obj.sender, receiver=mail_obj.receiver, status=False,csv_name=mail_obj.csv_name)
            print("Mail Not Send to ",mail_obj.receiver)
        finally:
            mail_send_status.save()
            mail_obj.delete()
    else:
        print("No Data Found")

