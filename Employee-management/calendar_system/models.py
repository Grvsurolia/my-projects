from django.db import models
from employees.models import User

# Create your models here.
class EmployeeCalendar(models.Model):
    employee = models.ForeignKey(User,on_delete=models.CASCADE)
    today_date=models.DateField(auto_now=True)
    status = models.CharField(max_length=30)

    def __str__(self):
        return str(self.employee)