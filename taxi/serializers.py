from rest_framework import serializers
from .models import FakeTaxi

class FakeTaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeTaxi
        fields = '__all__'
