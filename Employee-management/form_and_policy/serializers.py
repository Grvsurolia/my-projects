from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers

from .models import Documentation


class DocumentationSerilizer(serializers.ModelSerializer):
    
    """ Serializer for user login """
    
    class Meta:
        model = Documentation
        fields = '__all__'



