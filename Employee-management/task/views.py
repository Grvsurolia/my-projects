from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from employees.models import User
from .models import Task
from .serializers import TaskSerializer,TaskupdateSerializer
from rest_framework.response import Response 
from django.http import request,Http404




class TaskAdd(CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        request.data['name'] =request.user.first_name+' ' + request.user.last_name
        request.data['employee'] = request.user.id
        if request.user.is_bde or request.user.is_ceo:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data, "status":status.HTTP_201_CREATED,"success":True})
            return Response({"error":serializer.errors, "status":status.HTTP_400_BAD_REQUEST,"success":False})
        return Response({"error":"Permission required", "status":status.HTTP_400_BAD_REQUEST,"success":False})
        




class TaskView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdate(APIView): 
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        queryset = self.get_object(pk)
        serializer = TaskSerializer(queryset)
        return Response({"data":serializer.data,"success":True})


    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        if task.employee.pk == request.user.id or request.user.is_bde  or request.user.is_superuser :
            serializer = TaskupdateSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"success":True})
            return Response({"error":serializer.errors, "status":status.HTTP_400_BAD_REQUEST,"success":False})
        return Response({"message": "Not Authenticated User","status":status.HTTP_400_BAD_REQUEST,"success":True})

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        if task.employee.pk == request.user.id or request.user.is_bde  or request.user.is_superuser :
            task.delete()
            return Response({"message":"successfully deleted","status":False})
        return Response({"message": "Not Authenticated User","status":status.HTTP_400_BAD_REQUEST,"success":True})
        


    