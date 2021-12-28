from django.db import models
from django.db.models.enums import Choices
from django.utils.translation import gettext as _

# Create your models here.

Choice =  [
    ("policy", 'Policy'),
    ("form", 'Form'),
    ]

class Documentation(models.Model):
    doc_name = models.CharField(max_length=100,blank=False,null=False)
    file_type = models.CharField(choices=Choice,max_length=6,blank=True,null=True)
    file = models.FileField(upload_to='file/',null=True)
    date_time = models.DateTimeField(_("Date and Time"), auto_now=False, auto_now_add=False)
    

    def __str__(self):
        return self.doc_name  
