from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
import pytz
from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_managements.settings')

app = Celery('employee_managements')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings',namespace='CELERY')
# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'schedule_task':{
            'task':'attendance.tasks.attendance_task',
            'schedule':crontab(hour=23, minute=59),
            
        }
    }
)

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'schedule_task':{
            'task':'attendance.tasks.auto_calendar',
            'schedule':crontab(hour=23, minute=59),
            
        }
    }
)

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'schedule_task':{
            'task':'attendance.tasks.Auto_Leave',
            'schedule':crontab(hour=15, minute=1),
            
        }
    }
)


app.conf.update(
    CELERYBEAT_SCHEDULE={
        'schedule_task':{
            'task':'attendance.tasks.auto_calendar',
            'schedule':crontab(hour=15, minute=17),
            
        }
    }
)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')