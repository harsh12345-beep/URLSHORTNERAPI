from dataclasses import field, fields
from re import L
from rest_framework import serializers
from .models import *
class UrlShortnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlShortner
        fields = '__all__'