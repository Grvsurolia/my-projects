import json
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.contrib.auth.models import AbstractBaseUser
from django.test import TestCase , Client
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIClient
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from CustomUserModel.models import CustomUser, Authantication
from CustomUserModel.serializers import UserProfileUpdateSerializer,CustomUserLoginSerializer,CustomUserRegisterSerializer,UserProfileViewSerializer
from CustomUserModel.urls import RegisterUsersView
from CustomUserModel.views import (LoginView, RegisterUsersView,
                                   UpdatePassword, UserProfileUpdateView,
                                   getPhoneNumberRegistered)

client = Client()

class CustomUserModelTestCase(APITestCase):

    def setUp(self):
        CustomUser.objects.create(username="testuser", password='12345',email="testuser@gmail.com",phone_number=998989898,address='testing address2')
        CustomUser.objects.create(username="testuser1", password="678910", email="testuser1@gmail.com",phone_number=8956237775,address='testing address')

    def test_customuser(self):
        testuser_1 = CustomUser.objects.get(username='testuser')
        testuser_2 = CustomUser.objects.get(username='testuser1')

        self.assertEqual(testuser_1.get_username(),'testuser@gmail.com')
        self.assertEqual(testuser_2.get_username(),'testuser1@gmail.com')

# class phoneModelTestCase(APITestCase):

#     def setUp(self):
#         phoneModel.objects.create(Mobile=9660222632,email='testphone@gmail.com')
#         phoneModel.objects.create(Mobile=9982520263,email='testphone2@gmail.com')

#     def test_phonemodel(self):
#         phone1 = phoneModel.objects.get(email='testphone@gmail.com')
#         phone2 = phoneModel.objects.get(email='testphone2@gmail.com')
#         self.assertEqual(phone1.get_Mobile(),"9660222632 belongs to testphone@gmail.com email.")
#         self.assertEqual(phone2.get_Mobile(),"9982520263 belongs to testphone2@gmail.com email.")


# class CustomUserRegisterViewTestCase(APITestCase):

#     def setUp(self):
#         self.valid_payload = {"email":"ashu@gmail.com","password":"12345",}        
#         self.invalid_payload = {"email":"ashu@gmail.com",'password':'',}        
       

#     def test_Newuser_Register(self):
#         response = client.post(reverse('auth-register'),
#         data = self.valid_payload,
#         cotent_type = 'application/json', )

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
#     def test_newinvalid_user(self):
#         response = client.post(reverse('auth-register'),
#         data = self.invalid_payload,
#         cotent_type = 'application/json', )

#         self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        




# class CustomUserRegisterSerilizerTest(APITestCase):

#     def setUp(self):

#         self.customeuser = CustomUser.objects.create(email='testuser@gmail.com', password='test123')
#         self.serilizer = CustomUserRegisterSerializer(self.customeuser)



#     def test_case_registerserilizer(self):
#         data = self.serilizer.data
#         self.assertEqual(set(data.keys()),set(['email','password']))



# class CustomUserLoginSerializerTest(APITestCase):

#     def setUp(self):

#         self.newuser = CustomUser.objects.create(email='testuser1@gmail.com',password='test1234')
#         self.serilizer = CustomUserLoginSerializer(self.newuser)
        
#     def test_correct(self):
#         data = self.serilizer.data
#         self.assertEqual(set(data.keys()), set(['email','password']))
        

# class CustomUserProfileUpdateSrializerTest(APITestCase):

#     def setUp(self):
#         self.newuser = CustomUser.objects.create(password='12345',email='test2@gmail.com',phone_number=9889566547,address = 'jaipur')
#         self.serilizer = UserProfileUpdateSerializer(self.newuser)


#     def test_userupdation(self):
#         data = self.serilizer.data
#         self.assertEqual(set(data.keys()), set(['username','first_name','last_name','phone_number','address']))


# class CustomUserProfileViewSerializerTest(APITestCase):
    
#     def setUp(self):
#         self.newuser = CustomUser.objects.create(username='test2',password='12345',email='test2@gmail.com',phone_number=9889566547,address = 'jaipur')
#         self.serilizer = UserProfileViewSerializer(self.newuser)

#     def test_userprofileview(self):
#         data = self.serilizer.data
#         self.assertEqual(set(data.keys()), set(['username','first_name','last_name','email','phone_number','address']))
        

# class CustomUserRegisterViewTest(APITestCase):
    
#     def test_user_register(self):
#         data = {'email':'test@gmail.com','password':'12345'}
#         res = self.client.post(reverse('auth-register'), data)
#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        
    

        
# class CustomeUserLogin(APITestCase):

#     login_url = reverse('auth-login')
    
#     def setUp(self) -> None:
#         self.client = APIClient()
#         self.new_user = CustomUser.objects.create_user(
#             email="ashuhardaska26@gmail.com",
#             password="12345",
#         )
        
        
#     def test_login_validuser(self):
        
#         data = {
            
#             'email':'ashuhardaska26@gmail.com',
#             'password':"12345"
#         }
       
      
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
#         token = response.data['token']
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
#     def test_login_InvalidPassword(self):
        
#         data = {
            
#             'email':'ashuhardaska26@gmail.com',
#             'password':"1234599"
#         }
       
      
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,response.content)
#         # token = response.data['token']
#         # self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
#     def test_login_InvalidUser(self):
        
#         data = {
            
#             'email':'ashuhardaska@gmail.com',
#             'password':"12345"
#         }
       
      
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,response.content)
#         # token = response.data['token']
#         # self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        
# # class CustomeuserLoginByOtp(APITestCase):
      
# #     login_url = reverse('OTP_Gen')
    
# #     def setUp(self) -> None:
# #         self.client = APIClient()
# #         self.new_user = CustomUser.objects.create_user(
# #             email="ashuhardaska26@gmail.com",
# #             password="12345",
# #             phone_number = 9660222632,
        
# #         )
        
# #     def test_login_byPhone(self):
        
# #         data = {
# #             # 'phone_number' : 9660222632,
# #             # 'otp':789548,
# #         }
        
# #         response = self.client.post(self.login_url,data,format='json')
# #         print(response,"***************")
# #         self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
# #         token = response.data['token']
# #         self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
    
         
        
# class PasswordUpdateSerializerTest(APITestCase):
#     """ test case class for password update serializer """
#     pass_update_url = reverse('password_update')
    
#     login_url = reverse('auth-login')
    
#     def setUp(self) -> None:
#         self.client = APIClient()
#         self.new_user = CustomUser.objects.create_user(
#             email="test2@gmail.com",
#             password="12345",
           
#         )
#         self.old_pass = self.new_user.password
    
#     def test_user(self):
#         data = {
#             'email':'test2@gmail.com',
#             'password':12345
#         }
#         password_data = {
#             'old_password':'12345',
#             'new_password1':'ashu123',
#             'new_password2':'ashu123',
#         }
        
#         response = self.client.post(self.login_url,data,format='json')
        
#         self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        
#         token = response.data['token']
        
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
#         response_update_password = self.client.put(self.pass_update_url,password_data,format='json')
        
#         self.assertEqual(response_update_password.status_code,status.HTTP_204_NO_CONTENT)
        
        
#     def test_Confirm_PassWrong(self):
        
#         data = {
#             'email':'test2@gmail.com',
#             'password':12345
#         }
#         password_data = {
#             'old_password':'12345',
#             'new_password1':'ashu123',
#             'new_password2':'ashu1234',
#         }
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
#         token = response.data['token']
        
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
#         response_update_password = self.client.put(self.pass_update_url,format='json')
        
#         self.assertNotEqual(response_update_password.status_code,status.HTTP_204_NO_CONTENT)

    
#     def test_Old_PassWrong(self):
        
#         data = {
#             'email':'test2@gmail.com',
#             'password':12345
#         }
#         password_data = {
#             'old_password':'1234566',
#             'new_password1':'ashu123',
#             'new_password2':'ashu1234',
#         }
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        
#         token = response.data['token']
        
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
#         response_update_password = self.client.put(self.pass_update_url,format='json')
        
#         self.assertNotEqual(response_update_password.status_code,status.HTTP_204_NO_CONTENT)
        

# class UserProfileUpdateView(APITestCase):
          
#     login_url = reverse('auth-login')
    
#     def setUp(self) -> None:
#         self.client = APIClient()
#         self.new_user = CustomUser.objects.create_user(
#             email="ashuhardaska26@gmail.com",
#             password="12345",
#         )
        
        
#     def test_update_Validuserprofile(self):
        
#         data = {
            
#             'email':'ashuhardaska26@gmail.com',
#             'password':"12345"
#         }
#         self.valid_data = {
#             "username":"ashu",
#             "first_name": "ashutosh",
#             "last_name": "sharma",
#             "phone_number": 9660222632,
#             "address": "jaipur"
#         }
      
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
#         token = response.data['token']
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
#         response = self.client.put(
#             reverse('UpdateProfile', kwargs={'pk': self.new_user.pk}),
#             data = json.dumps(self.valid_data),
#             content_type = 'application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        
#     def test_update_InValidDataProfile(self):
        
#         data = {
#             'email':'ashuhardaska26@gmail.com',
#             'password':'12345'
#         }
        
#         self.Invalid_data = {
#             "first_name": "ashutosh",
#             "last_name": "sharma",
#             "phone_number": 9660222632,
            
#         }
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
#         token = response.data['token']
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
#         response = self.client.put(
#             reverse('UpdateProfile', kwargs={'pk': self.new_user.pk}),
#             data = json.dumps(self.Invalid_data),
#             content_type = 'application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
#     def test_UpdateProfile_InvalidUser(self):
        
#         data = {
#             'email':'gaurav@gmail.com',
#             'password':'12345'
#         }
        
#         self.valid_data = {
#             "first_name": "ashutosh",
#             "last_name": "sharma",
#             "phone_number": 9660222632,
#             "address": "jaipur"
            
            
#         }
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,response.content)
       
        
#         response = self.client.put(
#             reverse('UpdateProfile', kwargs={'pk': self.new_user.pk}),
#             data = json.dumps(self.valid_data),
#             content_type = 'application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
        
# class RegisterUserDetailUpdateTestByAdmin(APITestCase):
          
#     login_url = reverse('auth-login')
    
#     def setUp(self) -> None:
#         self.client = APIClient()
#         self.new_user = CustomUser.objects.create_user(
#             email="ashuhardaska26@gmail.com",
#             password="12345",
#         )
#         self.new_user.is_superuser = True
#         self.new_user.save()
        
#         # self.new_user2 = CustomUser.objects.create_user(email='pawan@gmail.com',password='12345')
#         # self.new_user2.save()
#     def test_update_Validuserprofile(self):
        
#         data = {
            
#             'email':'ashuhardaska26@gmail.com',
#             'password':"12345"
#         }
#         self.valid_data = {
#             "username":"ashu",
#             "first_name": "ashutosh",
#             "last_name": "sharma",
#             "phone_number": 9660222632,
#             "address": "jaipur"
#         }
      
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
#         token = response.data['token']
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
#         response = self.client.put(
#             reverse('UpdateProfile', kwargs={'pk': self.new_user.pk}),
#             data = json.dumps(self.valid_data),
#             content_type = 'application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        
#     def test_update_InValidDataProfile(self):
        
#         data = {
#             'email':'ashuhardaska26@gmail.com',
#             'password':'12345'
#         }
        
#         self.Invalid_data = {
#             "first_name": "ashutosh",
#             "last_name": "sharma",
#             "phone_number": 9660222632,
            
#         }
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
#         token = response.data['token']
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
#         response = self.client.put(
#             reverse('UpdateProfile', kwargs={'pk': self.new_user.pk}),
#             data = json.dumps(self.Invalid_data),
#             content_type = 'application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
#     def test_UpdateProfile_InvalidUser(self):
        
#         data = {
#             'email':'gaurav@gmail.com',
#             'password':'12345'
#         }
        
#         self.valid_data = {
#             "first_name": "ashutosh",
#             "last_name": "sharma",
#             "phone_number": 9660222632,
#             "address": "jaipur"
            
            
#         }
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,response.content)
       
        
#         response = self.client.put(
#             reverse('UpdateProfile', kwargs={'pk': self.new_user.pk}),
#             data = json.dumps(self.valid_data),
#             content_type = 'application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
#     def test_UpdateProfileBy_UnauthUser(self):
        
        
#         # self.setUp().new_user.is_staff
#         # print(self.setUp().new_user.is_staff)
        
#         data = {
#             'email':'pawan@gmail.com',
#             'password':'12345'
#         }
        
#         self.valid_data = {
#             "first_name": "ashu21",
#             "last_name": "shar",
#             "phone_number": 9660222632,
#             "address": "jaipur"
            
            
#         }
        
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,response.content)
       
        
#         response = self.client.put(
#             reverse('UpdateProfile', kwargs={'pk': self.new_user.pk}),
#             data = json.dumps(self.valid_data),
#             content_type = 'application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

#     def test_DeleteApi_ValidUser(self):
        
#         data = {
            
#             'email':'ashuhardaska26@gmail.com',
#             'password':"12345"
#         }        
       
      
#         response = self.client.post(self.login_url,data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
#         token = response.data['token']
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
#         # self.plant = Product.objects.create(plant_name='testplant',description='this is a test plant', owner=self.new_user)
        
#         response = self.client.delete(
#             reverse('UpdateProfile', kwargs={'pk': self.new_user.pk}))
        
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)