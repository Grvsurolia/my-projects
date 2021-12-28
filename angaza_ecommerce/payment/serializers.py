from django.db import models
from rest_framework import serializers
from .models import MPayment


class MPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MPayment
        fields = "__all__"