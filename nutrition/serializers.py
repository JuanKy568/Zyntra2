from rest_framework import serializers
from .models import PlanNutricional, RegistroComida


class PlanNutricionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanNutricional
        fields = '__all__'


class RegistroComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroComida
        fields = '__all__'