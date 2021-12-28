from typing import ClassVar
from django.db.models import fields
from rest_framework import serializers
from .models import LeaveApplication,EmployeeLeave,EmployeeCancelLeave


class LeaveApplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LeaveApplication
        fields = '__all__'
        # fields = ('id','leave_type',"start_date","end_date","no_of_days","reason" ,"to_time" "from_time", "status")




class LeaveApplicationUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LeaveApplication
        fields = ('leave_type',"start_date","end_date","no_of_days","reason" ,"to_time" "from_time", "status")





class EmployeeLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLeave
        fields = '__all__'
    

class EmployeeCancelLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCancelLeave
        fields = '__all__'