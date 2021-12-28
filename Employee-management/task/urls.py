from django.urls import path
from task import views
# from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('', views.TaskAdd.as_view(), name="task"),
    path ('taskview/',views.TaskView.as_view(), name="taskview"),
    path ('taskupdate/<int:pk>/',views.TaskUpdate.as_view(), name="Taskupdate")

   
]
