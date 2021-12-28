from project_tracking.models import BenchList,OccupiedEmp,Project,POCList,PocWorkEmployees
from celery import shared_task
import datetime
from employees.models import User
from django.db.models import Q

@shared_task
def bench_employees(self):
    occupied_list = []
    poc_list= []
    message = "Add all employee in bench"
    if PocWorkEmployees.objects.filter(is_active=True).exists():
        poc=PocWorkEmployees.objects.filter(is_active=True)
        for project_poc in poc:
            poc_list.append(project_poc.emp_name.id)

    if OccupiedEmp.objects.filter(is_active=True).exists():
        queryset=OccupiedEmp.objects.filter(is_active=True)
        users = User.objects.filter(Q(department__status='technical')|Q(department__name__contains='graphic'),is_delete=False)
        benchs = BenchList.objects.all()
        bench_list = []
        
        for bench in benchs:
            bench_list.append(bench.name.id)
        for occupied in queryset:
            occupied_list.append(occupied.emp_name.id)
        for user in users:
            if user.id in occupied_list or user.id in bench_list or user.id in poc_list:
                pass
            else:
                BenchList.objects.create(name=user) 
        return 