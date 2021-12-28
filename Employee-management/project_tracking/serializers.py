from .models import Project,OccupiedEmp,BenchList,POCList,PocWorkEmployees
from rest_framework import serializers


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__" 


class  OccupiedEmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = OccupiedEmp
        fields = "__all__"


class  BenchEmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = BenchList
        fields = "__all__"

class  PocProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = POCList
        fields = "__all__"

class  PocProjectWorkerSerializers(serializers.ModelSerializer):
    class Meta:
        model = PocWorkEmployees
        fields = "__all__"

