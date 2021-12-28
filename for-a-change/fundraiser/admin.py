# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from django.contrib import admin
from .models import CustomUser, Fundraiser, frComments
from donor.models import DonorTransaction
from adminapp.models import RequestedUpdateFundraiser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Fundraiser)
admin.site.register(frComments)
admin.site.register(DonorTransaction)
admin.site.register(RequestedUpdateFundraiser)