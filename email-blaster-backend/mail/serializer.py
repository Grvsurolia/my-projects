from rest_framework import serializers
from .models import *



class SmtpAccoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = SMTPEmailAccount
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = '__all__'

class MailSentStatusSerilizer(serializers.ModelSerializer):

    class Meta:
        model = MailSentStatus
        fields = '__all__'

class MailSentCelerySerilizer(serializers.ModelSerializer):

    class Meta:
        model = MailSentCelery
        fields = '__all__'