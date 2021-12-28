from rest_framework import serializers

from order.models import Bill, BookingForm, Order, OrderProduct, SubBill


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

class GetOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
        depth = 1

class SubBillSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubBill
        fields = "__all__"
        depth = 2

class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = "__all__"
        depth = 1

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"
        depth = 1


class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingForm
        fields = "__all__"

class GetBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingForm
        fields = "__all__"
        depth = 2
