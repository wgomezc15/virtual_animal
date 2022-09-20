from rest_framework import serializers
from api.models import tabla_Enfermedad


class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model=tabla_Enfermedad
        fields='__all__'
    
