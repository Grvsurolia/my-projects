import os
import re
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db.models import fields
from rest_framework import serializers
from rest_framework.authentication import (BaseAuthentication,
                                           BasicAuthentication)
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from CustomUserModel.models import CustomUser,Message


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['email','password']
        
        
class CustomUserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id','email','password',]
        

class UserDataViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','last_name','phone_number','address']


class UserProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','first_name','last_name','email','phone_number','address']
        

class PasswordUpdateSerializer(serializers.ModelSerializer):
    
    model = CustomUser
    old_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    
    class Meta:
        model = CustomUser
        fields = ['old_password','new_password1','new_password2']

    def validate_new_password(self, value):
        validate_password(value)
        return value


class ForgetPasswordChangeSerializer(serializers.Serializer):

    """ Forgot Password Change Serializer """

    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)
  

class GetEmailSerializer(serializers.Serializer):

    """ Serializer for Get Email """

    email = serializers.CharField(required=True)


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    response = serializers.CharField()

# class MessageSerilizer(serializers.Serializer):
    
#     class meta:
#         model = Message
#         fields = '__all__'



class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=CustomUser.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=CustomUser.objects.all())
    # sender = serializers.

    class Meta:
        model = Message
        # fields = ['sender', 'receiver', 'message']
        fields = '__all__'



    
