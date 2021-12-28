from rest_framework import serializers
from .models import AdminUser, HomePagesAdvertisement, DetailPagesAdvertisement


class AdminUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminUser
        fields = "__all__"
        depth = 1


class HomePagesAdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomePagesAdvertisement
        fields = '__all__'


class DetailPagesAdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailPagesAdvertisement
        fields = '__all__'
