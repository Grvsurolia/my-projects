from rest_framework import serializers
from .models import EmployeeCalendar

class EmployeeCalendarSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeCalendar  
        fields = '__all__'

