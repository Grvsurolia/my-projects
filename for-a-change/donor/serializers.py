# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from rest_framework import serializers
from .models import DonorTransaction

class DonorTransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DonorTransaction
        fields = '__all__'