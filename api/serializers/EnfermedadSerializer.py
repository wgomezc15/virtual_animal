from rest_framework import serializers
from api.models.Enfermedad import tabla_Enfermedad
from dataclasses import fields

class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
         model=Enfermedad
        fields='__all__'
    

       def create(self, validated_data): 
        enfermedadInstace=Enfermedad.objects.create(**validated_data)
        return enfermedadInstace

    def to_representation(self, obj): 
        enfermedad=PENDIENTE.objects.get(id=obj.id)
        return{
            'id':enfermedad.id,
            'id_Enfermedad':enfermedad.id_enfermedad,
            'nombre':enfermedad.nombre,
            'fecha_creacion' : enfermedad.fecha_creacion,
            'descripcion' :enfermedad.descripcion
            
        }