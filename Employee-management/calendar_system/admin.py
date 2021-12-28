from django.contrib import admin
from .models import EmployeeCalendar



@admin.register(EmployeeCalendar)
class UserAdmin(admin.ModelAdmin):
    list_display = ('employee','today_date','status')
    