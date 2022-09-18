from rest_framework import serializers
from api.models.vaccines import Tabla_Vacunas
from dataclasses import fields

class VaccinesSerializer(serializers.ModelSerializer):
    class Meta: #class meta adjunta metadatos a un conjunto de campos que componen el modelo
        model=Tabla_Vacunas 
        fields='__all__'#incluye todos los campos id,name

    