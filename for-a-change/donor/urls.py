# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from django.urls import path, include
from .views import *
from fundraiser import views

urlpatterns = [
    
    path('transaction/', DonorTransactionView.as_view(), name="donottransaction"),
    
]