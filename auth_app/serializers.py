from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from auth_app.models import User


class CompanyCreateSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    repeat_password = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)

    def validate(self, data):
        if not data['password'] == data['repeat_password']:
            raise serializers.ValidationError({"repeat_password": "Repeat password is not match to Password"})
        return data

    def create(self, validated_data):
        user = User.objects.create_company(name=validated_data.get("name"),
                                           phone_number=validated_data.get('phone_number'),
                                           password=validated_data.get('password'))

        return validated_data
