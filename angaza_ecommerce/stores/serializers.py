from order.models import Order, OrderProduct
from product.models import ProductCategory, Store
from rest_framework import serializers

from .models import ProductSpecification, StoreOwner


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ['id',"email","name","owner","mobile_number","location","thumbnail","status","website","describe"]
        depth = 2


class StoreOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreOwner
        fields = "__all__"


class GetProductCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = "__all__"
        depth=1

class ProductSpecificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSpecification
        fields = "__all__"


class GetOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

class OrderProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderProduct
        fields = "__all__"
        depth = 2
