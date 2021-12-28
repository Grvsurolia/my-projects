from django.test import TestCase
from rest_framework.test import APITestCase, force_authenticate, APIClient
from rest_framework import status
from chat.models import chatUser, Message
from CustomUserModel.models import CustomUser, phoneModel

# Create your tests here.



# class PersonModelTestCase(APITestCase):
    
#     def setUp(self):
        
#         self.user1 = CustomUser.objects.create(email="testuser1@gmail.com", password='78910')
#         self.user2 = CustomUser.objects.create(email= "testuser2@gmail.com", password='12345')
        
#         self.person1 = Person.objects.create(user1=self.user1, user2=self.user2)
#         self.person2 = Person.objects.create(user1 = self.user2, user2=self.user1)
        
#     def test_person(self):
        
#         user1 = Person.objects.get(user1 = self.user1)
#         user2 = Person.objects.get(user1 = self.user2)
#         self.assertEqual(user1.get_user(),"testuser1@gmail.com with testuser2@gmail.com")
        