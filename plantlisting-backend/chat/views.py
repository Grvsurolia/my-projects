from weakref import ProxyTypes
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from .models import ChatUser,Message
from CustomUserModel.models import CustomUser

# @login_required(login_url="/chat/login/")
def index(request):

    my_users = CustomUser.objects.all()
    

    return render(request,'index.html',{'my_users':my_users})

# @login_required(login_url="/chat/login/")
def room(request,user_name):

    my_users = CustomUser.objects.all()
    print(request.user.username)
    my_messages = ChatUser.objects.get_or_new(request.user.username,user_name)
    print(my_messages,"my_messages")
    
    return render(request,'room2.html',{
        'user_name':user_name,
        'my_users':my_users,
        'my_messages':my_messages
    })
