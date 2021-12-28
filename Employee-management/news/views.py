import json

import requests
from django.http import Http404, request
from django.shortcuts import render
from employees.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (BirthdayPage, NewjoineePage, NewsAddPage,
                     UpcomingHolidayPage)
from .serializers import (BirthdaySerializer, NewjoineeSerializer,
                          NewsSerializer, UpcomingHolidaySerializer)


class AllNewsView(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NewsSerializer
    
    def get(self,request,*args, **kwargs):
        queryset = NewsAddPage.objects.all().order_by('-id')
        if queryset == []:
            return Response({"message":"There are no events available","success":False})        
        serializer = NewsSerializer(queryset,many=True)
        return Response({"data":serializer.data,"success":False})
        
        
class NewsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NewsSerializer

    def get_object(self, pk):
        try:
            return NewsAddPage.objects.get(pk=pk)
        except NewsAddPage.DoesNotExist:
            raise Http404
     
    def get(self, request, pk):
        news = self.get_object(pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)
    

class NewJoineeAllView(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NewjoineeSerializer

    
    def get(self,request,*args, **kwargs):
        queryset = NewjoineePage.objects.all().order_by('-id')
        if queryset == []:
            return Response({"message":"There are no newjoinee available"})        
        serializer = NewjoineeSerializer(queryset,many=True)
        return Response({"data":serializer.data,"success":True})


class NewJoineesView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NewjoineeSerializer
    
    def get_object(self, pk):
        try:
            return NewjoineePage.objects.get(pk=pk)
        except NewjoineePage.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        newjoinees = self.get_object(pk)
        serializer = NewjoineeSerializer(newjoinees)
        return Response({"data":serializer.data,"success":True})

        
class AllBirthdayView(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BirthdaySerializer 
    
    
    def get(self,request,*args, **kwargs):        
        queryset = BirthdayPage.objects.all().order_by('-id')
        if queryset == []:
            return Response({"message":"There are no birthday available"})        
        serializer = BirthdaySerializer(queryset,many=True)
        return Response({"data":serializer.data,"success":True})
    
    
class BirthdayView(generics.RetrieveUpdateDestroyAPIView):
    
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BirthdaySerializer 
    
    def get_object(self, pk):
        try:
            return BirthdayPage.objects.get(pk=pk)
        except BirthdayPage.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        birthdays = self.get_object(pk)
        serializer = BirthdaySerializer(birthdays)
        return Response({"data":serializer.data,"success":True})
   
from datetime import date
class AllUpcomingHolidays(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpcomingHolidaySerializer   
    
    
    def get(self,request,*args, **kwargs):
        queryset = UpcomingHolidayPage.objects.filter(date__gte=date.today()).order_by('date')

        if queryset == []:
            return Response({"message":"There are no birthday available"})        
        serializer = UpcomingHolidaySerializer(queryset,many=True)
        return Response({"data":serializer.data,"success":True})


class UpcomingHolidayView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpcomingHolidaySerializer   
    

    def get_object(self, pk):
        try:
            return UpcomingHolidayPage.objects.get(pk=pk)
        except UpcomingHolidayPage.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        upcomingholiday = self.get_object(pk)
        serializer = UpcomingHolidaySerializer(upcomingholiday)
        return Response({"data":serializer.data,"success":True})


class Teamprature(generics.ListAPIView):
    
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        city = 'jaipur'
        r = requests.get(url.format(city)).json()
        f = r["main"]["temp"]
        city_weather = {
            'Country':r['sys']['country'],
            'City': city,
            'Fahrenheit': r["main"]["temp"],
            
            'Celsius': (f-32)*5/9,
            'Wind':r['wind']['speed'],
            'Description': r["weather"][0]["description"]
        }
        return Response(city_weather)
