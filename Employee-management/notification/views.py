from django.http import Http404, request
from employees.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Notification
from .serializers import NotificationSerializers


class ViewLeaveNotification(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer = NotificationSerializers

    def get_object(self, pk):

        try:
            return Notification.objects.get(pk=pk,title='Leave',read_notification=False)
        except Notification.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        if (request.user.is_hr or request.user.is_supervisor or request.user.is_ceo or request.user.is_cto or request.user.is_teamlead or request.user.is_second_teamlead):
            notifications = self.get_object(pk)
            serializer = NotificationSerializers(notifications)
            notice=Notification.objects.get(pk=pk)
            notice.read_notification=True
            notice.save()
            return Response(serializer.data)
        return Response({"message":"You do not have permission to perform this action.", "success":False})

class ViewAttendanceNotification(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer = NotificationSerializers

    def get_object(self, pk):

        try:
            return Notification.objects.get(pk=pk,title='Attendance',read_notification=False)
        except Notification.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        
        notifications = self.get_object(pk)
        if request.user ==notifications.user:
            serializer = NotificationSerializers(notifications)
            notice=Notification.objects.get(pk=pk)
            notice.read_notification=True
            notice.save()
            return Response(serializer.data)
        return Response({"message":"You do not have permission to perform this action.", "success":False})
   
        
    
