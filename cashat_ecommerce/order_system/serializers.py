from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import OrderItem,Order,Refund

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class RefundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Refund
        fields = "__all__"
