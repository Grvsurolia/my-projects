from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['id','employee',"poc_project","project",'name',"date",'task','from_time','to_time']


class TaskupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name',"date","poc_project","project",'task','from_time','to_time']