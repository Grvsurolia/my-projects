# from __future__ import absolute_import

from .celery import app as celery_app

__all__ = ['celery_app']


# from apps.campaignschedule.models import WeekDays

# week_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# for day in week_names:
#     if not WeekDays.objects.filter(name = day):
#         week_ob = WeekDays(name = day)
#         week_ob.save()
#         print(day, " created in 'Week Days' table")