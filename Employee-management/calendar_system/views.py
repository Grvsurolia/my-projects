from django.shortcuts import render
from rest_framework import generics,permissions,serializers, status
from rest_framework.views import APIView
from employees.models import User
from leave.models import EmployeeLeave
from attendance.models import Attendance
from news.models import UpcomingHolidayPage
from .models import EmployeeCalendar
from .serializers import EmployeeCalendarSerializers
from rest_framework.response import Response
from datetime import date
import calendar

# Create your views here.



class EmployeeCalendarView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EmployeeCalendarSerializers

    def get_object(self,eid):
        try:
            return EmployeeCalendar.objects.filter(employee__id=eid)
        except EmployeeCalendar.DoesNotExist:
            raise Http404

    def get(self,request,eid):
        calendar = self.get_object(eid)
        if request.user.is_hr or request.user.id == eid or request.user.is_ceo :
            serializer = EmployeeCalendarSerializers(calendar, many=True)
            return Response({"data": serializer.data, "success": True})
        return Response({"message": "you don't have permissions for view Bankdetails", "success": False})
        


class EmployeeCalendarUpdate(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EmployeeCalendarSerializers

    def get_object(self,pk):
        try:
            return EmployeeCalendar.objects.get(pk=pk)
        except EmployeeCalendar.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        calendar = self.get_object(pk)
        if request.user.is_hr or request.user.id == calendar.employee.id or request.user.is_ceo :
            serializer = EmployeeCalendarSerializers(calendar)
            return Response({"data": serializer.data, "success": True})
        return Response({"message": "you don't have permissions for view Bankdetails", "success": False})

    def put(self,request,pk):
        calendar = self.get_object(pk)
        if request.user.is_hr or request.user.is_ceo :
            serializer = EmployeeCalendarSerializers(calendar, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST,"success":False})    
        return Response({"message": "you don't have permissions for view Bankdetails", "success": False})
