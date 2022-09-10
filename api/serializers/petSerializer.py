from dataclasses import fields
from api.models.pet import Pet
from rest_framework import serializers

#serializer es para transformar de JSON a una cuenta
class PetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pet
    fields = ['id', 'name','age','race','sex','species','features','isActive','userClient']


    def create(self, validated_data): 
        petInstace=Pet.objects.create(**validated_data)
        return petInstace

    def to_representation(self, obj): 
        pet=Pet.objects.get(id=obj.id)
        return{
            'id':pet.id,
            'name':pet.name,
            'age':pet.age,
            'race':pet.race,
            'sex':pet.sex,
            'species':pet.species,
            'features':pet.features,
            'isActive':pet.isActive,
            'userClient':pet.userClient
        }