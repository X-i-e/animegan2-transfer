from rest_framework import serializers
from .models import RawPic, ProcessedPic


class RawSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawPic
        fields = '__all__'

class ProSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedPic
        fields = '__all__'