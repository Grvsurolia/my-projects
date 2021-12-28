from rest_framework import serializers
from django.contrib.auth import models
from django.db.models import fields
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'



