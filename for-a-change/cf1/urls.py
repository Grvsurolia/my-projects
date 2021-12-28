# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from fundraiser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('fundraiser.urls')),
    path('donor/',include('donor.urls')),
    path('adminapp/',include('adminapp.urls')),
  
]
