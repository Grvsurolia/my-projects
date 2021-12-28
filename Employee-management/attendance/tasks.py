from attendance.models import Attendance
from django.core.mail import send_mail
from celery import shared_task
from  datetime import date
from employees.models import User
from leave.models import EmployeeLeave
from news.models import UpcomingHolidayPage
from calendar_system.models import EmployeeCalendar
# from rest_framework.response import Response
from attendance.models import Attendance
from django.core.mail import send_mail
from celery import shared_task
import datetime
from employees.models import User
from leave.models import EmployeeLeave
from news.models import UpcomingHolidayPage
# from rest_framework.response import Response
from attendance.models import Attendance
from django.core.mail import send_mail
from celery import shared_task
from datetime import date
from calendar_system.models import EmployeeCalendar

@shared_task
def attendance_task():
    user = User.objects.all(is_delete=False)
    message ="Out Time"
    for u in user:
        if Attendance.objects.filter(employee=u.id).exists():
            lastattendance = Attendance.objects.filter(employee=u.id).order_by('-id')[0]

            if lastattendance.attendance_status=="INTIME":
                combine_time = datetime.datetime.combine(lastattendance.attendance_date, lastattendance.attendance_time)
                combine_current_time = datetime.datetime.combine(lastattendance.attendance_date, datetime.time(23,59))
                work = combine_current_time- combine_time
                email = lastattendance.employee.email
                employee=lastattendance.employee
                name = lastattendance.employee.first_name + " "+ lastattendance.employee.last_name
                attendance_status='OUTTIME'
                hr_message=f" {name} not out punch attendance card"
                subject=f" {name} Attendance Warning"
                att = Attendance(employee=employee, attendance_status=attendance_status,break_time=lastattendance.break_time,working_time=work)
                att.save()
                
                send_mail("Attendance Warning","you are not punch attendance card","developer@externlabs.com",[email])
                # if not (lastattendance.employee.hr_common_email=="")  :
                hr = lastattendance.employee.hr_common_email
                send_mail(subject,hr_message,"developer@externlabs.com",[hr])
            else:        
                print("All Employee punch out card")
        else:
            print(" Employee not available")      
    return message


@shared_task 
def Auto_Leave():
    user = User.objects.filter(is_delete=False)
    message ="successfully "
    if not (UpcomingHolidayPage.objects.filter(date=datetime.date.today()).exists()):
        for u in user:
            if not (Attendance.objects.filter(employee=u.id,attendance_date=datetime.date.today()).exists()):
                if not (EmployeeLeave.objects.filter(employee_id=u,leave_date=datetime.date.today()).exists()):
                    EmployeeLeave.objects.create(employee_id=u,leave_date=datetime.date.today(),leave_type="casual leave",status="Pending")
    return message



@shared_task
def auto_calendar():
    message = " Add Calendar Successfully"
    user = User.objects.filter(is_delete=False)
    for u in user:
        if UpcomingHolidayPage.objects.filter(date=date.today()).exists():
            holiday=UpcomingHolidayPage.objects.get(date=date.today())
            EmployeeCalendar.objects.create(employee=u,status=holiday.name)
        elif Attendance.objects.filter(employee=u.id,attendance_date=date.today()).exists():
            lastattendance = Attendance.objects.filter(employee=u.id,attendance_date=date.today()).order_by('-id')[0]
            EmployeeCalendar.objects.create(employee=u,status=lastattendance.working_time)
        elif EmployeeLeave.objects.filter(employee_id=u,leave_date=date.today()).exists():
            EmployeeCalendar.objects.create(employee=u,status="leave")
        elif (date.today().weekday() == 5 or date.today().weekday() == 6):
            EmployeeCalendar.objects.create(employee=u,status="weekend") 
        else:
            EmployeeCalendar.objects.create(employee=u,status="leave")
    return message
