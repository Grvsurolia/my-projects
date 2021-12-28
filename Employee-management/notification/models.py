from django.db import models
from employees.models import User
from leave.models import LeaveApplication


class Notification(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    read_notification = models.BooleanField(default=False)
    
    

