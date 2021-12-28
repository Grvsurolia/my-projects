import urllib.request
import copy
import json
import re
from django_filters import rest_framework
from rest_framework import filters
from urllib.request import urlopen
from itertools import chain
import django_filters.rest_framework
from rest_framework import permissions
from CustomUserModel.models import CustomUser
from CustomUserModel.serializers import CustomUserLoginSerializer
from django.http import Http404
from django.shortcuts import render
from rest_framework import filters, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated , IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.conf import settings
from plants.models import Plant, PlantType,WishList
from plants.serializers import ProductSerializer, UserContactSerializer,ProductUpdateSerializer, PlantTypeSerializer, wishListSerializer,plantPostSerilizer
from django_filters import rest_framework as filters
import reverse_geocoder as rg 
import logging
from django.db.models import Q
import datetime


logger = logging.getLogger('django')

class Plants(APIView):
    
    permission_classes = (IsAuthenticated,)    
    authentication_class = JSONWebTokenAuthentication
        
    def post(self, request, format=None):
        if request.data == {}:
            return Response({'response':'plz fill tha all details'})
        if request.user.is_varified:
            request.data._mutable = True
            request.data["owner"] = request.user.id
            request.data._mutable = False
            serializer = plantPostSerilizer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                logger.info("this is a post method")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':"please Activate/Verify Your account",'status':status.HTTP_200_OK})
    

class PlantDetailView(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get_object(self, pk):
        try:
            return Plant.objects.get(pk=pk)
        except Plant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        if request.user.id == queryset.owner.pk or request.user.is_superuser:
            serializer = ProductUpdateSerializer(queryset)
            return Response(serializer.data)
        return Response({'message':'you are not valid user','status':status.HTTP_400_BAD_REQUEST})

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        if request.user.id == queryset.owner.pk or request.user.is_superuser:
            serializer = ProductUpdateSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        
        if (request.user.id == queryset.owner.pk or request.user.is_superuser):
            queryset.delete()
            return Response(status=status.HTTP_200_OK)
        return Response({'message':'you are not authorized user','status':status.HTTP_401_UNAUTHORIZED})



class GetPlantsByUser(generics.ListAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    
    def get(self, request, format=None):
            current_date = datetime.datetime.now().date()
            queryset = Plant.objects.filter(owner = request.user.id)
            serializer = ProductSerializer(queryset,  many=True)
            for data in serializer.data:
                
                submit_date = datetime.datetime.strptime(data['datetime'],'%m/%d/%Y').date()
                #submit_date = datetime.datetime.strptime("01/19/2021",'%m/%d/%Y').date()            
                difference = current_date - submit_date
                data['date_difference']=difference.days
            return Response(serializer.data)
                

class FilterPlant(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Plant.objects.all()
   
    def user_ip(self):
        url = 'https://geolocation-db.com/json'
        response = urllib.request.urlopen(url)
        data = json.load(response)
        city = data['city']
        return city

    def locationFetch(self, request,):
        coordinates = (request.data.get("latitude"), request.data.get("longitude"))
        if coordinates == (None, None):        
            request.data["location"]=""
        else:
            result = rg.search(coordinates) 
            location = result[0]['name']
            request.data._mutable = True
            request.data["location"] = location 
            request.data._mutable = False
        return (request.data["location"])
    
    def get(self,request, *args, **kwargs):
        cityFromLocation = self.locationFetch(request)
        cityFromIP = self.user_ip()
        queryset = ""
        allplants = Plant.objects.all()
        ownerids = []
        for plant in allplants:
            if cityFromLocation:
                if plant.owner.address:
                    if cityFromLocation.lower() in plant.owner.address.lower():
                        ownerids.append(plant.owner.pk)
                        city = cityFromLocation
            elif cityFromIP:
                if plant.owner.address:
                    if cityFromIP.lower() in plant.owner.address.lower():
                        ownerids.append(plant.owner.pk)
                        city = cityFromIP
            else:
                print("No Location found")
      
        allPlantsOwnerIds = Plant.objects.filter(owner__in = ownerids)
        for plant_ids in allPlantsOwnerIds:
            plant_ids.city = city
        allPlantsNotOwnerIds = Plant.objects.exclude(owner__in=ownerids)
        allPlants = list(chain(allPlantsOwnerIds, allPlantsNotOwnerIds)) #Merging two Querysets
        serializer_class = ProductSerializer(allPlants, many=True)
        wishlistIds = []
        wishlistData = WishList.objects.filter(user_id = request.user.id)
        for wishlistdata in wishlistData:
            wishlistIds.append(wishlistdata.plant_id.pk)
        for data in serializer_class.data:
            if data["id"] in wishlistIds:
                data["inWishlist"] = True
            else:
                data["inWishlist"] = False
        logger.info("This is a get function for webget")
        return Response(serializer_class.data)
                
    
class Usercontactapi(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializers_class = UserContactSerializer

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self,request, *args, **kwargs):
        if request.user.is_varified:
            pk = self.kwargs.get('pk')
            user = self.get_object(pk=pk)
            serializer = UserContactSerializer(user)
            return Response(serializer.data)
        return Response({'message':"please Activate/Verify Your Email",'status':status.HTTP_200_OK})


class PlantTypeView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    authentication_class = JSONWebTokenAuthentication
    queryset = PlantType.objects.all()
    serializer_class = PlantTypeSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PlantTypeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlantTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    authentication_class = JSONWebTokenAuthentication
    queryset = PlantType.objects.all()
    serializer_class = PlantTypeSerializer
    

class Wishlist(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        if request.data == {}:
            return Response({"Response":"Please Provide Plant Id"})
        if request.user.is_varified: 
            # request.data._mutable = True  
            request.data['user_id'] = request.user.id
            # request.data._mutable = False
            serializer = wishListSerializer(data = request.data)
            wishListDataCheck = WishList.objects.filter(plant_id=request.data['plant_id'], user_id=request.user.id)
            if len(wishListDataCheck) == 0:   
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message':"this plant is already exist in wishlist",'status':status.HTTP_400_BAD_REQUEST})
        return Response({'message':"please Activate/Verify Your Email",'status':status.HTTP_200_OK})
    
    
class WishListView(generics.ListAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
     
  
    def get(self, request, format=None):
            queryset = WishList.objects.filter(user_id = request.user.id)
            serializer = wishListSerializer(queryset,  many=True)
            for data in serializer.data:
                plant_id = data["plant_id"]
                plantDetails = Plant.objects.get(id = plant_id)
                data["plant_name"] = plantDetails.plant_name
                data["img1"] = settings.MEDIA_URL+plantDetails.img1.name
                data["img2"] = settings.MEDIA_URL+plantDetails.img2.name
                data["img3"] = settings.MEDIA_URL+plantDetails.img3.name
                data["img4"] = settings.MEDIA_URL+plantDetails.img4.name
                data["plant_type"] = plantDetails.plant_type.values()
                data["description"] = plantDetails.description
                data['inWishlist'] = True
            return Response(serializer.data)

    
class WishListDeleteView(generics.RetrieveDestroyAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = wishListSerializer
   
   
    def get_object(self,request,pk):
        try:            
            return WishList.objects.get(plant_id=pk, user_id=request.user.id)
        except CustomUser.DoesNotExist:
            raise Http404
    def get(self, request,pk):

        queryset = self.get_object(request,pk)

        if request.user.id == queryset.user_id.pk or request.user.is_superuser:
            serializer = wishListSerializer(queryset)
            return Response(serializer.data)
        return Response({'message':'you are not valid user','status':status.HTTP_400_BAD_REQUEST})

    def delete(self, request, pk, format=None):
        queryset = self.get_object(request, pk)
        queryset.delete()
        return Response({'message':'plant removed from wishlist',status:status.HTTP_200_OK})
        

class ProductList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Plant.objects.all()
    def get(self, request, format=None):
        if request.GET:
            if request.GET["search"]:
                toSearch = request.GET["search"]
                queryset = Plant.objects.filter(Q(plant_type__name__contains=toSearch) | Q(plant_name__contains=toSearch)).distinct()
        else:
            queryset = Plant.objects.all()
        serializer = ProductSerializer(queryset,  many=True)
        wishlistIds = []
        wishlistData = WishList.objects.filter(user_id = request.user.id)
        for wishlistdata in wishlistData:
            wishlistIds.append(wishlistdata.plant_id.pk)
        for data in serializer.data:
            if data["id"] in wishlistIds:
                data["inWishlist"] = True
            else:
                data["inWishlist"] = False
        return Response(serializer.data)
    
    
class PlantTypeView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = PlantType.objects.all()
    serializer_class = PlantTypeSerializer
    


        
        
    
    
