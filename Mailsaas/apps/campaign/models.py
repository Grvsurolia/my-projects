from datetime import date

from django.db import models

from apps.mailaccounts.models import EmailAccount
from apps.users.models import CustomUser

class CampaignLabel(models.Model):
    label_name = models.CharField(max_length=500,default='Unlabeled')
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.lable_name

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    from_address = models.ForeignKey(EmailAccount,on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=200,blank=True,null=True)
    csvfile_op1 = models.FileField(upload_to='csv_uploads/', blank=True, null=True)
    created_date_time = models.DateTimeField(auto_now=True)
    update_date_time = models.DateTimeField(auto_now=True)
    assigned = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    track_opens = models.BooleanField(default=False)
    track_linkclick = models.BooleanField(default=False)
    schedule_send = models.BooleanField(default=False)
    # scheduleDateTime = models.DateTimeField(auto_now_add=True, blank=True, null=True) 
    schedule_date = models.DateField(blank=True, null=True)
    schedule_time = models.TimeField(blank=True, null=True)
    terms_and_laws = models.BooleanField(default=False)
    campaign_status = models.BooleanField(default=False)    #Start Campaign or Pause Campaign
    label_name = models.ForeignKey(CampaignLabel, on_delete=models.SET_NULL, null=True, blank=True)
    is_archived = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=True)


    def __str__(self):
        return self.title


    
class CampaignRecipient(models.Model):
    LEAD_TYPE =( 

        ("none", "None"), 
        ("openLead", "Open Lead"), 
        ("wonLead", "Won Lead"), 
        ("lostLead", "Lost Lead"), 
        ("ignoredLead", "Ignored Lead"),
        ("forwardedLead", "Forwarded Lead"),
    ) 
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=2000, blank=True, null=True)
    company_name = models.CharField(max_length=1000, blank=True, null=True)
    role = models.CharField(max_length=1000, blank=True, null=True)
    email_body = models.TextField(blank=True, null=True)
    sent = models.BooleanField(default=False)
    leads = models.BooleanField(default=False)
    replies = models.BooleanField(default=False)
    opens = models.BooleanField(default=False)
    opens_count = models.PositiveIntegerField(default=0)
    has_link_clicked = models.BooleanField(default=False)
    link_clicked_count = models.PositiveIntegerField(default=0)
    bounces = models.BooleanField(default=False)
    lead_status = models.CharField(max_length=32,choices=LEAD_TYPE,default='none',blank = True, null = True)
    reciepent_status = models.BooleanField(default=False)    #Start Campaign or Pause Reciepent
    unsubscribe = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    created_date_time = models.DateTimeField(auto_now=True,blank=True,null=True)
    update_date_time = models.DateTimeField(auto_now=True,blank=True,null=True)
    assigned = models.BooleanField(default=True)
    engaged = models.BooleanField(default=False)


    def __str__(self):
        return str(self.campaign)


class FollowUpEmail(models.Model):
    campaign = models.ForeignKey('Campaign', on_delete=models.CASCADE)
    waitDays = models.PositiveIntegerField()
    subject = models.CharField(max_length=2000)
    email_body = models.TextField()

    def __str__(self):
        return str(self.campaign)


class DripEmailModel(models.Model):
    campaign = models.ForeignKey('Campaign', on_delete=models.CASCADE)
    waitDays = models.PositiveIntegerField()
    subject = models.CharField(max_length=2000)
    email_body = models.TextField()

    def __str__(self):
        return str(self.campaign)


class EmailOnLinkClick(models.Model):
    campaign = models.ForeignKey('Campaign', on_delete=models.CASCADE)
    waitDays = models.PositiveIntegerField()
    url = models.CharField(max_length=2000)
    subject = models.CharField(max_length=2000)
    email_body = models.TextField()

    def __str__(self):
        return str(self.campaign)
    

RECIPIENT =( 
    ('replies', "Replies"), 
    ('open', "Open"), 
    ('click_any_link', "Clicks any link"), 
    ('clicks_specific_link', "Clicks specific link"), 
) 

class CampaignLeadCatcher(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    assigned = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    leadcatcher_recipient = models.CharField(max_length=32,choices=RECIPIENT,default=0)
    specific_link = models.URLField(max_length=500, null=True,blank=True)
    of_times = models.PositiveIntegerField(null = True,blank=True,default = 0)
    
    def __str__(self):

        return str(self.campaign)


# class CampaignStatistic(models.Model):
#     Campaign_recipient = models.ForeignKey(CampaignRecipient, on_delete=models.CASCADE)
#     open_mail_count = models.PositiveIntegerField(null = True,blank=True,default = 0)
