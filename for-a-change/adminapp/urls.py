# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from django.urls import path, include
from .views import *
from fundraiser import views

urlpatterns = [
    path('browseallfundraisers/', GetAllBeneficiaries.as_view(), name="BrowseAllFundraiser"),
    path('delete_a_fundraiser/<pk>/', DeleteABeneficiaries.as_view(), name="delete_a_fundraisers"),
    path('delete_multi_fundraiser/', DeleteMultipleBeneficiaries.as_view(), name="delete_multi_fundraiser"),
    path('update_a_fundraiser/<pk>/', UpdateABeneficiarie.as_view(), name="update_a_fundraiser"),
    path('browseallcampaigners/', GetAllCampaigners.as_view(), name="GetAllCampaigners"),
    path('delete_a_campainer/<pk>/', DeleteACampaigner.as_view(), name="delete_a_campainer"),
    path('delete_multi_campainers/', DeleteMultipleCampaigners.as_view(), name="delete_multi_campainers"),
    path('update_a_campainers/<pk>/', UpdateACampaigners.as_view(), name="update_a_campainers"),
    path('get_all_trans/', GetAllTransactions.as_view(), name="get_all_trans"),
    path('delete_a_trans/<pk>', DeleteATransaction.as_view(), name="delete_a_trans"),
    path('delete_multi_trans/', DeleteMultipleTransactions.as_view(), name="delete_multi_trans"),
    path('update_a_trans/<pk>/', UpdateATransaction.as_view(), name="update_a_trans"),
    path('create_campaigner/', CreateCampaigner.as_view(), name="create_campaigner"),
    path('get_update_request/', GetAllActiveBeneficiaryRequest.as_view(), name="get_update_request"),
 ]