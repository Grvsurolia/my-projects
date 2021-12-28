from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, serializers, status
from .serializers import *
from django.conf import settings
from django.core.mail import send_mail
import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
import json
from employees.serializers import RegisterSerializer

class CreateTeamView(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self,request,*args,**kwargs):
        if request.data!={}:
            if request.user.is_superuser or request.user.is_teamlead or request.user.is_hr or request.user.is_ceo:
                request.data["user"] = request.user.id
                serializer = TeamSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"data":serializer.data,"success":True})
                return Response({"message":serializer.error,"success":False})
            return Response({"message":"you don't have permission to create team","success":False})
        return Response({"message":"please give team name","success":False})
    

    def get(self,request,*args,**kwargs):
        team = Team.objects.filter(user=request.user.id)
        serializer = TeamSerializer(team, many=True)
        return Response({"data":serializer.data,"success":True})

class UpdateDeleteTeams(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TeamSerializer
        
    def get(self,request,pk):
        queryset = Team.objects.get(id = pk)
        user = request.user.id
        if queryset.user.id == user:
            team = TeamSerializer(queryset)
            return Response({"data":team.data,"sucess":True})
        return Response({"message":"you are not authenticate user","success":False})

    def put(self, request, pk, format=None):
        queryset = Team.objects.get(id = pk)

        request.data['user'] = request.user.id
        serializer = TeamSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Team Updated successfully","success":True})
        return Response({"message":serializer.errors,"success":False})


    def delete(self, request, pk, format=None):
        queryset = Team.objects.get(id = pk)
        request.data['user'] = request.user.id
        queryset.delete()
        return Response({"messsage":"Teams deleted successfully",'success':True})

class SendTeamInvitionsView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = InvitationSerializer
    queryset = Invitation.objects.all()

    def post(self,request,*args,**Kwargs):
        self_email = User.objects.get(email=request.user.email).email
        if self_email != request.data['email']:
            request.data['user']=request.user.id
            save_count = Invitation.objects.filter(email=request.data['email'])
            if len(save_count) > 0:
                serializer = InvitationSerializer(data=request.data)
                if serializer.is_valid():
                    user_email = serializer.data['email']
                    current_site = settings.SITE_URL
                    team = Team.objects.get(id=request.data["team"])
                    user_id = User.objects.get(id=request.user.id)
                    to_pass_with_url = {"TeamId": team.id, "user": user_id.id}
                    base64_message = base64.urlsafe_b64encode(json.dumps(to_pass_with_url).encode()).decode()
                    url =  "<a href='" + (current_site + "/teams/register/") + base64_message  + "'>JoinTeam</a>"
                    email_body = "Click the link below for join Team \n" + url
                    send_mail_with_smtp(user_email=user_email,body= email_body)
                    return Response({"data":serializer.data,"success":True})
                return Response({"message":serializers.error,"success":False})      

            serializer = InvitationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user_email = serializer.data['email']
                current_site =  settings.SITE_URL
                team_name = Team.objects.get(id=request.data["team"])
                user_id = User.objects.get(id=request.user.id)
                to_pass_with_url = {"TeamId": team.id, "user": user_id.id}
                base64_message = base64.urlsafe_b64encode(json.dumps(to_pass_with_url).encode()).decode()
                url =  "<a href='" + (current_site + "/teams/register/") + base64_message  + "'>JoinTeam</a>"
                email_body = "Click the link below for join Team \n" + url
                send_mail_with_smtp(user_email=user_email,body= email_body)
                return Response({"data":serializer.data,"success":True})
            return Response({"message":serializers.error,"success":False})
        return Response({"messsage":"you can't send email self","success":False})

    

class RegisterTeamMember(APIView):

    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

    def post(self,request,*args,**kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request)
            full_url = settings.SITE_URL + request.get_full_path()
            base64_message = full_url.split('/')[-1]
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            team_id = message_bytes.decode('ascii')
            team_id = eval(team_id)
            user = User.objects.get(email=serializer.data['email'])
            teams = Team.objects.get(id=team_id['TeamId'],user = team_id['user'])
            member = Member(team =teams)
            member.save()
            member.member.add(user)
            return Response({"data":serializer.data,"success":True})
        return Response({"message":serializer.errors,"success":False})
       
def send_mail_with_smtp(user_email,body):
    try:
        host = settings.EMAIL_HOST
        port = settings.EMAIL_PORT
        fromaddr = settings.EMAIL_HOST_USER
        password = settings.EMAIL_HOST_PASSWORD
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = user_email
        msg['Subject'] = 'Click the link below for join elmail'
        body = body
        msg.attach(MIMEText(body, 'html'))
        if ('@gmail.com' in settings.EMAIL_HOST_USER):
            server_ssl = smtplib.SMTP(host,port)
        else:
            server_ssl = smtplib.SMTP(host)
        server_ssl.ehlo()
        server_ssl.starttls()
        server_ssl.login(fromaddr, password)
        text = msg.as_string()
        server_ssl.sendmail(fromaddr, msg['To'], text)
        server_ssl.close()
    except Exception as _error:
        print(_error)
        raise Exception('Error in sending mail >> {}'.format(_error))