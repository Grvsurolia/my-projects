from django.contrib import admin
from .models import LeaveApplication,EmployeeLeave,EmployeeCancelLeave

# admin.site.register(LeaveApplication)
# Register your models here.
@admin.register(LeaveApplication)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','leave_type', 'apply_date', 'start_date', 'end_date', 'overall_status','reason')

admin.site.register(EmployeeCancelLeave)
admin.site.register(EmployeeLeave)