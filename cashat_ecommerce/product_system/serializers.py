from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Band,Categories,Cart,Colors,Sizes,Product,ProductImage,ProductFeedBack


class BandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Band
        fields = "__all__"

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = "__all__"

class ColorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colors
        fields = "__all__"

class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta :
        model = ProductImage
        fields = "__all__"

class ProductFeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeedBack
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"