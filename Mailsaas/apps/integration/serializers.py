from rest_framework import serializers

from .models import SalesForceDetails


class SalesForceDetailSerializer(serializers.ModelSerializer):
   class Meta:
      model = SalesForceDetails
      fields = '__all__'
