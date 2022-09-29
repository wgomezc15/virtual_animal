from rest_framework import serializers
from api.models import ConsultaMedica

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = '__all__'

    def to_representation(self,instance):
        return{
            'id': instance.id,
            'motivo': instance.motivo,
            'fecha': instance.fecha,
            'peso': instance.peso,
            'ritmocardiaco': instance.ritmocardiaco,
            'pet_species': instance.pet.species,
            'pet_name': instance.pet.name,
            'pet_id': instance.pet.id
        }
