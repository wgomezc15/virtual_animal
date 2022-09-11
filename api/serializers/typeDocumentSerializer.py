from api.models.typeDocument import TypeDocument
from rest_framework import serializers

class TypeDocumentSerializer(serializers.ModelSerializer):
  class Meta:
    model = TypeDocument
    fields = ['id', 'code', 'name']

    def create(self, validated_data): 
        typeDocumentInstace=TypeDocument.objects.create(**validated_data)
        return typeDocumentInstace

    def to_representation(self, obj): 
        typeDocument=TypeDocument.objects.get(id=obj.id)
        return {
                'id':typeDocument.id,
                'code':typeDocument.code,
                'name':typeDocument.name
                }