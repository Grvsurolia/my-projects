from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Bill,Payment,CouponApplied

class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


class CouponAppliedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CouponApplied
        fields = "__all__"
