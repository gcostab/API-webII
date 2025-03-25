from django.urls import path, include
from .models import Usuario
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'