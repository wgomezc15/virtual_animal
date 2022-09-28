from rest_framework import serializers
from api.models import PetVacinne

class PetVaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetVacinne
        fields = '__all__'

    def to_representation(self,instance):
        return{
            'id': instance.id,
            'pet_species': instance.pet.species,
            'pet_name': instance.pet.name,
            'vaccine_name': instance.vaccine.name,
            'fecha_vacunacion': instance.fecha,
            'pet_id': instance.pet.id,
            'vaccine_id': instance.vaccine.id
        }