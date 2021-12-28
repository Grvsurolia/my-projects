
# Create your models here.
from django.db import models
from django.utils import timezone
from employees.models import User

    
STATUS_CHOICE = [
        ('approved', 'Approved'),
        ('pending','Pending'),
        ('reject', 'Reject')]

LEAVETYPE_CHOICE= [
        ("casual leave", 'Casual Leave'),
        ("sick leave", 'Sick Leave'),
        ("comp off", 'Comp Off'),
        ("block leave", 'Block Leave'),
        ("maternity leave", 'Maternity Leave'),
        ("paternity leave", 'Paternity Leave'),
        ("bereavement leave", 'Bereavement Leave'),
        ("half-day", 'Half-Day'),
        ("other", "Other")]

class LeaveApplication(models.Model):
    
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Employees")
    leave_type = models.CharField(choices=LEAVETYPE_CHOICE,max_length=50, blank=True)    
    apply_date = models.DateField(auto_now_add = True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    no_of_days = models.IntegerField(default=0)
    reason=models.TextField()
    to_time = models.TimeField(auto_now_add=True)
    from_time = models.TimeField(auto_now_add=True)
    onetime_hr_status =models.BooleanField(default=False)
    overall_status = models.CharField(choices=STATUS_CHOICE,max_length=10, default="pending")
    total_leave = models.IntegerField(default=12)
    remaining_leave = models.IntegerField(default=0)

    def __str__(self):
        return str(self.employee)

    def save(self, *args, **kwargs):
        self.remaining_leave = self.total_leave-self.no_of_days
        super(LeaveApplication, self).save(*args, **kwargs)


class EmployeeLeave(models.Model):
    leaves_apply = models.ForeignKey(LeaveApplication,on_delete=models.CASCADE,blank=True,null=True)
    leave_date = models.DateField(auto_now=False,blank=True,null=True)
    leave_type = models.CharField(choices=LEAVETYPE_CHOICE,default="casual leave",max_length=255)
    employee_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    status = models.CharField(choices=STATUS_CHOICE,max_length=10, default="pending")

    def __str__(self):
        return self.employee_id
    

    
class EmployeeCancelLeave(models.Model):
    leaves_apply = models.ForeignKey(LeaveApplication,on_delete=models.CASCADE,blank=True,null=True)
    leave_date = models.DateField(auto_now=False,blank=True,null=True)
    leave_type = models.CharField(choices=LEAVETYPE_CHOICE,default="casual leave",max_length=255)
    employee_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    status = models.CharField(choices=STATUS_CHOICE,max_length=10, default="reject")