from django.contrib import admin
from  .models import  Documentation

# Register your models here.
@admin.register(Documentation)
class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('doc_name','file_type','file','date_time')
