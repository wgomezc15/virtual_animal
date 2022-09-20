from rest_framework import serializers
from api.models import Enfermedad

class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model=tabla_Enfermedad
        fields='__all__'
    

