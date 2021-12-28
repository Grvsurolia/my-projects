from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('attendence_view/<int:id>/',views.AttendanceView.as_view(),name ="attendence_view"),
    path('<str:CardID>/',views.AttendanceAdd.as_view(),name ="attendance"),
    path('filter_date/<int:id>/',views.DateWiseAttendanceView.as_view(),name ="attendance_filter"),
]
