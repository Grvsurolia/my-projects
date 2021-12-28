from django.db import models
from employees.models import  User
import datetime

# Create your models here.
class Attendance(models.Model):
    STATUS_CHOICE = [
        ('INTIME', 'In_Time'),
        ('OUTTIME','Out_Time')]
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_date = models.DateField(auto_now_add =True)
    attendance_time =models.TimeField(auto_now=True)
    attendance_status =models.CharField(choices=STATUS_CHOICE,max_length=15)
    break_time = models.DurationField(default=datetime.time())
    working_time = models.DurationField(default=datetime.time())


    # def __str__(self):
    #     return self.employee.first_name +" " + self.employee.last_name
