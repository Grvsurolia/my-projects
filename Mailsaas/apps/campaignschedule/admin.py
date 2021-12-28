from django.contrib import admin

from .models import Email_schedule, Schedule, WeekDays

# Register your models here.

admin.site.register(Schedule)
admin.site.register(WeekDays)
# admin.site.register(Email_schedule)

@admin.register(Email_schedule)
class EmailScheduleAdmin(admin.ModelAdmin):
    list_display = ('time','date', 'user_id', 'mail_account', 'recipient_email', 'subject', 'email_body')

