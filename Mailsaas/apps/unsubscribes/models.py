from django.db import models
from django.utils.translation import gettext as _

from apps.users.models import CustomUser

# Create your models here.

class UnsubscribeEmail(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    email = models.EmailField(_("Email Account"))
    mail_account = models.CharField(max_length=100,blank=True)
    name = models.CharField(max_length=100,blank=True,default='')
    date= models.DateTimeField(auto_now=True,blank=True)
    on_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class UnsubcribeCsv(models.Model):
    unscribe_emails= models.FileField(upload_to='unsubcribe_csv_uploads/', blank=True, null=True)

    
    def __str__(self):
        return str(self.unscribe_emails)
