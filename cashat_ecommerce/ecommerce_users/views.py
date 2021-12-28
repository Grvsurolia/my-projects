from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from .models import User,Seller,SellerAgreement,Address,Coupon
from .serializers import (ChangePasswordSerializer,UserLoginSerializer,RegisterUserSerialiers,SellerSerializer,
                            SellerAgreementSerializer,AddressSerializer,CouponSerializer,ResetPasswordSerializer,
                            UserLoginSerializer,TokenSerializer,ChangePasswordSerializer,GetEmailSerializer,UserUpdateSerializer)

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class RegisterView(generics.CreateAPIView): 
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterUserSerialiers

    def post(self,request,*args,**kwargs):
        serializer = RegisterUserSerialiers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            if serializer.data['is_seller']==True:
                seller = User.objects.get(email=serializer.data['email'])
                if request.data['seller_agreement']==True:
                    Seller.objects.create(user=seller,business_name=request.data['business_name'],seller_agreement=True)
                    return Response({"message":"Seller sucessfully registerd",'sucess':True})
                return Response({"message":"You must accept the agreement",'sucess':True})
            
            return Response({"message":"Customer sucessfully registerd",'sucess':True})
        return Response({"message": serializer.errors,'sucess':False})


class LoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        
        if request.data == {}:
            return Response({'message':'Please fill give email and password',"sucess":False})
        if request.data.get("email")== None or request.data.get("email")== '':
            return Response({'message':'Please Enter Your Email',"sucess":False})
        elif request.data.get("password")== None or request.data.get("password")== '':
            return Response({'message':'Please Enter Your password',"sucess":False})

        self.email = request.data.get("email")
        self.password = request.data.get("password")
        user = authenticate(email=self.email, password=self.password)
        if user is not None:    
            login(request,user,backend='django.contrib.auth.backends.ModelBackend',)
            serializer = TokenSerializer(data={"token": jwt_encode_handler(jwt_payload_handler(user))})
            serializer.is_valid()
            user = User.objects.get(email=self.email)
            # if user.is_seller==True:
                # print("seller ",Seller.objects.filter(user=user).exists())
                # seller = Seller.objects.filter(user=user).exists()
                # if request.data['seller_agreement']==True:
                #     Seller.objects.create(user=user,business_name=request.data['business_name'],seller_agreement=True)
                #     return Response({"message":"Seller sucessfully registerd",'sucess':True})
                # return Response({"message":"You must accept the agreement",'sucess':True})
            return Response({"token":serializer.data['token'],"sucess":True})
        return Response(data={"message": "Invalid credentials","sucess":False},status=status.HTTP_400_BAD_REQUEST)



class GenerateToken(generics.CreateAPIView): 
    permission_classes = (permissions.AllowAny,)
    serializer_class = GetEmailSerializer
    queryset = User.objects.all()
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        global jwt_token,user
        if not request.data.get('email'):
            return Response({"message":'please enter your correct email address',"success":False})
        email = request.data.get("email",'')
        try:
            user = User.objects.get(email=email) 
        except User.DoesNotExist:
            return Response({"status":status.HTTP_404_NOT_FOUND,"sucess":False})
        try:
            payload = jwt_payload_handler(user)
            jwt_token = jwt_encode_handler(payload)
            user_email = user.email
            print("email", user_email)
            url = 'http://127.0.0.1:8000/auth/token/'+jwt_token
            subject = 'change password  link'
            print("url ", url)
            
            # body = '''your token will be expired in 24 hours..\n f'http://127.0.0.1:8000/token/{jwt_token}'
            #     '''
            message = f'''your token will be expired in 24 hours..\n {url} '''
            sender = settings.EMAIL_HOST_USER
            print(sender," sender")
            to = [user_email]
            send_mail(subject,message,sender,to)
            return Response({'email':email,'token':jwt_token,'path':f'http://127.0.0.1:8000/auth/token/{jwt_token}/',"success":True})
        except:
            return Response({"status":status.HTTP_404_NOT_FOUND,"sucess":False})




class ResetPassword(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ResetPasswordSerializer
    
    def post(self, request,token_data):
        jwt_token_data = jwt_decode_handler(token_data)
        users_id = jwt_token_data['user_id']
        my_user = User.objects.get(id=users_id)
        if my_user is not None:
            new_password = request.data.get('new_password')
            confirm_new_password = request.data.get('confirm_new_password')
            if new_password == confirm_new_password:
                    serializer = ResetPasswordSerializer(data=request.data)
                    if serializer.is_valid():
                        my_user.set_password(serializer.data['new_password'])
                        my_user.password_change=True
                        my_user.save()
                        return Response({'response':'Password updated successfully'})
                    return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST,"sucess":False})
                       
            return Response({"message":"password don't match","status":status.HTTP_400_BAD_REQUEST,"sucess":False})
       
        return Response({"message":'signature has expired',"status":status.HTTP_400_BAD_REQUEST,"sucess":False})


class ChangePasswordView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    def get_object(self, queryset=None):
        return self.request.user

    def put(self,request, *args, **kwargs):
        queryset = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password  = serializer.data.get('new_password')
            new_confirm_password = serializer.data.get('new_confirm_password')
            if new_confirm_password == new_password:
                if not queryset.check_password(old_password):
                    return Response({"old_password": ["Wrong password."]}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                queryset.set_password(serializer.data.get("new_password"))
                queryset.save()
                return Response({"success":True,"message":"Password Sucessfully Updated"})
            else:
                return Response({"message":"confirm password did't match","success":False})            
        return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST,"sucess":False})



class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserUpdateSerializer
    
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request,pk):
        user = self.get_object(pk)
        serializer = UserUpdateSerializer(user)
        return Response({"data":serializer.data, "sucess":True})
    

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"sucess":True})
        return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST,"sucess":False})




    