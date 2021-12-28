
import datetime
import time
from django.core.mail import send_mail
from django.http import Http404, HttpResponse, request
from django.template.loader import render_to_string
from django.utils.html import format_html, html
from django.views.decorators.csrf import csrf_exempt
from employees import serializers
from employees.models import User
from employees.serializers import UserUpdateSerializer
from notification.models import Notification
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date,timedelta
from .models import LeaveApplication,EmployeeLeave,EmployeeCancelLeave
from .serializers import LeaveApplicationSerializer,EmployeeLeaveSerializer,EmployeeCancelLeaveSerializer


class Leaveapplication(generics.CreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LeaveApplicationSerializer

    def post(self,request,*args, **kwargs):
        now=datetime.datetime.now()
        emails=[]
        hr_ceo=[]
        hr_email =[]
        request.data['employee'] = request.user.id
        try:
            ceo=User.objects.get(is_ceo=True)
            emails.append(ceo.email)
        except:
            print("not ceo")

        try:
            # hr= User.objects.get(is_hr=True)
            hr_ceo.append(request.user.hr_common_email)
            hr_email.append(request.user.hr_common_email)
        except:
            print("not HR")

        try:
            cto=User.objects.get(is_cto=True,is_delete=False)
            emails.append(cto.email)
        except:
            print("not cto ")
            
        if User.objects.filter(is_teamlead=True,team=request.user.team,is_delete=False).exists():
            teamleads= User.objects.filter(is_teamlead=True,team=request.user.team,is_delete=False)
            for teamlead in teamleads:
                emails.append(teamlead.email)
        if User.objects.filter(is_supervisor=True,team=request.user.team,is_delete=False).exists():    
            supervisors= User.objects.filter(is_supervisor=True,team=request.user.team,is_delete=False)
            for supervisor in supervisors:
                emails.append(supervisor.email)

        if request.data['leave_type'] =="half-day":
            request.data['end_date']=request.data['start_date']
            if request.data['to_time']=="" and request.data['from_time']=="" and request.data['to_time']=="null" and request.data['from_time']=="null":
                return Response({"message":"Please Enter to and from time ", "success":False}) 
            if request.data['to_time']=="" and request.data['to_time']=="null":
                return Response({"message":"Please Enter to time ", "success":False})
            if request.data['from_time']=="" and request.data['from_time']=="null":
                return Response({"message":"Please Enter from time ", "success":False})
            else:
                serializer = LeaveApplicationSerializer(data = request.data)
                if serializer.is_valid():
                    half_day = serializer.save()
                    half_day.to_time = request.data['to_time']
                    half_day.from_time = request.data['from_time']
                    half_day.save()
                    start_date=request.data['start_date']
                    name=request.user.first_name+" "+request.user.last_name
                    message=f"{name} apply Half day leave {start_date}"
                    Notification.objects.create(title="Leave", message=message, user=request.user)
                    params ={"id":serializer.data['id'],"name":name,"start_date":start_date,'reason':request.data['reason']}
                    email_message = render_to_string('emails.html',params)
                    # send_mail(message,"email_message",request.user.email,emails,html_message=email_message)
                    send_mail(message,"email_message",'developer@externlabs.com',['divyakhandelwal@externlabs.com','ashutoshsharma@externlabs.com'],html_message=email_message)
                    params_email ={"id":serializer.data['id'],"name":name,"start_date":start_date,"hr_email":request.user.hr_common_email,'reason':request.data['reason']}
                    hr_message = render_to_string('hr_ceo.html',params)
                    # send_mail(message,"email_message",request.user.email,hr_ceo,html_message=hr_message)
                    send_mail(message,"email_message",'developer@externlabs.com',['divyakhandelwal@externlabs.com','ashutoshsharma@externlabs.com'],html_message=hr_message)

                    return Response({"data":serializer.data, "status":status.HTTP_201_CREATED,"success":True})
                return Response({"error":serializer.errors, "status":status.HTTP_400_BAD_REQUEST,"success":False})
                
        else:
            start_date=request.data['start_date']
            end_date=request.data['end_date']
            
            serializer = LeaveApplicationSerializer(data = request.data)
            if serializer.is_valid():
                
                leave = serializer.save()
                days = leave.end_date - leave.start_date
                
                leave.no_of_days = days.days
                leave.save()
            
            name=request.user.first_name+" "+ request.user.last_name
            message=f"{name} apply leave {start_date} to {end_date}"
            Notification.objects.create(title="Leave", message=message, user=request.user)
            params ={"id":serializer.data['id'],"name":name,"start_date":start_date,"end_date":end_date,'reason':request.data['reason']}
            email_message = render_to_string('emails.html',params)
            # send_mail(message,"email_message",request.user.email,emails,html_message=email_message)
            send_mail(message,"email_message",'developer@externlabs.com',['divyakhandelwal@externlabs.com','ashutoshsharma@externlabs.com'],html_message=email_message)

            params ={"id":serializer.data['id'],"name":name,"start_date":start_date,"end_date":end_date,"hr_email":request.user.hr_common_email,'reason':request.data['reason'],"user_email":request.user.email}
            hr_message = render_to_string('hr_ceo.html',params)
            # send_mail(message,"email_message",request.user.email,hr_ceo,html_message=hr_message)
            send_mail(message,"email_message",'developer@externlabs.com',['divyakhandelwal@externlabs.com','ashutoshsharma@externlabs.com'],html_message=hr_message)


            return Response({"data":serializer.data, "status":status.HTTP_201_CREATED,"success":True})
        return Response({"error":serializer.errors, "status":status.HTTP_400_BAD_REQUEST,"success":False})
   
   
class LeaveReply(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request):    
        actions=request.POST.get('action')
        leave_id = request.POST.get('leaveid')
       

        user_email = request.POST.get('user_email')
     

        hr_email = request.POST.get('hr_email')

        leaves = LeaveApplication.objects.get(pk=leave_id)

        hr_users=User.objects.get(email=hr_email)
        msg_reject= "Sorry Your Leave Rejected Some reasons please contact your hr "
        msg_approved = "Your leave Approved "
        if leaves.onetime_hr_status==True:
            send_mail("Already Reply Leave ","Your are already Reply this Leave Application","developer@externlabs.com",["ashutoshsharma@externlabs.com"])
                # send_mail("Leave Already CEO","Your are already Reply this Leave Application",hr_users.email,hr_users.email)       
        elif leaves.onetime_hr_status==False:
            if actions=="Accept":
                leaves.onetime_hr_status = True
                leaves.overall_status="approved"
                leaves.save()
                # send_mail("Leave approved HR",msg_approved,hr_users.email,[user_email])
                send_mail("Leave approved HR",msg_approved,"developer@externlabs.com",["ashutoshsharma@externlabs.com"])
                if(leaves.start_date == leaves.end_date):
                    EmployeeLeave.objects.create(employee_id=leaves.employee,leaves_apply=leaves,leave_date=leaves.start_date,leave_type=leaves.leave_type,status=leaves.overall_status)
        
                else:
                    numberofday = leaves.end_date - leaves.start_date
                    print("numberofday accept",numberofday.days)
                    for dates in range(0,numberofday.days):
                        if dates == 0:
                            s_date = leaves.start_date
                            EmployeeLeave.objects.create(employee_id=leaves.employee,leaves_apply=leaves,leave_date=s_date,leave_type=leaves.leave_type,status=leaves.overall_status)
                        else:
                            s_date = leaves.start_date
                            s_date += timedelta(days=dates)
                            if (leaves.end_date >= s_date):
                                EmployeeLeave.objects.create(employee_id=leaves.employee,leaves_apply=leaves,leave_date=s_date,leave_type=leaves.leave_type,status=leaves.overall_status)

            elif actions=="Reject":
                leaves.onetime_hr_status = True
                leaves.overall_status="reject"
                leaves.save()
                # send_mail("Leave reject HR",msg_reject,hr_users.email,[user_email])
                send_mail("Leave reject HR",msg_reject,"developer@externlabs.com",["ashutoshsharma@externlabs.com"]) 
                if(leaves.start_date == leaves.end_date):
                    EmployeeCancelLeave.objects.create(employee_id=leaves.employee,leaves_apply=leaves,leave_date=leaves.start_date,leave_type=leaves.leave_type,status=leaves.overall_status)
        
                else:
                    numberofday = leaves.end_date - leaves.start_date
                    print("numberofday reject",numberofday.days)
                    for dates in range(0,numberofday.days):
                        if dates == 0:
                            s_date = leaves.start_date
                            EmployeeCancelLeave.objects.create(employee_id=leaves.employee,leaves_apply=leaves,leave_date=s_date,leave_type=leaves.leave_type,status=leaves.overall_status)
                        else:
                            s_date = leaves.start_date
                            s_date += timedelta(days=dates)
                            if (leaves.end_date >= s_date):
                                EmployeeCancelLeave.objects.create(employee_id=leaves.employee,leaves_apply=leaves,leave_date=s_date,leave_type=leaves.leave_type,status=leaves.overall_status)

        return HttpResponse("Successfully")



class LeaveApplicationView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LeaveApplicationSerializer

    def get_object(self, id):

        try:
            return LeaveApplication.objects.filter(employee_id__id=id)
        except LeaveApplication.DoesNotExist:
            raise Http404

    def get(self,request,id):

        leave = self.get_object(id)
        
        if request.user.is_hr  or request.user.is_superuser :
            serializer = LeaveApplicationSerializer(leave, many=True)
            return Response({"data":serializer.data,"success":True})
        elif(request.user.id == id):
            
            serializer = LeaveApplicationSerializer(leave, many=True)
            return Response({"data":serializer.data,"success":True})
        return Response({"message":"You do not have permission to perform this action.", "success":False})


class ApplyLeaveUpdateView(generics.RetrieveUpdateAPIView):

    serializer_class = LeaveApplicationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):

        try:
            return LeaveApplication.objects.get(pk=pk)
        except LeaveApplication.DoesNotExist:
            raise Http404

    def get(self, request,pk):

        leave = self.get_object(pk)

        if request.user.is_ceo or request.user.is_hr  or request.user.is_superuser:
            serializer = LeaveApplicationSerializer(leave)
            return Response({"data":serializer.data,"success":True})
        return Response({"message":"You do not have permission to perform this action.", "success":False})
        
    def put(self, request, pk, format=None):

        leave = self.get_object(pk)

        if request.user.is_hr  or request.user.is_superuser:
            if request.data['leave_type'] =="half-day":
                request.data['end_date']=request.data['start_date']

                if request.data['to_time']=="" and request.data['from_time']=="" and request.data['to_time']=="null" and request.data['from_time']=="null":
                    return Response({"message":"Please Enter to and from time ", "success":False}) 
                if request.data['to_time']=="" and request.data['to_time']=="null":
                    return Response({"message":"Please Enter to time ", "success":False})
                if request.data['from_time']=="" and request.data['from_time']=="null":
                    return Response({"message":"Please Enter from time ", "success":False})
                else:
                    serializer = LeaveApplicationSerializer(leave, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"data":serializer.data,"success":True})
                    return Response({"error":serializer.errors, "status":status.HTTP_400_BAD_REQUEST,"success":False})

            else:
                serializer = LeaveApplicationSerializer(leave, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"data":serializer.data,"success":True})
                return Response({"error":serializer.errors, "status":status.HTTP_400_BAD_REQUEST,"success":False})
            
        return Response({"message":"You do not have permission to perform this action.", "success":False})


class ViewAllCancelLeave(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeCancelLeaveSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, eid):

        try:
            return EmployeeCancelLeave.objects.filter(employee_id__id=eid,status="reject")
        except EmployeeCancelLeave.DoesNotExist:
            raise Http404


    def get(self,request,eid):
        leave = self.get_object(eid)
        if request.user.is_hr  or request.user.is_ceo or request.user.id==leave.employee.id :
            serializer = EmployeeCancelLeaveSerializer(leave, many=True)
            return Response({"data":serializer.data,"success":True})
        return Response({"message":"You do not have permission to perform this action.", "success":False})



class UpdateCancelLeave(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeCancelLeaveSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return EmployeeCancelLeave.objects.get(pk=pk,status="reject")
        except EmployeeCancelLeave.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        leave = self.get_object(pk)
        if request.user.is_hr  or request.user.is_ceo or request.user.id==leave.employee.id :
            serializer = EmployeeCancelLeaveSerializer(leave)
            return Response({"data":serializer.data,"success":True})
        return Response({"message":"You do not have permission to perform this action.", "success":False})
    

    def put(self, request, pk):
        leave = self.get_object(pk)
        if request.user.is_hr or request.user.is_ceo:
            serializer = EmployeeCancelLeaveSerializer(leave, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"success":True})
            return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST, "success":False})
        return Response({"message":"you don't have permissions for Update Profile", "success":False})


class ViewAllLeave(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeLeaveSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, eid):
        try:
            return EmployeeLeave.objects.filter(employee_id__id=eid)
        except EmployeeLeave.DoesNotExist:
            raise Http404


    def get(self,request,eid):
        leave = self.get_object(eid)
        if request.user.is_hr  or request.user.is_ceo or request.user.id==leave.employee.id :
            serializer = EmployeeLeaveSerializer(leave, many=True)
            return Response({"data":serializer.data,"success":True})
        return Response({"message":"You do not have permission to perform this action.", "success":False})


class UpdateLeave(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeLeaveSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return EmployeeLeave.objects.get(pk=pk)
        except EmployeeLeave.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        leave = self.get_object(pk)
        if request.user.is_hr  or request.user.is_ceo or request.user.id==leave.employee.id :
            serializer = EmployeeLeaveSerializer(leave)
            return Response({"data":serializer.data,"success":True})
        return Response({"message":"You do not have permission to perform this action.", "success":False})
    

    def put(self, request, pk):
        leave = self.get_object(pk)
        if request.user.is_hr or request.user.is_ceo:
            serializer = EmployeeLeaveSerializer(leave, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"success":True})
            return Response({"error":serializer.errors, status:status.HTTP_400_BAD_REQUEST, "success":False})
        return Response({"message":"you don't have permissions for Update Profile", "success":False})