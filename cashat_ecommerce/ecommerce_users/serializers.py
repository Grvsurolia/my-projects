from django.db.models import fields
from rest_framework import serializers
from .models import User,Seller,SellerAgreement,Address,Coupon


class RegisterUserSerialiers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =['email','first_name','last_name',"phone_number","is_seller","is_customer"]
        extra_kwargs = {"password": {"write_only": True}}


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = "__all__"


class SellerAgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerAgreement
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = "__all__"

class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = "__all__"



class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True},
        }


class TokenSerializer(serializers.Serializer):

    token = serializers.CharField(max_length=255)


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
    confirm_new_password = serializers.CharField(required=True)


class UserUpdateSerializer(serializers.ModelSerializer):
    """ serializer for user update """

    class Meta:
        model = User
        fields = ["first_name","last_name","profile_image"]