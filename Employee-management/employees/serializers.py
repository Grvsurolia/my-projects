from django.db.models import fields
from rest_framework import serializers
from .models import User, UpdateRequest, Bankaccount, Department
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = User
        fields = "__all__"
        # fields = ('id','email','employee_code','profile_image','full_name','first_name','last_name','designation','mobile_number','address','password','hr_common_email')
        extra_kwargs = {"password": {"write_only": True}}



class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pan_no','aadhar_id','martial_status','blood_group','pincode','state','address','birth_date','gender','alternative_number','mobile_number','profile_image', 'first_name', 'last_name']


class UserLoginSerializer(serializers.ModelSerializer):

    """ Serializer for user login """

    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True},
        }


class TokenSerializer(serializers.Serializer):

    """ Token Serializer """

    token = serializers.CharField(max_length=255)


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'new_confirm_password']


class UserUpdateSerializer(serializers.ModelSerializer):
    """ serializer for user update """

    class Meta:
        model = User
        fields = ['CardID', "department", 
                'designation', 'gender', 'mobile_number',
                'is_delete','designation','salary'
                "hr_common_email","is_hr","is_supervisor","is_ceo","is_cto","is_bde","is_teamlead"]


class UpdateRequestFormSerializer(serializers.ModelSerializer):

    """ Serializer for user Update Request """

    class Meta:
        model = UpdateRequest
        fields = ("employee", 'profile_image',
                  'first_name', "last_name", 'designation',
                  'mobile_number', 'alternative_number', 'gender',
                  'birth_date', 'address', 'state', 'country', 'pincode',
                  'age', 'blood_group', 'martial_status', 'uid',
                  'pan_no')


class BankaccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bankaccount
        fields = ("employee", 'account_number', "ifsc",
                  "bank_name", "account_holder_name")


class BankdetailsupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bankaccount
        fields = ('account_number', "ifsc", "bank_name", "account_holder_name")


class AddDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)


class GetEmailSerializer(serializers.Serializer):

    """ Serializer for Get Email """

    email = serializers.CharField(required=True)