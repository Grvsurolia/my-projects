# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import DonorTransactionSerializer
from rest_framework.views import APIView
import re
from urllib.request import urlopen
import urllib.request
import json
from django.contrib.sites.shortcuts import get_current_site





# Create your views here.

class DonorTransactionView(APIView):

    permission_classes = (permissions.AllowAny,)    
    
    def user_ip(self):
        url = 'https://geolocation-db.com/json'
        response = urllib.request.urlopen(url)
        data = json.load(response)
        return data
        
    def post(self, request, format=None):
        if (re.match(r'[6789]\d{9}$',request.data.get('phone_number'))):
                pass
        else:
            return Response({"response":"Please enter valid Phone number"})
        locationDataFromIp = self.user_ip()
        # current_site = get_current_site(request)        
        request.data._mutable = True
        for key, value in locationDataFromIp.items():
            request.data[key] = value
        request.data._mutable = False
        serializer = DonorTransactionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)