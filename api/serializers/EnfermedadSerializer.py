from rest_framework import serializers
from api.models.Enfermedad import tabla_Enfermedad
from dataclasses import fields

class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model=tabla_Enfermedad
        fields='__all__'
    