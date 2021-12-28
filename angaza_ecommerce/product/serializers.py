# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""


from .models import  Slider, Specification, SubProduct
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Deal,Tag, Brand, Colour, WishList, SubCategories, Category, ProductDescription, ProductQuestion, Product, ProductSize, ProductImage, ProductDeal, ProductReview, Cart, Store, ProductCategory, ProductColour, Size


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    # sub_name = SubCategorySerializer()
    class Meta:
        model = Category
        fields = '__all__'


class DealsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deal
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id',"email","name","owner","mobile_number","location","thumbnail","status","website","store_portal_admin","describe"]

class SubProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProduct
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','title',"price","sale_price","description","price_type",
            "store","brand",'start_time','end_time','sku','thumbnail',
            "tags",'is_sale','inventory','depot','discount_percent',"product_option","visit_product"]
    




class ProductDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"
        depth = 2
        

    # def to_representation(self, instance):
    #     rep = super(ProductSerializer, self).to_representation(instance)
    #     rep['store'] = instance.store.name
    #     rep['brand'] = instance.brand.name
    #     return rep

# class ProductSubProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductSubProduct
#         fields = ['id','product',"sub_product"]
#         depth = 2

class ProductDealSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    
    class Meta:
        model = ProductDeal
        fields = ['id', 'product', "product_deals", "status"]
        depth = 2


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'product_image1','product_image2','product_image3','product_image4']


class ProductSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSize
        fields = ['id', 'product', 'product_size']

class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ['id', 'size_or_weight']


class ProductColourSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductColour
        fields = ["id", 'product', 'product_color']



class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = '__all__'



class CartCreateSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    class Meta:
        model = Cart
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'product_image1','product_image2','product_image3','product_image4']



class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReview
        fields = "__all__"



class WishListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = WishList
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super(WishListSerializer, self).to_representation(instance)
    #     rep['product'] = instance.product.title
    #     rep['user'] = instance.user.first_name + " "+ instance.user.last_name
    #     return rep


class WishListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = '__all__'



class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'



class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = '__all__'

  

class CategoriesSerializer(serializers.ModelSerializer):
    # sub_name = SubCategorySerializer()
    class Meta:
        model = Category
        fields = '__all__'

class GetCatgoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        depth = 2

class ProductCategorySerializer1(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = '__all__'
        depth = 3


class ProductDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDescription
        fields = ['id', 'product', "title", "description", "thumbnail"]

  


class ProductQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductQuestion
        fields = ['id', 'product', "user", "question", 'answer']

        depth = 2




class ColoursSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colour
        fields = ['id', 'name', 'code']


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id',"user", 'name']


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'



# class ProductSerializer(serializers.ModelSerializer):
#     # tags = serializers.StringRelatedField(many=True, read_only=True)
    
#     class Meta:
#         model = Product
#         fields = "__all__"
#         depth = 1