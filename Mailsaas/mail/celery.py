
from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
import pytz
from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mail.settings')

import django
django.setup()


app = Celery('mail')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# from django_celery_beat.models import CrontabSchedule, PeriodicTask

# schedule, _ = CrontabSchedule.objects.get_or_create(
#     minute='30',
#     hour='*',
#     day_of_week='*',
#     day_of_month='*',
#     month_of_year='*',
#     timezone=pytz.timezone( 'Asia/Calcutta')
#  )

# PeriodicTask.objects.create(
#     crontab=schedule,
#     name='Importing mail',
#     task='mail.apps.campaignschedule.tasks.send_email_task',
#  )




app.conf.update(
    CELERYBEAT_SCHEDULE={
        'schedule_task':{
            # 'my':print('from celery app for task by'),
            'task':'apps.campaignschedule.tasks.send_email_task',
            'schedule':crontab(),
            
        }
    }
)




# from django_celery_beat.models import PeriodicTask, PeriodicTasks
# PeriodicTask.objects.all().update(last_run_at=None)
# for task in PeriodicTask.objects.all():
#     PeriodicTasks.changed(task)




@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')