from django.db import models
from datetime import date
from employees.models import User
from project_tracking.models import Project ,POCList
# Create your models here.


class Task(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project,blank=True)
    poc_project = models.ManyToManyField(POCList,blank=True)
    name = models.CharField(blank = True,null=True,max_length=255)
    date = models.DateField(auto_now_add =True)
    task = models.TextField()
    from_time =models.TimeField(auto_now=False)
    to_time =models.TimeField(auto_now=False)
    

    def __str__(self):
        # return self.employee.first_name +" " + self.employee.last_name
        return self.name 
    
   


