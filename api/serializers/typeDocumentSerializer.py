from rest_framework import serializers
from api.models import TypeDocument

class TypeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeDocument
        fields=['id','code','name']
