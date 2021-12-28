from django.contrib import admin
from .models import  Attendance
# Register your models here.

# admin.site.register(Attendance)
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("attendance_date","attendance_time","attendance_status","break_time","working_time")

