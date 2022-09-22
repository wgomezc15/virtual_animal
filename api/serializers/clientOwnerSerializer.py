from rest_framework import serializers
from api.models import ClientOwner
from api.serializers.typeDocumentSerializer import TypeDocumentSerializer
class ClientOwnerSerializer(serializers.ModelSerializer):
    typedocument = TypeDocumentSerializer(many=False, read_only=True)
    class Meta:
        model = ClientOwner
        fields = ['id','name','lastname','email','document','typedocument','telephone','address','gender','isactive']