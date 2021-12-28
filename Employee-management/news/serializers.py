from django.contrib.auth import models
from rest_framework import serializers
from .models import BirthdayPage,UpcomingHolidayPage,NewsAddPage,NewjoineePage


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsAddPage
        fields = "__all__"


class NewjoineeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewjoineePage
        fields = ['id','name',"designation","emp_image","body","joining_date"]


class BirthdaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BirthdayPage
        fields = ['id','employee_name',"emp_image","birthday_date","body"]
        
        
class UpcomingHolidaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UpcomingHolidayPage
        fields = ['id','name',"date","emp_image","body"]
            
        
        