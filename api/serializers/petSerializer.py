from rest_framework import serializers
from api.models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

    def to_representation(self,instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'age': instance.age,
            'race': instance.race,
            'client_id': instance.client.id,
            'client_name': instance.client.name + ' ' + instance.client.lastname,
            'sex': instance.sex,
            'species': instance.species,
            'features': instance.features,
            'isactive': instance.isactive
        }