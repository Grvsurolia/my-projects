from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, IntegerField, RelatedField
from CustomUserModel.models import CustomUser
from .models import Plant, PlantType,WishList


class PlantTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlantType
        fields = '__all__'


class plantPostSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id','plant_name','plant_type','other_p_type','description','quantity','city','owner','img1','img2','img3','img4','status','datetime']
    
  
# class ProductUserNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id','username']
  
class ProductSerializer(serializers.ModelSerializer):
    plant_type = serializers.StringRelatedField(many=True, read_only=True)
    datetime = serializers.DateField(format="%m/%d/%Y", required=False, read_only=True)

    class Meta:
        model = Plant
        # fields = "__all__"
        fields = ['id','plant_name','plant_type','other_p_type','description','quantity','city','owner','img1','img2','img3','img4','status','datetime','owner_name']
        
        # fields.__add__('difference')

    

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id','plant_name','plant_type','other_p_type','description','quantity','img1','img2','img3','img4','status']
        
        
class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','last_name','phone_number','address']
        
        
class wishListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WishList
        fields = '__all__'