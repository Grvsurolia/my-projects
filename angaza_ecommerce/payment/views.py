import json
from datetime import date, datetime

import requests
from django.http import (Http404, HttpResponse, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from requests import api
from requests.auth import HTTPBasicAuth
from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MPayment
from .serializers import MPaymentSerializer

# import datetime  




# def getAccessToken(request):
#     consumer_key = '0c34a3HAzHphUeWKYpIOjD1Q8DFun1NU'
#     consumer_secret = 'enLxU1GNmktVMOdG'
#     api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
#     r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
#     print(r ,"edrftyuiopo")
#     mpesa_access_token = json.loads(r.text)
#     validated_mpesa_access_token = mpesa_access_token['access_token']
#     return HttpResponse(validated_mpesa_access_token)


class GetAccessToken(generics.CreateAPIView):

    permission_classes = [permissions.IsAuthenticated,]

    def getAccessToken(request):
        consumer_key = '0c34a3HAzHphUeWKYpIOjD1Q8DFun1NU'
        consumer_secret = 'enLxU1GNmktVMOdG'
        api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        mpesa_access_token = json.loads(r.text)
        validated_mpesa_access_token = mpesa_access_token['access_token']
        return validated_mpesa_access_token



class SendPaymentRequest(generics.CreateAPIView):

    permission_classes = [permissions.IsAuthenticated,]

    # def post(self,request):

    #     access_token = GetAccessToken.getAccessToken(request)
    #     letters = string.ascii_letters
    #     random_string =  ''.join(random.choice(letters) for i in range(10))

    #     now = datetime.datetime.now()
    #     current_datetime = now.strftime("%Y%m%d%H%M%S")


    #     print("ccccccccc", type(current_datetime))
    #     print("ccccccccc", current_datetime)


    #     headers = {'Content-Type': 'application/json',
    #                "Authorization": "Bearer %s" % access_token
    #                }

    #     payload = {
    #         "BusinessShortCode": 174379,
    #         "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwODEyMDk1NTIy",
    #         "Timestamp": "20210812112219",
    #         "TransactionType": "CustomerPayBillOnline",
    #         "Amount": 1,
    #         "PartyA": int("254"+request.data["phone_number"]),  #254708374149,
    #         "PartyB": 174379,
    #         "PhoneNumber": int("254"+request.data["phone_number"]),  #254708374149,
    #         "CallBackURL": "https://mydomain.com/path",
    #         "AccountReference": random_string,
    #         "TransactionDesc": "stk push" 
    #         }
    #     print("pppppppppppppp",payload)

    #     response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, json = payload)
    #     print(response.json())
    #     return Response(response.json())


    def post(self, request):
        validated_mpesa_access_token = GetAccessToken.getAccessToken(request)
        # validated_mpesa_access_token ="Qm5Hq9GtaRMjjUPuiXq50KGr75tK"
        unique_id = get_random_string(length=10)
        request.data["Password"]= "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwNzMwMTIyNTAx",
        request.data["Timestamp"]= "20210730122501",
        request.data["CallBackURL"]= "http://dealzmoto.com/callback/",
        request.data["AccountReference"]= unique_id,
        request.data['description']="stk push"
        request.data["PartyB"]=174379
        request.data["PartyA"]=int("254"+request.data["phone_number"])
        request.data["PhoneNumber"]=int("254"+request.data["phone_number"])
        serializer = MPaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        headers = {'Content-Type': 'application/json',"Authorization": "Bearer %s" % validated_mpesa_access_token}
        des = "stk push"
        amount = request.data['Amount']
        payload = {
            "BusinessShortCode": 174379,
            "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwNzMwMTIyNTAx",
            "Timestamp": "20210730122501",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": int("254"+request.data["phone_number"]),
            "PartyB": 174379,
            "PhoneNumber": int("254"+request.data["phone_number"]),
            "CallBackURL": "http://dealzmoto.com/callback/",
            "AccountReference": unique_id,
            "TransactionDesc": des
        }
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        data = requests.post(api_url, json=payload, headers=headers)
        return JsonResponse({'data': data.json()})
   



class CheckPayment(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MPaymentSerializer

    def post(self, request):
        validated_mpesa_access_token = GetAccessToken.getAccessToken(request)
        # validated_mpesa_access_token="Qm5Hq9GtaRMjjUPuiXq50KGr75tK"
        headers = {'Content-Type': 'application/json',
                   "Authorization": "Bearer %s" % validated_mpesa_access_token}
        
        payload ={
                "BusinessShortCode": "174379",
                "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwODAzMTAxMjUy",
                "Timestamp": "20210803101252",
                "CheckoutRequestID": request.data['checkoutrequestid']
            }
        data = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query', headers = headers, json = payload)
        return Response({'data': data.json()})


