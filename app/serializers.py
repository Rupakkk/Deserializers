from .models import Student
from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)