from django.urls import path
from . import views


urlpatterns = [
    path('<int:eid>/',views.EmployeeCalendarView.as_view(),name ="calendar_view"),
    path('update/<int:pk>/',views.EmployeeCalendarUpdate.as_view(),name ="calendar_update"),
    
]





