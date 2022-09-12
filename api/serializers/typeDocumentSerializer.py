from rest_framework import serializers
from django.http import HttpResponse,JsonResponse
from api.models import TypeDocument

class TypeDocumentSerializer(serializers.ModelSerializer):
    
    #typeDocument = TypeDocumentSerializer()

    class Meta:
        model=TypeDocument
        fields=['id','code','name']
    
    def create(self, validated_data): 
        userInstance=TypeDocument.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj): 
        typeDocument = TypeDocument.objects.get(id=obj.id)
        return {
          "id": typeDocument.id,
          "code": typeDocument.code,
          "name": typeDocument.name
        }