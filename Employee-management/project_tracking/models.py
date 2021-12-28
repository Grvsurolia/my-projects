from django.db import models
from employees.models import User
from django.utils.translation import gettext as _

status = (
    ('1', 'High'),
    ('2', 'Medium'),
    ('3', 'Low'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)


class Project(models.Model):
    name = models.CharField(max_length=80,unique=True)
    assign = models.ManyToManyField(User)
    start_date = models.DateField(auto_now_add=False)
    dead_line = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False,blank=True)
    description = models.TextField(blank=True)
    client_name = models.CharField(max_length=200)
    company_document = models.FileField(upload_to='company_document',blank=True,null=True)
    client_document = models.FileField(upload_to='client_document',blank=True,null=True)
    status = models.CharField(max_length=7, choices=status, default=1)
    number_of_emp = models.PositiveIntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

class BenchList(models.Model):
    name = models.CharField(_("Employee Name"),max_length=255)

    def __str__(self):
        return self.name

    
class OccupiedEmp(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE) 
    emp_name = models.ForeignKey(User, on_delete=models.CASCADE) 
    is_active = models.BooleanField()

    def __str__(self):
        return self.emp_name.first_name


class POCList(models.Model):
    project_name = models.CharField(_("Project Name"),unique=True,max_length=255)
    assign = models.ManyToManyField(User)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    client_name = models.CharField(_("Client Name"),max_length=255)
    project_description = models.TextField()
    client_documentation = models.FileField(upload_to="poc_client_documentation/",null=True, blank=True)
    company_documentation = models.FileField(upload_to="poc_company_documentation/",null=True, blank=True)
    number_of_emp = models.PositiveIntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return str(self.project_name)
    
class PocWorkEmployees(models.Model):
    project_name = models.ForeignKey(POCList, on_delete=models.CASCADE) 
    emp_name = models.ForeignKey(User, on_delete=models.CASCADE) 
    is_active = models.BooleanField()

    def __str__(self):
        return str(self.emp_name)