from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from Notifications.models import Notification

from .serializers import NotificationSerializer


class ViewAllNotification(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NotificationSerializer

    def get_object(self,uid):
        try:
            return Notification.objects.filter(user__id=uid).order_by("-created_date")
        except Notification.DoesNotExist:
            raise Http404

    def get(self, request):
        notification = self.get_object(request.user.id)
        serializer = NotificationSerializer(notification, many=True)
        return Response({"data": serializer.data, "sucess": True})


class DeleteNotification(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NotificationSerializer

    def get_object(self,pk):
        try:
            return Notification.objects.get(pk=pk)
        except Notification.DoesNotExist:
            raise Http404

    def delete(self, request,pk):
        notification = self.get_object(pk)
        notification.delete()
        return Response({"message": "successfully delete notification", "sucess": True})

