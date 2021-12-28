
from attendance import serializers
from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer
from django.core.mail import send_mail
from django.http import Http404, request
from employees.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Documentation
from .serializers import DocumentationSerilizer
# Create your views here.


class DocumentationView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DocumentationSerilizer

    def post(self,request,*args, **kwargs):
        hr = request.user.is_hr
        admin = request.user.is_superuser
        if hr or admin:
            serializer = DocumentationSerilizer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data, "success":True})
            return Response({"message":serializer.errors, "success":False})
        else:
            return Response({"message":"you do not have permission to perform this action.", "success":False}) 
        
    def get(self,request,*args, **kwargs):
        queryset = Documentation.objects.all()
        if queryset == []:
            return Response({"message":"There are no documents available"})        
        serializer = DocumentationSerilizer(queryset,many=True)
        return Response({"data":serializer.data,"success":True})
        


class Policyview(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Documentation.objects.filter(file_type = "policy")
    serializer_class = DocumentationSerilizer


class Formview(generics.ListAPIView): 
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Documentation.objects.filter(file_type = "form")
    serializer_class = DocumentationSerilizer


class DocumentationUpdateView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Documentation.objects.get(pk=pk)
        except Documentation.DoesNotExist:
            raise Http404
    
    def get(self, request):
        document = self.get_objects()
        serializer = DocumentationSerilizer(document, many=True)
        return Response({"data":serializer.data, "success":True})

    def put(self, request, pk, format=None):
        hr = request.user.is_hr
        admin = request.user.is_superuser
        if hr or admin:
            policy = self.get_object(pk)
            serializer = DocumentationSerilizer(policy, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data, "success":True})
            return Response({"message":serializer.errors, "success":False})
        return Response({"message":"you do not have permission to perform this action.", "success":False})
      

    def delete(self, request, pk, format=None):
        hr = request.user.is_hr
        admin = request.user.is_superuser
        if hr  or admin:
            policy = self.get_object(pk)
            policy.delete()
            return Response({"success":True,"message":" successfully delete"})
        else:
            return Response({"message":"you do not have permission to perform this action.", "success":False})



