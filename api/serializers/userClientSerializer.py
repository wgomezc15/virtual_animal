from rest_framework import serializers
from api.models import UserClient
from api.serializers.typeDocumentSerializer import TypeDocumentSerializer
from django.http import HttpResponse, JsonResponse

from virtual_animal.api.models import typeDocument
from virtual_animal.api.models.userClient import UserClient_Tabla

class userClient(serializers.Modelserializer):
    class Meta:
        model = UserClient_Tabla
        fields = ['id','name','lastname','typeDocument','document','isActive']

    def userClientSerializer(self, validated_data):
        userInstance =  userClient.objects.create(**validated_data)
        return userInstance

    def userClient_To_representation(self, obj):
        typeDocument = userClient.objects.get(id=obj.id)
        return {
            'id':userClient.id,
            'name':userClient.id,
            'lastname':userClient.id,
            'typeDocument':userClient.id,
            'document':userClient.id,
            'isActive':userClient.id
        }