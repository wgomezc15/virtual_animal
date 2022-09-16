from rest_framework import serializers
from api.models.vaccines import AnimalVaccinations
from dataclasses import fields

class VaccinesSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'#incluye todos los campos id,idpet,name

    def create(self, validated_data):
        vaccineInstance=AnimalVaccinations.objects.create(**validated_data)
        return vaccineInstance 

    def to_representation(self, obj):
        vaccine=AnimalVaccinations.objects.get(id=obj.id)
        return {
            'id':vaccine.id,
            'name':vaccine.name,
            'idPet':vaccine.idPet
        }