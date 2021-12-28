from rest_framework import serializers

from .models import EmailAccount


class EmailAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailAccount
        fields = '__all__'
