from rest_framework import serializers
from wagtail.core import fields

from calendar_system import models
from .models import Team,Member,Invitation


class TeamSerializer(serializers.ModelSerializer):

    class meta:
        model = Team
        fields = "__all__"

class InvitationSerializer(serializers.ModelSerializer):

    class meta:
        model = Invitation
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):

    class meta:
        model = Member
        fields = "__all__"