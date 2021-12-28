from django.db import models
from django.db.models.base import Model
from users.models import User

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=255)
    category = models.CharField(max_length=255)
    
    class Meta:
        db_table = "Notification"
        verbose_name = 'Notification'
        verbose_name_plural = 'Notification'

