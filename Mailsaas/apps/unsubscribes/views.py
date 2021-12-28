import csv
import io

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404, HttpResponse, JsonResponse, request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, serializers, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UnsubcribeCsv, UnsubscribeEmail
from .serializers import UnsubscribeEmailSerializers
from apps.campaign.models import CampaignRecipient
# from apps.campaign.serializers CampaignRecipient

class UnsubscribeEmailAdd(CreateAPIView):
    serializer_class = UnsubscribeEmailSerializers
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self,request):
        postdata = request.data
        print("request.data", postdata)
        for email in postdata["email"]:
            recipients = CampaignRecipient.objects.filter(email=email,campaign__assigned=request.user.id).exists()
            if recipients:
                campaign_recipient = CampaignRecipient.objects.filter(email=email,campaign__assigned=request.user.id)
                for recipient in campaign_recipient:
                    recipient.unsubscribe=True
                    recipient.save()

            data = {
                "email" : email,
                'user':request.user.id
            }
       
           
            data_list = []
            serializer = UnsubscribeEmailSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                data_list.append(serializer.data)            
        return Response({"message":"Unsubcribe Successfully done","success":True})
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            
   
class UnsubcribeCsvEmailAdd(CreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self,request):
        csv_file = request.data['csv_file']
        csv_obj = UnsubcribeCsv(unscribe_emails=csv_file)
        csv_obj.save()
        with open('media/'+str(csv_obj.unscribe_emails)) as csv_file:
            
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            resp = []
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    data = {'email':row[0], 'name':row[1],'user':request.user.id}
                    
                    

                    serializer = UnsubscribeEmailSerializers(data = data)
                    if serializer.is_valid():
                        line_count += 1
                        serializer.save()
                        recep = CampaignRecipient.objects.get(email=data['email'])
                        if data['email'] == recep.email:
                            recep.unsubscribe = True
                            recep.save()
                        resp.append(serializer.data)
                    
                        
            resp.append({"success":True})
            return Response(resp)


class UnsubcribeEmailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UnsubscribeEmailSerializers
    def get(self,request):
        params = list(dict(request.GET).keys())
        # print(params)
        if ["search"] in params:
            toSearch = request.GET['search']
            unsubcribe = UnsubscribeEmail.objects.filter(Q(email__contains=toSearch)|Q(name__contains=toSearch),user=request.user.id,on_delete=False)
        else:
            unsubcribe = UnsubscribeEmail.objects.filter(user=request.user.id,on_delete=False)
        serializer=UnsubscribeEmailSerializers(unsubcribe, many=True)
        return Response(serializer.data)


class UnsubcribeEmailDelete(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UnsubscribeEmailSerializers 
    def get_object(self, pk):
        return UnsubscribeEmail.objects.get(pk=pk)
        
    def put(self, request, format=None):
        data =request.data["data"]
        
        for pk in data:
            try:
                unsubcribe = self.get_object(pk)
                if unsubcribe.on_delete:
                    return Response("Does Not exist ")
                else:
                    recipients = CampaignRecipient.objects.filter(email=unsubcribe.email,campaign__assigned=request.user.id).exists()
                    if recipients:
                        campaign_recipient = CampaignRecipient.objects.filter(email=unsubcribe.email,campaign__assigned=request.user.id)
                        for recipient in campaign_recipient:
                            recipient.unsubscribe=False
                            recipient.save()

                    unsubcribe.on_delete=True
                    unsubcribe.save()
            except UnsubscribeEmail.DoesNotExist:
                return Response("Does Not exist ")
        return Response("Unsubcribe Recipient Successfully Done ")
       

 
  