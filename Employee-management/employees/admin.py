from django.contrib import admin

from .models import User,UpdateRequest,Department,Bankaccount




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','CardID','first_name', 'last_name', 'department', 'designation', 'employee_code',"is_hr",'is_supervisor','is_ceo','is_cto','is_teamlead')
    

class EmployeeFeedbackAdmin(admin.ModelAdmin):
    list_display = ('incident_person','incident_name','incident_nature','attach_file')

admin.site.register(UpdateRequest)
admin.site.register(Department)
admin.site.register(Bankaccount)