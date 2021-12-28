from django.contrib import admin
from .models import Project,OccupiedEmp,BenchList,POCList

# Register your models here.

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display=("project_name__name","emp_name__first_name")

admin.site.register(Project)
admin.site.register(OccupiedEmp)
admin.site.register(BenchList)
admin.site.register(POCList)
