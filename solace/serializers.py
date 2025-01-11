from rest_framework import serializers
from .models import User, Prof
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'fullname']

    def create(self, validated_data):
        print("THE SERIALIZER PART")
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            fullname=validated_data['fullname']
        )

        return user
    

class ProfRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Prof
        fields = ['username', 'email', 'password', 'fullname']

    def create(self, validated_data):
        print("THE SERIALIZER PART")
        prof = Prof.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            fullname=validated_data['fullname']
        )

        return prof
    

