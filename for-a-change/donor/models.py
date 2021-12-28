# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from django.db import models
from fundraiser.models import Fundraiser
from django.conf import settings

# Create your models here.

class DonorTransaction(models.Model):
    fr = models.ForeignKey(Fundraiser, on_delete=models.CASCADE)
    amount = models.IntegerField()
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=10)
    contributeAnonimusly = models.BooleanField(default=False)
    billingCity = models.CharField(max_length=1000)

    country_code = models.CharField(max_length=1000)
    country_name = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    postal = models.CharField(max_length=1000)
    latitude = models.CharField(max_length=1000)
    longitude = models.CharField(max_length=1000)
    IPv4 = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.fr)