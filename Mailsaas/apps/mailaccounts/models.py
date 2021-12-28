from django.db import models

from apps.users.models import CustomUser

# Create your models here.

Smtp_Port = (
    ("587",'587'),
    ("25" , "25"),
    ("465","465"),
    ("2525","2525"),
)
Imap_Port = (
    ("993",'993'),
    ("143" , "143"),
    ("995","995"),
)

Provider = (
    ("SMTP","Smtp"),
    ("GOOGLE","Google"),
    ("MICROSOFT","Microsoft"),
)


class EmailAccount(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200)
    smtp_host = models.CharField(max_length=200,blank=True,null = True)
    smtp_username = models.CharField(max_length=200,blank=True,null = True)
    smtp_password = models.CharField(max_length=200,blank=True,null = True)
    smtp_port = models.CharField(max_length=20,choices=Smtp_Port,default='587',blank=True,null = True)
    imap_host = models.CharField(max_length=200,blank=True,null = True)
    imap_username = models.CharField(max_length=200,blank=True,null = True)
    imap_password = models.CharField(max_length=200,blank=True,null = True)
    imap_port = models.CharField(max_length=20,choices=Imap_Port,default='993',blank=True,null = True)
    access_token = models.CharField(max_length=500,blank=True,null=True)
    provider = models.CharField(max_length=100,choices=Provider,default='',null=True,blank=True)

    def __str__(self):
        return self.email


