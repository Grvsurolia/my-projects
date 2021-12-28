from rest_framework import serializers

from .models import UnsubcribeCsv, UnsubscribeEmail


class UnsubscribeEmailSerializers(serializers.ModelSerializer):

    class Meta:
        model = UnsubscribeEmail
        fields = '__all__'

class UnsubcribeCsvEmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = UnsubcribeCsv
        fields = '__all__'
