from django.db import models

# Create your models here.

Smtp_Port = (
    ("587",'587'),
    ("25" , "25"),
    ("465","465"),
    ("2525","2525"),
)

class SMTPEmailAccount(models.Model):
    smtp_username = models.CharField(max_length=200,blank=True,null = True)
    smtp_password = models.CharField(max_length=200,blank=True,null = True)
    smtp_host = models.CharField(max_length=200,blank=True,null = True)
    smtp_port = models.CharField(max_length=20,choices=Smtp_Port,default='587',blank=True,null = True)


    def __str__(self):
        return self.smtp_username


class Email(models.Model):
    csvfile = models.FileField(upload_to='csv_uploads/', blank=True, null=True)

    def __str__(self):
        return str(self.csvfile)


class MailSentStatus(models.Model):
    sender = models.CharField(max_length=200,blank=True,null = True)
    receiver = models.CharField(max_length=200,blank=True,null = True)
    status = models.BooleanField(default=False)
    csv_name = models.CharField(max_length=500)
    is_open = models.BooleanField(default=False)
    open_count = models.PositiveIntegerField(default = 0,blank=True,null = True)
    is_linked_clicked = models.BooleanField(default=False)
    link_count = models.PositiveIntegerField(default = 0,blank=True,null = True)


    def __str__(self):
        return self.receiver


class MailSentCelery(models.Model):
    sender = models.ForeignKey(SMTPEmailAccount, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=200,blank=True,null = True)
    subject = models.TextField()
    body = models.TextField()
    at_time = models.TimeField(auto_now=True)
    csv_name = models.CharField(max_length=500)

    def __str__(self):
        return self.receiver
