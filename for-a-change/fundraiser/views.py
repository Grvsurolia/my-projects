# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import CustomUser, Fundraiser, frComments
from donor.models import DonorTransaction
from .serializers import TokenSerializer,CustomUserSerializer, FundraiserSerializer, DoCommentsSerializer, AdminUpdateRequestFundraiserSerializer
from rest_framework.response import Response
import re
from rest_framework_jwt.settings import api_settings
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import (DjangoUnicodeDecodeError, force_bytes, force_text)
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.urls import reverse
import pyotp
from validate_email import validate_email
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db.models import Avg, Count, Min, Sum
import datetime
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date 
from django_filters import rest_framework as filters
from django.db.models import Q
from django.http import HttpResponse, Http404


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{6,18}$"

# Campaigner Register
class RegisterUsersView(generics.CreateAPIView):
   
    permission_classes = (permissions.AllowAny,)

    # serializer_class = CustomUserRegisterSerializer

    def post(self, request, *args, **kwargs):
        email_is_valid = validate_email(request.data.get('email'))
        if not email_is_valid:
            return Response({"response":"Please enter valid email"})
        elif request.data.get('password')== None or request.data.get('password')== "":
            return Response({"response":"please enter password"})
        elif request.data.get('full_name')== None or request.data.get('full_name')== "":
            return Response({"response":"please enter full name"})
        elif request.data.get('user_profile')== None or request.data.get('user_profile')== "":
            return Response({"response":"please enter profile photo"})
        elif request.data.get('phone_number')==None or request.data.get('phone_number')=="":
            return Response({"response":"please enter phone number"})
        if (re.match(r'[6789]\d{9}$',request.data.get('phone_number'))):
                # if CustomUser.objects.filter(phone_number=request.data.get('phone_number')):
                #     return Response({"response":"Phone Number Already Registered, Please Login"})
                pass
        else:
            return Response({"response":"Please enter valid Phone number"})
        
        customuser = CustomUser.objects.filter(email=request.data['email'])
        if len(customuser) == 0:
            match_re = re.compile(reg)
            res = re.search(match_re, request.data.get('password'))
            totp = pyotp.TOTP('base32secret3232')
            otp = totp.now() # => '492039'
            if res:
                user = CustomUser.objects.create_user(
                    full_name = request.data.get('full_name'),
                    email = request.data.get('email'),
                    username = (request.data.get('email')).split("@")[0],
                    password = request.data.get('password'),
                    lastEmailOtp = otp,
                    user_profile = request.data.get('user_profile'),
                    phone_number = request.data.get('phone_number'),
                    is_active = False,
                )
                group = Group.objects.get(name='campaigner')
                user.groups.add(group)
                user.set_password(str(request.data.get('password')))
                user.save()
                
                subject, from_email = 'Activate your account', settings.EMAIL_HOST_USER
                text_content = 'plain text body message.'
                html_content = '<p>Hi '+user.username+', thank you for registering in our website, OTP to activate your account</p>\n<h2>'+otp+'</h2>'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [user.email])

                msg.attach_alternative(html_content, "text/html")
                msg.send()
                # subject = 'Activate your account'
                
                # message = f'''Hi {user.username}, thank you for registering in our website, OTP to activate your account \n{otp}'''
                
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [user.email]
                # print(message)
                # send_mail(subject,message,email_from,recipient_list)
                return Response({"status":"success","response":"Successfully Registered, a verification code has been sent to the provided email"}, status=status.HTTP_201_CREATED)
            return Response({"message":"Password Character must be 6 to 18 digit (alphanumericand special charcter"})
        else:
            return Response ({"message":"this email is already exists",'status':status.HTTP_400_BAD_REQUEST})


# Campaigner Verify Email
class verifyEmailOtp(generics.CreateAPIView):
    # Get to Create a call for OTP
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        if request.data.get("email")==None or request.data.get("email")=="":
            return Response({"response":"Please provide Email"})
        if (request.data.get("otp")==None or request.data.get("otp")=="") and request.data.get("email")!=None:
            totp = pyotp.TOTP('base32secret3232')
            otp = totp.now() # => '492039'
            user = CustomUser.objects.filter(email = request.data.get('email'))
            if user:
                user = user[0]
                user.lastEmailOtp = int(otp)
                user.is_active = True
                user.save()
                subject, from_email = 'Activate your account', settings.EMAIL_HOST_USER
                text_content = 'plain text body message.'
                html_content = '<p>Hi '+user.username+', Your New Generated OTP is</p><h2>\n'+ otp +'</h2>'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [user.email])

                msg.attach_alternative(html_content, "text/html")
                msg.send()
                # subject = 'Activate your account'
                
                # message = f'''Hi {user.username}, Your New Generated OTP is\n{otp}'''
                
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [user.email]
                # print(message)
                # send_mail(subject,message,email_from,recipient_list)
                return Response({'response':"New OTP Generated, and sent to your email"})
            else:
                return Response({'response':"User not found"})
        elif (request.data.get("otp")!=None or request.data.get("otp")!="") and (request.data.get("email")!=None or request.data.get("email")!=""):
            email = request.data.get("email")
            user = CustomUser.objects.filter(email = email)

            if user:
                user = user[0]
                if request.data.get("otp")==user.lastEmailOtp:
                    user.lastEmailOtp = ""
                    user.is_active = True
                    user.save()
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    serializer = TokenSerializer(data={
                        "token": jwt_encode_handler(
                            jwt_payload_handler(user)
                        )})
                    serializer.is_valid()
                    
                    # return Response(serializer.data)
                    # else:
                    #     return Response({'response':'This Otp is Expired'})
                        
                    return Response({'response':serializer.data})
                else:
                    return Response({'response':"OTP is Incorrect, enter valid otp or Try Generate OTP"})
            else:
                return Response({'response':"No user found, Register First"})
        
        else:
            return Response({'response':"email Or OTP Not Provided"})


# Campaigner Login
class LoginView(generics.CreateAPIView):
    
    # serializer_class = CustomUserLoginSerializer
    permission_classes = (permissions.AllowAny,)

    # queryset = ""

    def post(self, request, *args, **kwargs):
        #If No Password but only email
        if (request.data.get("passwordorotp")==None or request.data.get("passwordorotp")=="") and request.data.get("email")!=None:
            totp = pyotp.TOTP('base32secret3232')
            otp = totp.now() # => '492039'
            user = CustomUser.objects.filter(email = request.data.get('email'))
            if user:
                user = user[0]
                user.lastEmailOtp = int(otp)
                user.save()
                subject, from_email = 'Activate your account', 'developer@externlabs.com'
                text_content = 'plain text body message.'
                html_content = '<p>Your New Generated OTP is:</p><h2>\n'+ otp +'</h2>'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [user.email])

                msg.attach_alternative(html_content, "text/html")
                msg.send()
                # subject = 'Activate your account'
                
                # message = f'''Hi {user.username}, Your New Generated OTP is:\n{otp}'''
                
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [user.email]
                # print(message)
                # send_mail(subject,message,email_from,recipient_list)
                return Response({'response':"New OTP Generated, and sent to your email"})
            else:
                return Response({'response':"User not found"})
        #if Email and Password Both
        elif (request.data.get("passwordorotp")!=None or request.data.get("passwordorotp")!="") and (request.data.get("email")!=None or request.data.get("email")!=""):
            email = request.data.get("email")        
            password = request.data.get("passwordorotp")
            if request.data == {} or (email== None or email== ""):
                return Response({"response":"please enter email"})
            if (password == None or password == ""):
                return Response({"response":"please enter Password"})
            user = CustomUser.objects.filter(email = email)
            if user:
                userWithPass = authenticate(email=email, password=password)
                if userWithPass is not None:
                    login(request, userWithPass)
                    userWithPass.lastEmailOtp = ""
                    userWithPass.save()
                    serializer = TokenSerializer(data={
                        "token": jwt_encode_handler(
                            jwt_payload_handler(userWithPass)
                        )})
                    serializer.is_valid()
                    return Response(serializer.data)
                if userWithPass is None:
                    userWithotp = CustomUser.objects.filter(email=email, lastEmailOtp=password)
                    if userWithotp.count() != 0 and userWithotp.get().is_active:
                        login(request, userWithotp.get())
                        userWithotp.get().lastEmailOtp = ""
                        userWithotp.save()
                        serializer = TokenSerializer(data={
                            "token": jwt_encode_handler(
                                jwt_payload_handler(userWithotp.get())
                            )})
                        serializer.is_valid()
                        return Response(serializer.data)
                    else:
                        return Response({"response":"Please Activate Account First or Try Generate OTP"})
            return Response({'response':"Invalid Password/OTP or Email",'status':status.HTTP_401_UNAUTHORIZED})


# Create Beneficiary (Campaigner / Admin)
class FundraiserCreate(generics.CreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)    
        
    def post(self, request, format=None):
        if request.user.is_active:
            # print("permisssssssssss ", request.user, request.user.get_group_permissions(), 'fundraiser.add_fundraiser' in request.user.get_group_permissions())
            if 'fundraiser.add_fundraiser' in request.user.get_group_permissions():
                # print("gggggggggg11111 ", Group.objects)
                # print("ggggggggggg22222222 ",Group.objects.get(name="campaigner"))
                # print("grouppppppppppppp ",Group.objects.get(name="campaigner").user_set.filter(id=request.user.id).exists())
                request.data._mutable = True
                request.data["user"] = request.user.id
                request.data["slug"] = "-".join(request.data["title"].split(" "))
                request.data._mutable = False
                serializer = FundraiserSerializer(data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message':"Has No Permissions",'status':status.HTTP_200_OK})
        return Response({'message':"please Activate/Verify Your account",'status':status.HTTP_200_OK})
    

# View Beneficiary
class FundraiserView(APIView):

    permission_classes = [permissions.AllowAny,]
    # authentication_class = JSONWebTokenAuthentication

    def get(self, request, slug):
    
        try:
            # print(request.user)
            fr_profile = Fundraiser.objects.filter(slug=slug, is_active=True)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                }
            frData = []
            allCommentsOfFr =[]
            allTransactions = queryset = DonorTransaction.objects.none()
            for fr in fr_profile:
                # print("fr.pk = ",fr.pk)
                # print(DonorTransaction.objects.filter(fr=fr.pk))
                # totalRaisedAmount = DonorTransaction.objects.filter(fr=fr.pk).aggregate(Sum('amount'))
                # print("tot  =  ",totalRaisedAmount)
                # totalRaisedAmount = totalRaisedAmount["amount__sum"]
                # print("tot2 = ",totalRaisedAmount)

                allCommentsOfFr = frComments.objects.filter(fundraiser=fr.pk)
                allTransactions = DonorTransaction.objects.filter(fr=fr.pk, contributeAnonimusly=False)

                totalRaisedAmount = DonorTransaction.objects.filter(fr=fr).aggregate(Sum('amount'))
                totalRaisedAmount = 0 if totalRaisedAmount["amount__sum"]== None else totalRaisedAmount["amount__sum"]
                from datetime import date 
                today = date.today()
                frLastDateToFund = datetime.datetime.strptime(fr.lastDateToFund, '%Y-%m-%d').date()
                daysLeft = abs(today - frLastDateToFund)
                
                perc = round((float(totalRaisedAmount)/float(fr.goalAmount))*100)

                data = {
                    'id': fr.id,
                    'title': fr.title,
                    'slug': fr.slug,
                    'cause': fr.cause,
                    'beneficiaryFullName': fr.beneficiaryFullName,
                    'beneficiaryAge': fr.beneficiaryAge,
                    'beneficiaryGender': fr.beneficiaryGender,
                    'cityOfResidence': fr.cityOfResidence,
                    'goalAmount': fr.goalAmount,
                    'story': fr.story,
                    'beneficiaryPhoto': settings.MEDIA_URL+str(fr.beneficiaryPhoto),
                    'isPrivate': fr.isPrivate,
                    'lastDateToFund': fr.lastDateToFund,
                    'RaisedAmount': totalRaisedAmount,
                    'daysLeft': daysLeft.days,
                    'percentage': perc,
                }
                frData.append(data)
            response["frData"] = frData
            commentData = []
            for comment in allCommentsOfFr:
                data = {
                    'id': comment.id,
                    'user_name': comment.user.full_name,
                    'user_photo': str(comment.user.user_profile),
                    'fundraiser': str(comment.fundraiser.beneficiaryFullName),
                    'comment': comment.comment,
                    'createdDateTime': comment.created_date_time,
                }
                commentData.append(data)
            response["commentData"] = commentData
            allDonorData = []
            for trans in allTransactions:
                data = {
                    "full_name": trans.full_name,
                    "email": trans.email,
                    "phone_number": trans.phone_number,
                    "DonatedAmount": trans.amount,
                }
                allDonorData.append(data)
            response["allDonorData"] = allDonorData

            topDonorData = []
            allTransactions = allTransactions.order_by("-amount")
            for trans in allTransactions:
                data = {
                    "full_name": trans.full_name,
                    "email": trans.email,
                    "phone_number": trans.phone_number,
                    "DonatedAmount": trans.amount,
                }
                topDonorData.append(data)
            response["topDonorData"] = topDonorData
            

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'error': str(e)
                }
        return Response(response, status=status_code)


# Create comments (Campaigner / Admin)
class DoComments(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)    
        
    def post(self, request, format=None):
        if request.user.is_active:
            if 'fundraiser.add_frcomments' in request.user.get_group_permissions():
                request.data._mutable = True
                request.data["user"] = request.user.id
                request.data["is_active"] = True
                request.data._mutable = False
                serializer = DoCommentsSerializer(data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message':"Has No Permission"})
        return Response({'message':"please Activate/Verify Your account",'status':status.HTTP_200_OK})



# View All Active Beneficiaries
class BrowseFundraisers(generics.ListAPIView):
    
    permission_classes = (permissions.AllowAny,)

    def get(self, request):

        try:
            params = list(dict(request.GET).keys())
            if 'search' in params:
                toSearch = request.GET['search']
                user_profile = Fundraiser.objects.filter(Q(cause__contains=toSearch) | Q(title__contains=toSearch) | Q(slug__contains=toSearch), isPrivate=False, is_active=True)
            elif 'cause' in params:
                toSearch = request.GET['cause']
                user_profile = Fundraiser.objects.filter(cause__contains=toSearch, isPrivate=False, is_active=True)
            else:
                user_profile = Fundraiser.objects.filter(isPrivate=False, is_active=True)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                }
            frData = []
            for user in user_profile:
                totalRaisedAmount = DonorTransaction.objects.filter(fr=user,contributeAnonimusly=False).aggregate(Sum('amount'))
                totalRaisedAmount = 0 if totalRaisedAmount["amount__sum"]== None else totalRaisedAmount["amount__sum"]
                
                today = date.today()
                frLastDateToFund = datetime.datetime.strptime(user.lastDateToFund, '%Y-%m-%d').date()
                daysLeft = abs(today - frLastDateToFund)
                perc = round((float(totalRaisedAmount)/float(user.goalAmount))*100)
                data = {
                    'title': user.title,
                    'CampaignerFullName': user.user.full_name,
                    'beneficiaryFullName': user.beneficiaryFullName,
                    # 'frPhoto': settings.MEDIA_URL+str(user.),
                    'cause': user.cause,
                    'Goalamount': user.goalAmount,
                    # 'isPrivate': user.isPrivate,
                    'raisedAmount': totalRaisedAmount,
                    'beneficiaryPhoto': settings.MEDIA_URL+str(user.beneficiaryPhoto),
                    'daysLeft': daysLeft.days,
                    'percentage': perc,
                }
                frData.append(data)
            response["frData"] = frData
         
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'error': str(e)
                }
        return Response(response, status=status_code)


# View own Beneficiaries
class MyBeneficiaries(generics.ListAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    # authentication_class = JSONWebTokenAuthentication

    def get(self, request):

        try:
            params = list(dict(request.GET).keys())
            if 'search' in params:
                toSearch = request.GET['search']
                user_profile = Fundraiser.objects.filter(Q(cause__contains=toSearch) | Q(title__contains=toSearch) | Q(slug__contains=toSearch) | Q(beneficiaryFullName__contains=toSearch), user = request.user.id)
            else:
                user_profile = Fundraiser.objects.filter(user = request.user.id)
            status_code = status.HTTP_200_OK
            if user_profile:
                response = {
                    'success': 'true',
                    'status code': status_code,
                    'message': 'Beneficiaries fetched successfully',
                    }

                frData = []
                for user in user_profile:
                    totalRaisedAmount = DonorTransaction.objects.filter(fr=user, contributeAnonimusly=False).aggregate(Sum('amount'))
                    totalRaisedAmount = 0 if totalRaisedAmount["amount__sum"]== None else totalRaisedAmount["amount__sum"]
                    # from datetime import date 
                    today = date.today()
                    frLastDateToFund = datetime.datetime.strptime(user.lastDateToFund, '%Y-%m-%d').date()
                    daysLeft = abs(today - frLastDateToFund)
                    perc = round((float(totalRaisedAmount)/float(user.goalAmount))*100)
                    data = {
                        'id': user.id,
                        'title': user.title,
                        'slug': user.slug,
                        'cause': user.cause,
                        'beneficiaryFullName': user.beneficiaryFullName,
                        'beneficiaryAge': user.beneficiaryAge,
                        'beneficiaryGender': user.beneficiaryGender,
                        'cityOfResidence': user.cityOfResidence,
                        'goalAmount': user.goalAmount,
                        'story': user.story,
                        'beneficiaryPhoto': settings.MEDIA_URL+str(user.beneficiaryPhoto),
                        'isPrivate': user.isPrivate,
                        'lastDateToFund': user.lastDateToFund,
                        'RaisedAmount': totalRaisedAmount,
                        'daysLeft': daysLeft.days,
                        'percentage': perc,
                        'is_active': user.is_active,
                    }
                    frData.append(data)
                response["frData"] = frData
            else:
                response = {
                'success': 'true',
                'status code': status_code,
                'message': 'No Beneficiaries',
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'error': str(e)
                }
        return Response(response, status=status_code)


#Update My Inactive Beneficiaries
class UpdateAInactiveBeneficiary(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, frid):
        try:
            return Fundraiser.objects.get(pk=frid)
        except Fundraiser.DoesNotExist:
            raise Http404

    def get(self, request):
        if 'fundraiser.view_fundraiser' in request.user.get_group_permissions():
            fr = self.get_object(request.data['frid'])
            serializer = FundraiserSerializer(fr)
            return Response(serializer.data)
        else:
            return Response({"message":"Has No Permission"})

    def put(self, request):
        if 'fundraiser.change_fundraiser' in request.user.get_group_permissions():
            fr = self.get_object(request.data['frid'])
            if fr.is_active == False:
                serializer = FundraiserSerializer(fr, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
            elif fr.is_active == True:
                request.data._mutable = True
                request.data["frTitle"] = fr.title
                request.data["frid"] = fr.id
                request.data["user"] = request.user.id
                request.data._mutable = False
                serializer = AdminUpdateRequestFundraiserSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"Request to update this Beneficiary has been sent to our team, We will contact you soon"})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Has No Permission"})