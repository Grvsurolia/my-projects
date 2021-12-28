# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

import re

import pyotp
from admin_user import serializers
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from validate_email import validate_email

from .models import Contact, Customer, CustomerAddress, Subscribe, User
from .serializers import (ChangePasswordSerializer, ContactSerializer,
                          CustomerAddressSerializer, GetEmailSerializer,
                          LoginSerializer, RegisterSerializer,
                          ResetPasswordSerializer, ShowUserSerializer,
                          SubscribeSerializer, TokenSerializer, UserSerializer,
                          UserUpdateSerializer)

# Create your views here.
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{6,18}$"


class RegisterCustomersView(generics.GenericAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.data.get('email')).exists()
        if user:
            return Response({"message": "this email is already exists", 'status': status.HTTP_400_BAD_REQUEST})
        totp = pyotp.TOTP('base32secret3232')
        otp = totp.now()  # => '492039'
    # 
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            print('serializer.data',serializer.data)
            user = serializer.create(validated_data=serializer.data)
            subject, from_email = 'Activate your account', settings.EMAIL_HOST_USER
            text_content = 'plain text body message.'
            html_content = '<p>Hi '+user.email + \
                    ', thank you for registering in our website, OTP to activate your account</p>\n<h2>'+otp+'</h2>'

            update_user = User.objects.filter(email=user.email).update(lastEmailOtp=otp,role=1,is_active=False)

            send_mail(subject, text_content, settings.EMAIL_HOST_USER, [user.email], html_message = html_content)
            return Response({"message": "User has been created", 'status':status.HTTP_201_CREATED})
        return Response({"message": "Error in data", 'status': status.HTTP_400_BAD_REQUEST})



class verifyEmailOtp(generics.CreateAPIView):
    # Get to Create a call for OTP
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer


    def post(self, request, *args, **kwargs):
        if request.data.get("email") == None or request.data.get("email") == "":
            return Response({"response": "Please provide Email"})
        if (request.data.get("otp") == None or request.data.get("otp") == "") and request.data.get("email") != None:
            totp = pyotp.TOTP('base32secret3232')
            otp = totp.now()  # => '492039'
            user = User.objects.filter(email=request.data.get('email'))
            if user:
                user = user[0]
                user.lastEmailOtp = int(otp)
                user.is_active = True
                user.save()
                from_email =  settings.EMAIL_HOST_USER
                params = {"username":user.username,"otp":otp}
                email_message = render_to_string("templates/verify.html",params)
                send_mail("Activate your account","Active otp",from_email,[user.email],html_message=email_message)
                return Response({'response': "New OTP Generated, and sent to your email"})
            else:
                return Response({'response': "User not found"})
        elif (request.data.get("otp") != None or request.data.get("otp") != "") and (request.data.get("email") != None or request.data.get("email") != ""):
            email = request.data.get("email")
            user = User.objects.filter(email=email)

            if user:
                user = user[0]
                if request.data.get("otp") == user.lastEmailOtp:
                    user.lastEmailOtp = ""
                    user.is_active = True
                    user.save()
                    login(request, user,
                          backend='django.contrib.auth.backends.ModelBackend')
                    serializer = TokenSerializer(data={"token": jwt_encode_handler(jwt_payload_handler(user))})
                    user_serializer = UserSerializer(user)
                    serializer.is_valid()

                    # return Response(serializer.data)
                    # else:
                    #     return Response({'response':'This Otp is Expired'})
                    return Response({"token": serializer.data, "user": user_serializer.data, "success": True})
                else:
                    return Response({'response': "OTP is Incorrect, enter valid otp or Try Generate OTP", "success": False})
            else:
                return Response({'response': "No user found, Register First", "success": False})

        else:
            return Response({'response': "email Or OTP Not Provided", "success": False})


class LoginUserView(generics.CreateAPIView):

    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    # queryset = ""

    def post(self, request, *args, **kwargs):
        # If No Password but only email
        if (request.data.get("passwordorotp") == None or request.data.get("passwordorotp") == "") and request.data.get("email") != None:
            totp = pyotp.TOTP('base32secret3232')
            otp = totp.now()  # => '492039'
            user = User.objects.filter(email=request.data.get('email'))
            if user:
                user = user[0]
                user.lastEmailOtp = int(otp)
                user.save()
                from_email = settings.EMAIL_HOST_USER
                params = {"otp":otp}
                email_message = render_to_string("templates/login_otp.html",params)
                send_mail('Activate your account', "New Password Otp ", from_email, [user.email], html_message = email_message)
                return Response({'response': "New OTP Generated, and sent to your email"})
            else:
                return Response({'response': "User not found"})
        # if Email and Password Both
        elif (request.data.get("passwordorotp") != None or request.data.get("passwordorotp") != "") and (request.data.get("email") != None or request.data.get("email") != ""):
            email = request.data.get("email")
            password = request.data.get("passwordorotp")
            if request.data == {} or (email == None or email == ""):
                return Response({"response": "please enter email"})
            if (password == None or password == ""):
                return Response({"response": "please enter Password"})
            user = User.objects.filter(email=email)
            if user:
                userWithPass = authenticate(email=email, password=password)
                if userWithPass is not None:
                    login(request, userWithPass)
                    userWithPass.lastEmailOtp = ""
                    # userWithPass[0].save()
                    serializer = TokenSerializer(data={
                        "token": jwt_encode_handler(
                            jwt_payload_handler(userWithPass)
                        )})
                    serializer.is_valid()
                    user_serializer = UserSerializer(userWithPass)
                    return Response({"token": serializer.data, "user": user_serializer.data, "success": True})
                if userWithPass is None:
                    userWithotp = User.objects.filter(
                        email=email, lastEmailOtp=password)
                    if userWithotp.count() != 0 and userWithotp.get().is_active:
                        login(request, userWithotp.get())
                        userWithotp[0].lastEmailOtp = ""
                        # userWithotp[0].save()
                        serializer = TokenSerializer(data={
                            "token": jwt_encode_handler(
                                jwt_payload_handler(userWithotp.get())
                            )})
                        serializer.is_valid()
                        user_serializer = UserSerializer(userWithotp,many=True)
                        return Response({"token": serializer.data,"user": user_serializer.data[0], "success": True})
                    else:
                        return Response({"response": "Please Enter Right Password or OTP", "success": False})
            return Response({'response': "Invalid Password/OTP or Email", 'status': status.HTTP_401_UNAUTHORIZED, "success": False})


class GenerateToken(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = GetEmailSerializer
    queryset = User.objects.all()

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        global jwt_token, user
        if not request.data.get('email'):
            return Response({"message": 'please enter your correct email address', "success": False})
        email = request.data.get("email", '')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "success": False})
        try:
            payload = jwt_payload_handler(user)
            jwt_token = jwt_encode_handler(payload)
            user_email = user.email
            params ={"link_url":'https://www.dealzmoto.com/account/newpassword?token='+jwt_token}
            sender = settings.EMAIL_HOST_USER
            to = [user_email]
            email_message = render_to_string("templates/forget.html", params)
            send_mail("change password  link", "forget password link ", sender, to, html_message = email_message)
            return Response({'email': email, 'token': jwt_token, 'path': f'localhost:3000/account/newpassword?token={jwt_token}/', "success": True})
        except:
            return Response({"status": status.HTTP_404_NOT_FOUND, "success": False})



class ResetPassword(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        users_id = request.data['user_id']
        my_user = User.objects.get(id=users_id)
        if my_user is not None:
            new_password = request.data.get('new_password')
            serializer = ResetPasswordSerializer(data=request.data)
            if serializer.is_valid():
                my_user.set_password(serializer.data['new_password'])
                my_user.save()
                return Response({'response': 'Password updated successfully', "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})

        return Response({"message": 'signature has expired', "status": status.HTTP_400_BAD_REQUEST, "success": False})


class ChangePasswordView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get('new_password')
            new_confirm_password = serializer.data.get('new_confirm_password')
            if new_confirm_password == new_password:
                if not queryset.check_password(old_password):
                    return Response({"old_password": ["Wrong password."]},
                                    status=status.HTTP_400_BAD_REQUEST)
                queryset.set_password(serializer.data.get("new_password"))
                queryset.save()
                return Response({"success": True, "message": "Password Sucessfully Updated"})
            else:
                return Response({"message": "confirm password did't match", "success": False})
        return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})


class UserProfileUpdateView(generics.RetrieveUpdateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserUpdateSerializer

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = ShowUserSerializer(user)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        if request.user.id == pk or request.user.is_superuser or request.user.role == "Admin":
            serializer = UserUpdateSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "sucess": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "You don't permission Update profile", "success": False})


class AddSubscribe(generics.CreateAPIView):

    permission_classes = [permissions.AllowAny, ]
    serializer_class = SubscribeSerializer

    def post(self, request):
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "sucess": True})
        return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})


class AddressAdd(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CustomerAddressSerializer

    def post(self, request):
        request.data['user'] = request.user.id
        serializer = CustomerAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
        return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})


class GetCustomerAddress(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomerAddressSerializer

    def get_object(self, uid):
        try:
            return CustomerAddress.objects.filter(user__id=uid)
        except CustomerAddress.DoesNotExist:
            raise Http404

    def get(self, request, uid):
        address = self.get_object(uid)
        serializer = CustomerAddressSerializer(address, many=True)
        return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})


class AddressUpdateView(generics.RetrieveUpdateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CustomerAddressSerializer

    def get_object(self, pk):
        try:
            return CustomerAddress.objects.get(pk=pk)
        except CustomerAddress.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        address = self.get_object(pk)
        serializer = CustomerAddressSerializer(address)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk, format=None):
        address = self.get_object(pk)
        if request.user.id == address.user.id or request.user.is_superuser or request.user.role == "Admin":
            serializer = CustomerAddressSerializer(address, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "sucess": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "You don't permission Update profile", "success": False})


class CreateContactForm(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"status":status.HTTP_200_OK,"sucess": True})
        return Response({"error":serializer.errors,"status":status.HTTP_400_BAD_REQUEST,"success":False})
