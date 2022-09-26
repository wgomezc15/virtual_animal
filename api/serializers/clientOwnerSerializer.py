from rest_framework import serializers
from api.models import ClientOwner

class ClientOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientOwner
        fields = '__all__'

    def to_representation(self,instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'lastname': instance.lastname,
            'email': instance.email,
            'typedocument_id': instance.typedocument.id,
            'typedocument_code': instance.typedocument.code,
            'typedocument_name': instance.typedocument.name,
            'document': instance.document,
            'telephone': instance.telephone,
            'address': instance.address,
            'gender': instance.gender,
            'isactive': instance.isactive
        }