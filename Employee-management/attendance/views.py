import datetime
import time
from datetime import date
from leave.models import LeaveApplication
from django.http import Http404, request
from django.shortcuts import render
from employees.models import User
from notification.models import Notification
from rest_framework import permissions, serializers, status, viewsets
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Attendance
from .serializers import AttendanceSerializer


class AttendanceAdd(CreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = (permissions.AllowAny,)

    def get_object(self, CardID):
        try:
            return User.objects.get(CardID=CardID, is_delete=False)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, CardID):

        user = self.get_object(CardID)
        request.data['employee'] = user.id
        emp = Attendance.objects.filter(employee=user.id).exists()
        Inmessage = "Time In " + user.first_name
        if emp:
            lastattendance = Attendance.objects.filter(
                employee=user.id).order_by('-id')[0]
            combine_time = datetime.datetime.combine(
                lastattendance.attendance_date, lastattendance.attendance_time)
            timedelta = datetime.timedelta(minutes=1)
            if (date.today() == lastattendance.attendance_date):
                time2 = (combine_time + timedelta).time()
                if (time2 <= datetime.datetime.now().time()):
                    if lastattendance.attendance_status == "OUTTIME":
                        time_break = lastattendance.break_time
                        request.data['attendance_status'] = 'INTIME'
                        current_break = datetime.datetime.now()-combine_time
                        total_break = time_break + current_break
                        request.data['break_time'] = total_break
                        request.data['working_time'] = lastattendance.working_time
                        one_hour = datetime.timedelta(hours=1)
                        if total_break >= one_hour:
                            message = " Your break time completed "
                            Notification.objects.create(
                                title="Attendance", message=message, user=user)
                        serializer = AttendanceSerializer(data=request.data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response({"out": 0, "in": 1, "message": Inmessage})
                        return Response({"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})

                    elif lastattendance.attendance_status == "INTIME":
                        time_work = lastattendance.working_time
                        current_break = datetime.datetime.now()-combine_time
                        total_work = time_work + current_break
                        request.data['break_time'] = lastattendance.break_time
                        request.data['working_time'] = total_work
                        request.data['attendance_status'] = 'OUTTIME'
                        outmessage = "Time Out "+user.first_name
                        serializer = AttendanceSerializer(data=request.data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response({"out": 1, "in": 0, "message": outmessage})
                        return Response({"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
                return Response({"out": 0, "in": 0, "message": "wait for 1 min"})

            elif (date.today() > lastattendance.attendance_date):
                request.data['attendance_status'] = 'INTIME'
                serializer = AttendanceSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"out": 0, "in": 1, "message": Inmessage})
                return Response({"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})

        else:
            request.data['attendance_status'] = 'INTIME'
            serializer = AttendanceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"out": 0, "in": 1, "message": Inmessage})
            return Response({"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})


class AttendanceView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AttendanceSerializer

    def get_object(self, id):
        try:
            return Attendance.objects.filter(employee=id)
        except Attendance.DoesNotExist:
            raise Http404

    def get(self, request, id):
        attendance = self.get_object(id)
        if id == request.user.id or request.user.is_hr  or request.user.is_ceo:
            serializer = AttendanceSerializer(attendance, many=True)
            return Response({"data": serializer.data, "success": True})
        else:
            return Response({"message": "you don't have permissions for view attendance", "success": False})


class  DateWiseAttendanceView(ListAPIView):               
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AttendanceSerializer

    def get(self, request, id):
        s_date = request.data['from_date']
        e_date = request.data['to_date']
        attendance = Attendance.objects.filter(employee=id,attendance_date__range=[s_date,e_date])
        if id == request.user.id or request.user.is_hr or request.user.is_ceo:
            serializer = AttendanceSerializer(attendance, many=True)
            return Response({"data": serializer.data, "success": True})
        else:
            return Response({"message": "you don't have permissions for view filter by date", "success": False})

