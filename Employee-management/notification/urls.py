from django.urls import path
from . import views

urlpatterns = [
     path('attendance_notication/<int:pk>/',views.ViewAttendanceNotification.as_view(),name ="attendance_notication"),
     path('leave_notication/<int:pk>/',views.ViewLeaveNotification.as_view(),name ="leave_notication"),
     
]
