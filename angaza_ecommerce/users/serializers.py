# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""
from admin_user import models
from django.db.models import fields
from rest_framework import serializers

from .models import Contact, Customer, CustomerAddress, Subscribe, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', "username", "email", "first_name", "last_name", "phone_number", "profile_image","role"]


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    response = serializers.CharField()


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'new_confirm_password']


class GetEmailSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)


class UserUpdateSerializer(serializers.ModelSerializer):
    """ serializer for user update """

    class Meta:
        model = User
        fields = ["first_name", "last_name", "profile_image", "phone_number"]


class ShowUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', "username", "email", "first_name",
                  "last_name", "phone_number", "profile_image"]


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'



class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name","role", "is_active", "password"]
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        customer = Customer.objects.create(user=user)
        return user

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = ["email", "password"]
