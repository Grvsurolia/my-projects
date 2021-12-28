from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

import employees
from .models import Bankaccount, Department, UpdateRequest, User
from .serializers import (AddDepartmentSerializer, BankaccountSerializer,
                          BankdetailsupdateSerializer,
                          ChangePasswordSerializer, GetEmailSerializer,
                          RegisterSerializer, ResetPasswordSerializer,
                          TokenSerializer, UpdateRequestFormSerializer,
                          UserLoginSerializer, UserUpdateSerializer,EmployeeSerializer)
from employees import serializers

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class RegisterView(generics.CreateAPIView): 
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RegisterSerializer


    def post(self,request,*args,**kwargs):
        print(request.data)
        hr = request.user.is_hr
        ceo = request.user.is_ceo
        super_user = request.user.is_superuser
        serializer = RegisterSerializer(data=request.data)
        if hr or ceo or super_user:
            if serializer.is_valid():
                employee = serializer.save()
                employee.set_password(employee.password)
                employee.full_name = serializer.data['first_name'] +' '+serializer.data['last_name']
                employee.save()
                return Response({"message":"employee successfully registerd",'success':True})
            return Response({"message": serializer.errors,'success':False})
        return Response({"message":"You can't able to create employee",'success':False})


class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        
        if request.data == {}:
            return Response({'message':'Please fill give email and password',"success":False})
        if request.data.get("email")== None or request.data.get("email")== '':
            return Response({'message':'Please Enter Your Email',"success":False})
        elif request.data.get("password")== None or request.data.get("password")== '':
            return Response({'message':'Please Enter Your password',"success":False})

        self.email = request.data.get("email")
        self.password = request.data.get("password")
        user = authenticate(email=self.email, password=self.password)
        
        if user is not None:
            if user.is_delete==False:
                
                if user.password_change or user.is_superuser:
                    login(request,user,backend='django.contrib.auth.backends.ModelBackend',)
                    user_data = {
                    "id":user.id,
                    "name":user.email,
                    "first_name":user.first_name.title(),
                    "last_name": user.last_name.title(),
                    "emp_id":user.employee_code,
                    "is_hr":user.is_hr,
                    "is_ceo":user.is_ceo,
                    "is_cto":user.is_cto,
                    "is_supervisor":user.is_superuser,
                    "is_teamlead":user.is_teamlead,
                    "is_bde":user.is_bde,
                    "password_change":user.password_change,

                    }
                    serializer = TokenSerializer(data={"token": jwt_encode_handler(jwt_payload_handler(user))})
                    serializer.is_valid()
                    return Response({"token":serializer.data['token'],"data":user_data,"success":True})
                return Response(data={"message": "You are First Time Login So first you reset your password After that login ","success":False})
            return Response(data={"message": "You Account is deleted ","success":False})

        return Response(data={"message": "Invalid Username and Password","success":False},status=status.HTTP_400_BAD_REQUEST)


class GenerateToken(generics.CreateAPIView):
    """
    POST get_token/
    """
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
            return Response({"status":status.HTTP_404_NOT_FOUND,"success":False})
        try:
            payload = jwt_payload_handler(user)
            jwt_token = jwt_encode_handler(payload)
            user_email = user.email
            print("email", user_email)
            url = 'http://localhost:3000/auth/token/'+jwt_token
            subject = 'change password  link'
            
            # body = '''your token will be expired in 24 hours..\n f'http://localhost:3000/token/{jwt_token}'
            #     '''
            message = f'''your token will be expired in 24 hours..\n {url} '''
            sender = settings.EMAIL_HOST_USER
            print(sender," sender")
            to = [user_email]
            send_mail(subject,message,sender,to)
            return Response({'email':email,'token':jwt_token,'path':f'http://localhost:3000/auth/token/{jwt_token}/',"success":True})
        except:
            return Response({"status":status.HTTP_404_NOT_FOUND,"success":False})




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
                return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST,"success":False})
                       
            return Response({"message":"password don't match","status":status.HTTP_400_BAD_REQUEST,"success":False})
       
        return Response({"message":'signature has expired',"status":status.HTTP_400_BAD_REQUEST,"success":False})


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
                return Response({"success":True,"message":"Password Successfully Updated"})
            else:
                return Response({"message":"confirm password did't match","success":False})            
        return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST,"success":False})


class RequestFromView(generics.CreateAPIView): 
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdateRequestFormSerializer
    def post(self,request):
        request.data['employee'] = request.user.id
        serializer = UpdateRequestFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "status":status.HTTP_201_CREATED, "success":True})
        return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST,"success":False})



class ViewRequestFrom(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdateRequestFormSerializer
    def get_object(self,pk):
        try:
           
            return UpdateRequest.objects.all().filter(employee=pk)

        except UpdateRequest.DoesNotExist:
            raise Http404

    def get(self, request,pk):
        request_form = self.get_object(pk)
        print(request_form)
        for data in request_form:
            if data.employee.id==request.user.id or request.user.is_hr  or request.user.is_ceo:
                serializer = UpdateRequestFormSerializer(request_form,many=True)
                return Response({"data":serializer.data, "success":True})
            return Response({"message":"You do not have permission to perform this action.", "success":False})


class ViewAllEmployee(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        employee = User.objects.filter(is_delete=False) 
        serializer = RegisterSerializer(employee,many=True)
        return Response({"data":serializer.data, "success":True})



class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserUpdateSerializer
    
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request,pk):
        employee = self.get_object(pk)
        serializer = UserUpdateSerializer(employee)
        return Response({"data":serializer.data, "success":True})
    

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        if request.user.is_hr  or request.user.is_ceo:
            serializer = UserUpdateSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"success":True})
            return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST,"success":False})
        return Response({"message":"you don't have permissions for update Profile", "success":False})



class UserProfileDelete(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        if request.user.is_hr  or request.user.is_ceo:
            if employee.is_delete:
                    return Response({"error":"Does Not exist ", "success":False})
            else:
                employee.is_delete=True
                employee.save()
            return Response({"message":"employee successfully Delete","success":True})
        return Response({"message":"you don't have permissions for Delete Profile", "success":False})


        
    
class BankDetails(generics.CreateAPIView):
    serializer_class = BankaccountSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self,request):
        request.data['employee'] = request.user.id
        serializer = BankaccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "status":status.HTTP_201_CREATED, "success":True})
        return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST, "success":False})

   
class Bankdetailsview(generics.RetrieveUpdateAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self, pk):
        try:
            return Bankaccount.objects.get(pk=pk)
        except Bankaccount.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bankaccount = self.get_object(pk)
        if bankaccount.employee.id == request.user.id or request.user.is_hr  or request.user.is_ceo :
            serializer = BankaccountSerializer(bankaccount)
            return Response({"data":serializer.data,"success":True})
        return Response({"message":"you don't have permissions for view Bankdetails", "success":False})

    def put(self, request, pk, format=None):
        bankaccount = self.get_object(pk)
        if request.user.is_hr  or request.user.is_ceo:
            serializer = BankdetailsupdateSerializer(bankaccount, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"success":True})
            return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST, "success":False})
        return Response({"message":"you don't have permissions for Update Bankdetails", "success":False})


class BankDetailDelete(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self,pk):
        try:
            return Bankaccount.objects.get(pk=pk)
        except Bankaccount.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        bankaccount = self.get_object(pk)
        if request.user.is_hr  or request.user.is_ceo:
            if bankaccount.is_delete:
                    return Response({"message":"Does Not exist ", "success":False})
            else:
                bankaccount.is_delete=True
                bankaccount.save()
            return Response({"message":"bankaccount Successfully Delete ", "success":True})
        return Response({"message":"you don't have permissions for Delete bankaccount", "success":False})

    
class AddDepartment(generics.CreateAPIView):
    serializer_class = AddDepartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self,request):
        if request.user.is_hr  or request.user.is_ceo:
            serializer = AddDepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data, "status":status.HTTP_201_CREATED,"success":True})
            return Response({"error":serializer.errors, "status":status.HTTP_400_BAD_REQUEST, "success":False})
        return Response({"message":"you don't have permissions for Add Department", "success":False})

    def get(self,request):
        # if request.user.is_hr  or request.user.is_ceo:
        queryset = Department.objects.all()
        if queryset == []:
            return Response({"message": "There are no project available"})
        serializer = AddDepartmentSerializer(queryset, many=True)
        return Response({"data": serializer.data, "success": True})
        # return Response({"message":"you don't have permissions for Add Department", "success":False})


class DepartmentUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self,pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request,pk):
        department = self.get_object(pk)
        if request.user.is_hr  or request.user.is_ceo:
            serializer = AddDepartmentSerializer(department)
            return Response({"data":serializer.data,"success":True})
        return Response({"message":"you don't have permissions", "success":False}) 

    def put(self, request, pk, format=None):
        department = self.get_object(pk)
        if request.user.is_hr  or request.user.is_ceo:
            serializer = AddDepartmentSerializer(department, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"success":True})
            return Response({"error":serializer.errors, "status":status.HTTP_400_BAD_REQUEST, "success":False})
        return Response({"message":"you don't have permissions for update Profile", "success":False})


class DepartmentDelete(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self,pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        department = self.get_object(pk)
        if request.user.is_hr  or request.user.is_ceo:
            if department.is_delete:
                    return Response({"message":"Does Not exist ", "success":False})
            else:
                department.is_delete=True
                department.save()
            return Response({"message":"department Successfully Delete ", "success":True})
        return Response({"message":"you don't have permissions for Delete department", "success":False})


class UserOwnProfileUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EmployeeSerializer

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        if request.user.id==pk:
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"success":True})
            return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST, "success":False})
        return Response({"message":"you don't have permissions for Update Profile", "success":False})