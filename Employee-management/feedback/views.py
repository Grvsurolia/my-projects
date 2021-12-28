from django.shortcuts import render
from . serializers import FeedBackSerializers
from .models import FeedBack
from rest_framework import generics,permissions,status
from rest_framework.response import Response
from django.http import Http404




class AddFeedBack(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FeedBackSerializers

    def post(self,request):
        request.data._mutable = True
        request.data['incident_person'] = request.user.id
        request.data._mutable = False
        serializer = FeedBackSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "status":status.HTTP_201_CREATED, "success":True})
        return Response({"error":serializer.errors, "status":status.HTTP_400_BAD_REQUEST,"success":False})

    def get(self,request):
        feedbacks = FeedBack.objects.all()
        if feedbacks !=[]:
            if request.user.is_ceo or request.user.is_hr:
                serializer = FeedBackSerializers(feedbacks,many=True)
                return Response({"data":serializer.data,"success":True})
                return Response({"message":"You do not have permission to perform this action.", "success":False})
            else:
                feedbacks = FeedBack.objects.filter(incident_person=request.user.id)
                serializer = FeedBackSerializers(feedbacks,many=True)
                return Response({"data":serializer.data,"success":True})
        else:
            return Response({"message":"There are no Feedback available","success":False})


class UpdateFeedBack(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FeedBackSerializers

    def get_object(self, pk):
        try:
            return FeedBack.objects.get(pk=pk)
        except FeedBack.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        queryset = self.get_object(pk)
        if request.user.is_hr  or request.user.is_ceo or request.user.id==queryset.incident_person.id :
            serializer = FeedBackSerializers(queryset)
            return Response({"data":serializer.data,"success":True})
        return Response({"message":"You do not have permission to perform this action.", "success":False})
    

    def put(self, request, pk):
        queryset = self.get_object(pk)
        if request.user.is_hr or request.user.is_ceo or request.user.id==queryset.incident_person.id:
            serializer = FeedBackSerializers(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"success":True})
            return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST, "success":False})
        return Response({"message":"you don't have permissions for Update Profile", "success":False})


class ViewFeedback(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FeedBackSerializers

    def get(self,request):
        if FeedBack.objects.filter(incident_person__id=request.user.id).exists():
            feedback = FeedBack.objects.filter(incident_person__id=request.user.id)
            serializer = FeedBackSerializers(feedback,many=True)
            return Response({"data":serializer.data,"success":True})
        return Response({"message":" Does not exist.", "success":False})