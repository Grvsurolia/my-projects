# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from django.urls import path, include
from .views import *
from fundraiser import views

urlpatterns = [
    
    path('register/', RegisterUsersView.as_view(), name="register"),
    path('verifyemail/', verifyEmailOtp.as_view(), name="verifyemail"),
    path('login/', LoginView.as_view(), name="login"),
    path('createfundraiser/', FundraiserCreate.as_view(), name="createfundraiser"),
    path('viewfundraiser/<str:slug>/', FundraiserView.as_view(), name="viewfundraiser"),
    path('comments/', DoComments.as_view(), name="DoComments"),
    path('browsefundraisers/', BrowseFundraisers.as_view(), name="BrowseFundraiser"),
    path('mybeneficiaries/', MyBeneficiaries.as_view(), name="mybeneficiaries"),
    path('update_beneficiary/', UpdateAInactiveBeneficiary.as_view(), name="update_beneficiary"),
]