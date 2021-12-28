from django.test import TestCase,Client
from .models import Plants, PlantType
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse 
from .serializers import ProductSerializer,UserContactSerializer, ProductUpdateSerializer, PlantTypeSerializer
from CustomUserModel.models import CustomUser
from rest_framework import status
# from rest_framework.authtoken.models import Token
import json
from django.contrib.gis.geos import Point, WKBWriter

client = Client()

class PlantTypeModelTest(APITestCase):

    def setUp(self):
        PlantType_obj = PlantType.objects.create(name='flower')

    def test_planttype(self):
        plnat1 = PlantType.objects.get(name='flower')
        self.assertEqual(plnat1.get_name(),'flower')
        
    def test_wrong_planttype(self):
        plant = PlantType.objects.get(name='flower')
        self.assertNotEqual(plant.get_name(), 'floower')



class ProductModelTestCase(APITestCase):
    
    def setUp(self):
        self.user_obj = CustomUser.objects.create(username='user1',password='12345',email='test@gmail.com')
        
        new_plant = Plants.objects.create(plant_name='rose', description = 'flower Plant',quantity=10, owner=self.user_obj)
        
    def test_plants_models(self):
        plant = Plants.objects.get(plant_name = 'rose')
        self.assertEqual(plant.get_plantname(),'rose is flower Plant')
        
        
    def test_wrong_plants_model(self):
        plant = Plants.objects.get(plant_name='rose')
        self.assertNotEqual(plant.get_plantname(),'sunflower is flower Plant')
        
    

class ProductGetTestCase(APITestCase):

    def setUp(self):
        # self.PlantType_obj1 = PlantType.objects.create(name='flower')
        # self.PlantType_obj2 = PlantType.objects.create(name='Vegetable')
        # # philip = Author.objects.create(first_name="Philip", last_name="K. Dick")
        # # juliana = Author.objects.create(first_name="Juliana", last_name="Crain")
        # plant1.plant_type.set([self.PlantType_obj1.pk, self.PlantType_obj2.pk])
        # self.assertEqual(plant1.plant_type.count(), 2)
        
        self.user_obj1 = CustomUser.objects.create(email='test@gmail.com',password='12345')
        
        self.plant1 = Plants.objects.create(plant_name="testplant1",description='this is a test flower',quantity=5,owner=self.user_obj1,)
        self.plant2 = Plants.objects.create(plant_name="testplant2",description="this is a test flower 2", quantity=15,owner=self.user_obj1,)
        self.plant3 = Plants.objects.create(plant_name="testplant3",description="this is a test flower 3",quantity=10, owner=self.user_obj1,)

    def test_all_get(self):
        response = client.get(reverse('plant-post'))
        pt = Plants.objects.all()
        serializer = ProductSerializer(pt, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class ProductpostTestCase(APITestCase):
    """ test case class for password update serializer """
    plant_post_url = reverse('Plants')
    
    login_url = reverse('auth-login')
    
    def setUp(self) -> None:
        self.client = APIClient()
        self.new_user = CustomUser.objects.create_user(
            email="test2@gmail.com",
            password="12345",
           
        )
        
    
    def test_post_plant(self):
        data = {
            'email':'test2@gmail.com',
            'password':'12345',
        }
        plant_data = {
            'plant_name':'rose',
            'description':'this is rose plant',
            'quantity':15,
        
        }
        
        response = self.client.post(self.login_url,data,format='json')
        
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        
        token = response.data['token']
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        plant_post = self.client.post(self.plant_post_url,plant_data,format='json')
        
        self.assertEqual(plant_post.status_code,status.HTTP_201_CREATED)
        
    def test_post_plant_unauthorize(self):
        
        data = {
            'email':'test2@gmail.com',
            'password':'123465'
        }
        plant_data = {
            'plant_name':'rose',
            'description':'this is rose plant',
        }
        
        response = self.client.post(self.login_url,data,format='json')
        
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,response.content)
        
        # token = response.data['token']
        
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        plant_post = self.client.post(self.plant_post_url,plant_data,format='json')
        
        self.assertEqual(plant_post.status_code,status.HTTP_401_UNAUTHORIZED)
        
    
    def test_post_WrongPlantData(self):
        
        data = {
            'email':'test2@gmail.com',
            'password':'12345'
        }
        plant_data = {
            'plant_name':'rose',
        }
        
        response = self.client.post(self.login_url,data,format='json')
        
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        
        token = response.data['token']
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        plant_post = self.client.post(self.plant_post_url,plant_data,format='json')
        
        self.assertEqual(plant_post.status_code,status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(APITestCase):
          
    login_url = reverse('auth-login')
    product_url = reverse('Plants')
    
    def setUp(self) -> None:
        self.client = APIClient()
        self.new_user = CustomUser.objects.create_user(
            email="ashuhardaska26@gmail.com",
            password="12345",
        )
        
        
    def test_update_ByValidUser(self):
        
        data = {
            
            'email':'ashuhardaska26@gmail.com',
            'password':"12345"
        }
       
      
        self.valid_data = {
            'plant_name' : 'new rose',
            'description' : 'this is a new rose flower plant',
            'quantity' : 10,
        }
        response = self.client.post(self.login_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        self.plant = Plants.objects.create(plant_name='testplant',description='this is a test plant', quantity=5,owner=self.new_user)
        
        response = self.client.put(
            reverse('PlantDetailUpdate', kwargs={'pk': self.plant.pk}),
            data = json.dumps(self.valid_data),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
  
    def test_update_ByInValidUser(self):

      
      
       
      
        self.valid_data = {
            'plant_name' : 'new rose',
            'description' : 'this is a new rose flower plant',
            'quantity' : 10,
        }
        # response = self.client.post(self.login_url,data,format='json')
        # self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        # token = response.data['token']
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        self.plant = Plants.objects.create(plant_name='testplant',description='this is a test plant', quantity=5,owner=self.new_user)
        
        response = self.client.put(
            reverse('PlantDetailUpdate', kwargs={'pk': self.plant.pk}),
            data = json.dumps(self.valid_data),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    
    def test_update_InValidData(self):
        
        data = {
            
            'email':'ashuhardaska26@gmail.com',
            'password':"12345"
        }        
       
      
        self.valid_data = {
            # 'plant_name' : 'new rose',
            'description' : 'this is a new rose flower plant',
            'quantity' : 10,
            
        }
        response = self.client.post(self.login_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        self.plant = Plants.objects.create(plant_name='testplant',description='this is a test plant', quantity=5,owner=self.new_user)
        
        response = self.client.put(
            reverse('PlantDetailUpdate', kwargs={'pk': self.plant.pk}),
            data = json.dumps(self.valid_data),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_DeleteApi_ValidUser(self):
        
        data = {
            
            'email':'ashuhardaska26@gmail.com',
            'password':"12345"
        }        
       
      
        response = self.client.post(self.login_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        self.plant = Plants.objects.create(plant_name='testplant',description='this is a test plant',quantity=5, owner=self.new_user)
        
        response = self.client.delete(
            reverse('PlantDetailUpdate', kwargs={'pk': self.plant.pk}))
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        


class GetPlantsByUserTestCase(APITestCase):
    
    
    login_url = reverse('auth-login')
    
    def setUp(self) -> None:
        self.client = APIClient()
        self.new_user = CustomUser.objects.create_user(
            email="ashuhardaska26@gmail.com",
            password="12345",
        )
        self.plant = Plants.objects.create(plant_name='testplant',description='this is a test plant', quantity=5,owner=self.new_user)
        
        
    # def test_get_ByValidUser(self):
        
    #     data = {
            
    #         'email':'ashuhardaska26@gmail.com',
    #         'password':"12345"
    #     }
       
      
       
    #     response = self.client.post(self.login_url,data,format='json')
    #     self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
    #     token = response.data['token']
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
    #     response = self.client.get(
    #         reverse('usercontactview', kwargs={'pk': self.plant.pk}))
    #     pt = Product.objects.all()
    #     serializer = ProductSerializer(pt, many=True)
    #     # self.assertEqual(response.data, serializer.data)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_get_ByInValidUser(self):
        
        data = {
            
            'email':'gaurav@gmail.com',
            'password':"123456"
        }
       
      
       
        response = self.client.post(self.login_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,response.content)
        # token = response.data['token']
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        response = self.client.get(
            
            reverse('usercontactview', kwargs={'pk': self.plant.pk}))
        pt = Plants.objects.all()
        serializer = ProductSerializer(pt, many=True)
        # self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
         
        
class PlantTypePostByAdminTestCase(APITestCase):
    """ test case class for password update serializer """
    PlantType_post_url = reverse('PlantTypePost')
    
    login_url = reverse('auth-login')
    
    def setUp(self) -> None:
        self.client = APIClient()
        self.new_user = CustomUser.objects.create_user(
            email="test2@gmail.com",
            password="12345",
           
        )
        self.new_user.is_staff = True
        self.new_user.save()
        
        # self.new_user2 = CustomUser.objects.create_user(email="newuser@gmail.com",password='test@123')
        # self.new_user2.save()
    
    def test_post_planttype(self):
       
        
        data = {
            'email':'test2@gmail.com',
            'password':'12345',
        }
        plant_data = {
            'name':'flower',
        }
        
        response = self.client.post(self.login_url,data,format='json')
        
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        
        token = response.data['token']
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        plant_post = self.client.post(self.PlantType_post_url,plant_data,format='json')
        
        self.assertEqual(plant_post.status_code,status.HTTP_201_CREATED)
        
    def test_postptype_byinvaliduser(self):
       
        
        data = {
            'email':'test@gmail.com',
            'password':'12345',
        }
        plant_data = {
            'name':'flower',
        }
        
        response = self.client.post(self.login_url,data,format='json')
        
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,response.content)

        
        plant_post = self.client.post(self.PlantType_post_url,plant_data,format='json')
        
        self.assertEqual(plant_post.status_code,status.HTTP_401_UNAUTHORIZED)

    
    def test_PostPtypeByInvalidData(self):
       
        
        data = {
            'email':'test2@gmail.com',
            'password':'12345',
        }
        plant_data = {
            
            
        }
        
        response = self.client.post(self.login_url,data,format='json')
        
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        
        token = response.data['token']
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        plant_post = self.client.post(self.PlantType_post_url,plant_data,format='json')
        
        self.assertEqual(plant_post.status_code,status.HTTP_400_BAD_REQUEST)
        
        
class PlantTypeUpdateView(APITestCase):
          
    login_url = reverse('auth-login')
    # product_url = reverse('PlantUpdate')
    
    def setUp(self) -> None:
        self.client = APIClient()
        self.new_user = CustomUser.objects.create_user(
            email="ashuhardaska26@gmail.com",
            password="12345",
        )
        self.new_user.is_staff = True
        self.new_user.save()
    
    def test_update_ByValidUser(self):
        
        data = {
            
            'email':'ashuhardaska26@gmail.com',
            'password':"12345"
        }
       
      
        self.valid_data = {
           
           'name':'grass'
        }
        response = self.client.post(self.login_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        self.P_type = PlantType.objects.create(name='flower')
        
        response = self.client.put(
            reverse('UpdateP_Type', kwargs={'pk': self.P_type.pk}),
            data = json.dumps(self.valid_data),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
  
    def test_update_ByInValidUser(self):

  
      
        self.valid_data = {
            
            'quantity' : 10,

        }
        # response = self.client.post(self.login_url,data,format='json')
        # self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        # token = response.data['token']
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        
        self.P_type = PlantType.objects.create(name='flower')

        
        response = self.client.put(
            reverse('UpdateP_Type', kwargs={'pk': self.P_type.pk}),
            data = json.dumps(self.valid_data),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    
    def test_update_InValidData(self):
        
        data = {
            
            'email':'ashuhardaska26@gmail.com',
            'password':"12345"
        }        
       
      
        self.valid_data = {
            
            
        }
        response = self.client.post(self.login_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        self.P_type = PlantType.objects.create(name='flower')
        
        response = self.client.put(
            reverse('UpdateP_Type', kwargs={'pk': self.P_type.pk}),
            data = json.dumps(self.valid_data),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_DeleteApi_ValidUser(self):
        
        data = {
            
            'email':'ashuhardaska26@gmail.com',
            'password':"12345"
        }        
       
      
        response = self.client.post(self.login_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        self.P_type = PlantType.objects.create(name='flower')
        
        response = self.client.delete(
            reverse('UpdateP_Type', kwargs={'pk': self.P_type.pk}))
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ProductPostSrializerTest(APITestCase):

    def setUp(self):
        self.newuser = CustomUser.objects.create(email='test2@gmail.com',password='12345')
        self.newproduct = Plants.objects.create(plant_name='rose',description='this is a  flower plant type',quantity=5,owner=self.newuser,)

        self.serializer = ProductSerializer(self.newproduct)
    
    def test_post_product(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id','plant_name','plant_type','other_p_type','description','quantity','owner','img','status','datetime',]))


class UserContactSerilizerTestCase(APITestCase):

    def setUp(self):
        self.newuser = CustomUser.objects.create(email='test2@gmail.com',password='12345')

        self.serializer = UserContactSerializer(self.newuser)
        
    def test_user_contact(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['first_name','last_name','email','phone_number','address']))
        
class ProductUpdateSerializerTestCase (APITestCase):
    
    
    def setUp(self):
            
        self.newuser = CustomUser.objects.create(email='test2@gmail.com',password='12345')
        self.plant = Plants.objects.create(plant_name='testplant',description='this is a test plant',quantity=5, owner=self.newuser)

        self.serializer = ProductUpdateSerializer(self.plant)
        
    def test_plant_update(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['plant_name','plant_type','other_p_type','description','quantity','img','status']))
    
    

class PlantTypePostSerializerTest(APITestCase):

    def setUp(self):
        # self.newuser = CustomUser.objects.create(username='test2',password='12345',email='test2@gmail.com',phone_number=9889566547,location='jsipur')
        self.plant_type = PlantType.objects.create(name='flower')
        self.serializer = PlantTypeSerializer(self.plant_type)

    def test_post_plantype(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()),set(['name']))
        
class ProductUpdateByAdminView(APITestCase):
          
    login_url = reverse('auth-login')
    # product_url = reverse('PlantUpdate')
    
    def setUp(self) -> None:
        self.client = APIClient()
        self.new_user = CustomUser.objects.create_user(
            email="ashuhardaska26@gmail.com",
            password="12345",
        )
        self.new_user.is_staff = True
        self.new_user.save()
    def test_update_ByValidUser(self):
        
        data = {
            
            'email':'ashuhardaska26@gmail.com',
            'password':"12345"
        }
       
      
        self.valid_data = {
            'plant_name' : 'new rose',
            'description' : 'this is a new rose flower plant',
            'quantity' : 10,
        }
        response = self.client.post(self.login_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        self.plant = Plants.objects.create(plant_name='testplant',description='this is a test plant', quantity=5,owner=self.new_user)
        
        response = self.client.put(
            reverse('PlantDetailUpdate', kwargs={'pk': self.plant.pk}),
            data = json.dumps(self.valid_data),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
  
    def test_update_ByInValidUser(self):

      
      
       
      
        self.valid_data = {
            'plant_name' : 'new rose',
            'description' : 'this is a new rose flower plant',
            'quantity' : 10,
        }
        # response = self.client.post(self.login_url,data,format='json')
        # self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        # token = response.data['token']
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        self.plant = Plants.objects.create(plant_name='testplant',description='this is a test plant',quantity=5, owner=self.new_user)
        
        response = self.client.put(
            reverse('PlantDetailUpdate', kwargs={'pk': self.plant.pk}),
            data = json.dumps(self.valid_data),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    
    def test_update_InValidData(self):
        
        data = {
            
            'email':'ashuhardaska26@gmail.com',
            'password':"12345"
        }        
       
      
        self.valid_data = {
            # 'plant_name' : 'new rose',
            'description' : 'this is a new rose flower plant',
            'quantity' : 10,
            
        }
        response = self.client.post(self.login_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        self.plant = Plants.objects.create(plant_name='testplant',description='this is a test plant',quantity=5, owner=self.new_user)
        
        response = self.client.put(
            reverse('PlantDetailUpdate', kwargs={'pk': self.plant.pk}),
            data = json.dumps(self.valid_data),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_DeleteApi_ValidUser(self):
        
        data = {
            
            'email':'ashuhardaska26@gmail.com',
            'password':"12345"
        }        
       
      
        response = self.client.post(self.login_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK,response.content)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        
        self.plant = Plants.objects.create(plant_name='testplant',description='this is a test plant',quantity=5, owner=self.new_user)
        
        response = self.client.delete(
            reverse('PlantDetailUpdate', kwargs={'pk': self.plant.pk}))
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
