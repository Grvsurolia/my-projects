from django.contrib import admin
from .models import SMTPEmailAccount, Email, MailSentStatus, MailSentCelery
# Register your models here.

@admin.register(SMTPEmailAccount)
class SMTPEmailAccountAdmin(admin.ModelAdmin):
    list_display = ('smtp_username','smtp_password','smtp_host','smtp_port')

@admin.register(Email)
class SMTPEmailAccountAdmin(admin.ModelAdmin):
    list_display = ('csvfile',)


@admin.register(MailSentStatus)
class SMTPEmailAccountAdmin(admin.ModelAdmin):
    list_display = ('receiver','sender','status', 'is_open', 'open_count','is_linked_clicked','link_count')


@admin.register(MailSentCelery)
class SMTPEmailAccountAdmin(admin.ModelAdmin):
    list_display = ('receiver','sender','subject','body','at_time')