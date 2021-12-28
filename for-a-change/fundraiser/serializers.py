# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from rest_framework import serializers
from .models import CustomUser, Fundraiser, frComments
from adminapp.models import RequestedUpdateFundraiser

# class CustomUserRegisterSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = CustomUser
#         fields = ['email','password']

class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id','username','full_name', 'email', 'user_profile' , 'phone_number', 'lastEmailOtp', 'auth_provider', 'groups', 'is_superuser', 'is_staff', 'is_active', 'date_joined']


class FundraiserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fundraiser
        fields = '__all__'

class DoCommentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = frComments
        fields = '__all__'


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    response = serializers.CharField()


class AdminUpdateRequestFundraiserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RequestedUpdateFundraiser
        fields = '__all__'