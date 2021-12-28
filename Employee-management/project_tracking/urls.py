from django.urls import path
from . import views


urlpatterns = [
    path('', views.AddProject.as_view(), name="Add_project"),
    path("all_projects/",views.ViewAllProject.as_view(), name="all_projects"),
    path("update_project/<int:pk>/",views.UpdateProject.as_view(), name="update_project"),
    path("addpoc_project/",views.AddPocProject.as_view(), name="Add_Poc_Project"),
    path("all_poc_projects/",views.ViewAllPocProject.as_view(), name="all_poc_projects"),
    path("update_poc/<int:pk>/",views.UpdatePOCProject.as_view(), name="update_poc"),
    path("occupied_employee/",views.AllCurrentlyOccupiedEmployee.as_view(), name="occupied_employee"),
    path("allactive_poc_employee/",views.ActivePocProjectEmployee.as_view(), name="allactive_poc_employee"),
    path("all_poc_employee/",views.AllPocProjectingEmployees.as_view(), name="all_poc_employee"),

    path("project_working_emp/",views.AllProjectWorkingEmployee.as_view(), name="project_working_emp"),
    path("update_occupied_list/<int:pk>/",views.UpdateOccupiedListEmployee.as_view(), name="update_occupied_list"),
    path("bench_employees/",views.AllBenchEmployee.as_view(), name="bench_employees"),    

] 