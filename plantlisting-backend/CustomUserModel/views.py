import re
import time
from datetime import datetime

import pyotp
import requests
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from django.utils.functional import empty
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings

from CustomUserModel.models import *
from CustomUserModel.models import Authantication, CustomUser
from CustomUserModel.serializers import *

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{6,18}$"


class Login(generics.CreateAPIView):
    
    serializer_class = CustomUserLoginSerializer
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data == {} or (request.data.get('email')== None or request.data.get('password') == None):
            return Response({"response":"please fill all details"})
        self.username = request.data.get("email", "")        
        self.password = request.data.get("password", "")
        active = CustomUser.objects.filter(is_varified=True)
        user = authenticate(username=self.username, password=self.password)
        if user is not None:
                login(request, user)
                serializer = TokenSerializer(data={"token": jwt_encode_handler(jwt_payload_handler(user))})
                serializer.is_valid()
                message = {
                    'token':serializer.data['token'],
                    'is_varified':user.is_varified,
                }
                return Response(message)
        return Response({'response':"Invalid Password or Username",'status':status.HTTP_401_UNAUTHORIZED})

    
class RegisterUsersView(generics.CreateAPIView):
   
    permission_classes = (permissions.AllowAny,)

    serializer_class = CustomUserRegisterSerializer

    def post(self, request, *args, **kwargs):
        if request.data == {} or (request.data.get('email')== None or request.data.get('password') == None):
            return Response({"response":"please fill all details"})
        if not request.data['email'] or ("@" and ".") not in request.data['email']:
            return Response({"Response":"Please Give correct email format"})
        customuser = CustomUser.objects.filter(email=request.data['email'])
        if len(customuser) == 0:
            match_re = re.compile(reg)
            res = re.search(match_re, request.data.get('password'))
            if res:
                user = CustomUser.objects.create_user(
                    email = request.data.get('email'),
                    username = (request.data.get('email')).split("@")[0],
                    password = request.data.get('password'),
                
                )
                user.set_password(str(request.data.get('password')))
                user.save()
                
                payload = jwt_payload_handler(user)
                jwt_token = jwt_encode_handler(payload)
                current_site = get_current_site(request)
                
                email_body = {
                            'user': user,
                            'domain': current_site,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token':jwt_token,
                            }          
                link = reverse('activate', kwargs={
                                'uidb64': email_body['uid'], 'token': email_body['token']})

                subject = 'Activate your account'
                
                activate_url = current_site.domain+link
                message = f'''Hi {user.username}, thank you for registering in our website,
                                Please click the link below and activate your account \n {activate_url}'''
                # body = '<h1>Hi Vivek</h1>'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                send_mail(subject,message,email_from,recipient_list)
                return Response({"status":"success","response":"User Successfully Created"}, status=status.HTTP_201_CREATED)
            return Response({"response":"Password Character must be 6 to 18 digit (alphanumericand special charcter"})
        else:
            return Response ({"response":"this email is already exists",'status':status.HTTP_400_BAD_REQUEST})


class VerificationView(APIView):
    
    permission_classes = (AllowAny,)
    
    def get(self, request, uidb64, token):  
        id = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=id)
        if user.is_varified:
            return Response({'response':"User is already varified"})
        user.is_varified = True
        user.save()
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        serializer = TokenSerializer(data={"token": jwt_encode_handler(jwt_payload_handler(user)),'response':'user activate successfully'})
        serializer.is_valid()
        return Response(serializer.data)
            
    
class AccountActivation(generics.CreateAPIView):
    
    permission_classes = (IsAuthenticated,)
    
    def post(self, request,*args, **kwargs):
        user = request.user
        payload = jwt_payload_handler(user)
        jwt_token = jwt_encode_handler(payload)
        current_site = get_current_site(request)
        email_body = {
                    'user': user,
                    'domain': current_site,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':jwt_token,
                    }          
        link = reverse('activate', kwargs={
                        'uidb64': email_body['uid'], 'token': email_body['token']})
        subject = 'Activate your account'
        activate_url = 'http://'+current_site.domain+link
        message = f'''Hi {user.username}, Click the link below for activating you account\n {activate_url}'''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject,message,email_from,recipient_list)
        return Response({"status":"success","response":"Activation link send sucessfully"}, status=status.HTTP_201_CREATED)


class UpdatePassword(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = PasswordUpdateSerializer(data=request.data)
        
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password1 = serializer.data.get("new_password1")
            new_password2 = serializer.data.get("new_password2")
            if new_password1 == new_password2:
                if not self.object.check_password(old_password):
                    return Response({"Response":"Wrong password"}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                self.object.set_password(serializer.data.get("new_password1"))
                self.object.save()
                return Response({"status":"success","response":"Password Sucessfully Updated"},status=status.HTTP_204_NO_CONTENT)
            return Response({'response':"please give the correct password"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginWithOtp(APIView):
    permission_classes = (AllowAny,)
    counter = 0

    def post(self, request):
        totp = pyotp.TOTP('base32secret3232')

        if request.data.get("otp")==None and request.data.get("email")!=None:
            checkEmailidExist = CustomUser.objects.filter(email = request.data.get("email"))
            if checkEmailidExist:
                email = request.data.get("email")
                if email==None:
                    email=''
                otp = totp.now() # => '492039'
                Authantication.objects.filter(email=email).delete()
                phoneModelObj = Authantication(otp=otp, email=email)
                phoneModelObj.save()
                
                if request.data.get("email") :
                    subject = 'welcome to our website'
                    message = f'Hi your otp is : {otp}, thank you for register.'
                    email_from = settings.EMAIL_HOST_USER 
                    recipient_list = [email] 
                    send_mail(subject, message, email_from, recipient_list )
                    return Response({'response':"Email OTP sent "})
                else:
                    pass
            else:
                return Response({'response':"This email is not Registered, Please Register first"})
        else:
            if request.data.get("otp")!=None and request.data.get("email")!=None:
                user = CustomUser.objects.filter(email = request.data.get("email"))
                email = request.data.get("email")
                getSentOtpFromDBEmail = Authantication.objects.filter(email=email)
                user = user[0]

                if getSentOtpFromDBEmail:
                    if request.data.get("otp")==getSentOtpFromDBEmail[0].otp:
                        Authantication.objects.filter(email=email).delete()
                        if user is not None:
                            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                            serializer = TokenSerializer(data={
                                "token": jwt_encode_handler(
                                    jwt_payload_handler(user)
                                )})
                            serializer.is_valid()
                            message = {
                                'token':serializer.data['token'],
                                'is_varified':user.is_varified,
                                     }
                            time.sleep(30)
                            return Response(message)   
                        return Response({'response':"OTP Matched, Loged in"})
                    else:
                        return Response({'response':"OTP Not Match"})
                else:
                    return Response({'response':"Generate OTP First or Otp Expired"})
            else:
                return Response({'response':"email Or OTP Not Provided"})




class Generate_token(generics.CreateAPIView):
    """
    POST get_token/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = GetEmailSerializer
    queryset = CustomUser.objects.all()
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        global jwt_token,user
        if not request.data.get('email'):
            return Response('please enter your correct email address')
        email = request.data.get("email",'')
        try:
            user = CustomUser.objects.get(email=email) 
        except CustomUser.DoesNotExist:
            return Response({'Response':'This email is not registerd/Incorrect'})
        try:
            payload = jwt_payload_handler(user)
            jwt_token = jwt_encode_handler(payload)
            user_email = user.email
            url = 'https://plantlisting.herokuapp.com/user/token/'+jwt_token
            subject = 'change password link'
            message = f'''your token will be expired in 24 hours..\n {url} '''
            sender = settings.EMAIL_HOST_USER
            to = [user_email]
            send_mail(subject,message,sender,to)
            return Response({'email':email,'token':jwt_token,'path':f'https://plantlisting.herokuapp.com/user/token/{jwt_token}/'})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserForgetPassword(APIView):
    """
    POST activation link/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = ForgetPasswordChangeSerializer

    def post(self, request, token_data):

        jwt_token_data = jwt_decode_handler(token_data)
        users_id = jwt_token_data['user_id']

        my_user = CustomUser.objects.get(id=users_id)

        if my_user is not None:
            new_password = request.data.get('new_password')
            confirm_new_password = request.data.get('confirm_new_password')
            if new_password == confirm_new_password:
                serializer = ForgetPasswordChangeSerializer(data=request.data)
                if serializer.is_valid():
                    my_user.set_password(serializer.data['new_password'])
                    my_user.save()
                    return Response({'response':'Password updated successfully'})
            return Response({"message":"password don't match","status":status.HTTP_400_BAD_REQUEST})
        else:
            return Response('signature has expired')
    
   
class UserProfileUpdateView(generics.RetrieveUpdateAPIView):

    """
        API for updating login recruiter detail or admin can choose recruiter for update by username
        PUT : recuriter/update/ 
    """

    permission_classes = (permissions.IsAuthenticated,)
    
    
    def get_objects(self,request):
        try:
            current_user = request.user
            if current_user.is_varified:
                custom_get =  CustomUser.objects.get(pk=current_user.pk)
                response = {}
                response["user_obj"] = custom_get
                response["status_code"] = 200
                return response
                
            else:
                return Response({"message":"Activate your account"})
        except CustomUser.DoesNotExist:
            
            response = {}
            response["status_code"]=400
            return response
    
    def get(self,request):
        if request.user.is_varified:
            queryset=self.get_objects(request)
            if queryset["status_code"]==400:
                return Response(status=status.HTTP_404_NOT_FOUND)
            elif queryset["status_code"]==200:
                serializer=UserProfileUpdateSerializer(queryset["user_obj"])
                return Response(serializer.data)
        return Response({'Response':'Please Verify Your Email/Activate Your Account'})
        # return Response({'response':'you are not a valid user'})
    
    def put(self,request):
            
        if request.user.is_varified:
            queryset=self.get_objects(request)
            serializer=UserProfileUpdateSerializer(queryset["user_obj"],data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Response':'Please Verify Your Email/Activate Your Account'})
    # return Response({'response':'you are not a valid user'})
        
     
class GetAllUserByAdmin(generics.ListAPIView):
    
    permission_classes = (IsAdminUser,)
    authentication_class = JSONWebTokenAuthentication
    queryset = CustomUser.objects.all()
    serializer_class = UserDataViewSerializer


        

class GoogleView(APIView):
    
    permission_classes = (AllowAny,)
    
    def post(self, request):
        payload = {'access_token': request.data.get("access_token")}  # validate the token
        google_url = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(google_url.text)
        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)
        # create user if not exist
        try:
            user = CustomUser.objects.get(email=data['email'])
        except CustomUser.DoesNotExist:
            user = CustomUser()
            user.username = data['name']
            user.first_name = data['given_name']
            user.last_name = data['family_name']            
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.user_profile = data['picture']
            # user.auth_provider = data['idpId']
            user.is_varified = True
            user.save()
        serializer = TokenSerializer(data={
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
        serializer.is_valid()
        return Response(serializer.data)
    
            
        
class SocialLoginView(generics.GenericAPIView):
    """Log in using facebook"""
    permission_classes = (AllowAny,)
          
    def post(self, request):
        payload = {'access_token': request.data.get("access_token")}  # validate the token
        facebook_url = requests.get('https://graph.facebook.com/me?', params=payload)
        data = json.loads(facebook_url.text)
        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)
        try:
            user = CustomUser.objects.get(email=request.data['email'])
            
        except CustomUser.DoesNotExist:
            user = CustomUser()
            user.username = data['name']
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = request.data['email']
            user.user_profile = request.data['url']
            user.auth_provider = request.data['graphDomain']
            user.is_varified = True
            user.save()
        
        serializer = TokenSerializer(data={
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            
        serializer.is_valid()
        return Response(serializer.data)


class EmailSubscription(APIView):
    
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data.get('email')
        if emailModel.objects.filter(email=data):
            return Response('You are already Subscribd')
        if not data or ("@" and ".") not in data:
            return Response({'response':'Please Provide Correct Email Format'})
        email = emailModel()
        email.email = data
        email.save()
        sender = settings.EMAIL_HOST_USER
        subject = "subscription Email"
        message = f"Thanks For Subscribe Plant Listing {email.email} "
        to = [email.email]
        send_mail(subject,message,sender,to)

        return Response({'message':'thanks for subscribe',"status":status.HTTP_200_OK})


class MessagePost(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        receiver_id = request.data.get('reciever')
        message = Message.objects.filter(sender=request.user.id,receiver=receiver_id) | Message.objects.filter(sender=receiver_id,receiver=request.user.id)
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        sender = CustomUser.objects.get(id = request.user.id)   
        is_read = True
        receiver = CustomUser.objects.get(id =request.data["reciever"])
        timestamp = datetime.now()
        msg = request.data["message"]        
        msg = Message(sender=sender, receiver=receiver, is_read=is_read, message=msg, timestamp=timestamp)
        msg.save()
        return Response({"response":"Message send sucessfully"}, status=status.HTTP_201_CREATED) 
        

# for emp purpose
class MessageGet(APIView):  
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        receiver_id = request.data.get('reciever')
        message = Message.objects.filter(sender=request.user.id,receiver=receiver_id) | Message.objects.filter(sender=receiver_id,receiver=request.user.id)
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)


class CheckVerification(APIView):
    
    """ Check user is verified or not """
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        current_user = CustomUser.objects.get(pk=request.user.id)
        is_verified = current_user.is_varified
        response={}
        response['is_verified']=is_verified
        return Response(response)
