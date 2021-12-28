from django.db import models
from employees.models import User

# Create your models here.
NATURE_CHOICE =[
        ('positive', 'Positive'),
        ('negative','Negative')]

class FeedBack(models.Model):
    incident_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="IncidentPerson")
    responsible_person = models.ManyToManyField(User)
    incident_name = models.CharField(max_length=50)
    incident_nature = models.CharField(choices=NATURE_CHOICE,max_length=15)
    priority = models.CharField(max_length=50)
    description = models.TextField()
    comments = models.TextField()
    attach_file = models.FileField(upload_to='file/',null=True,blank=True)


    def __str__(self):
        return str(self.incident_person)


