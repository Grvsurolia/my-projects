from django.contrib import admin

from .models import (Campaign, CampaignLeadCatcher, CampaignRecipient,
                     DripEmailModel, EmailOnLinkClick, FollowUpEmail,CampaignLabel)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('assigned','title', 'from_address', 'csvfile_op1', 'created_date_time', 'track_opens', 'track_linkclick', 'schedule_send', 'schedule_date', 'schedule_time','terms_and_laws', 'campaign_status','id')


# @admin.register(CampaignStatistic)
# class CampaignCampaignStatisticAdmin(admin.ModelAdmin):
#     list_display = ('open_mail_count', 'Campaign_recipient')


@admin.register(CampaignRecipient)
class CampaignRecipientAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'email', 'subject', 'email_body','sent', 'leads','replies', 'opens', 'opens_count', 'has_link_clicked', 'link_clicked_count', 'bounces','engaged', 'lead_status','reciepent_status','unsubscribe','is_delete','id','assigned')


@admin.register(FollowUpEmail)
class CampaignFollowUpEmailAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'waitDays', 'subject', 'email_body')


@admin.register(DripEmailModel)
class CampaignDripEmailModelAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'waitDays', 'subject', 'email_body')


@admin.register(EmailOnLinkClick)
class EmailOnLinkClickAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'waitDays', 'url', 'subject', 'email_body')


@admin.register(CampaignLeadCatcher)
class Campaign_Lead_Catcher(admin.ModelAdmin):
    list_display = ('campaign', 'assigned', 'leadcatcher_recipient', 'of_times')


@admin.register(CampaignLabel)
class CampaignLabelAdmin(admin.ModelAdmin):
    list_display = ('label_name','created_date_time','id')