from rest_framework import serializers
from api.models import ClientOwner

class ClientOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientOwner
        fields = ['id','name','lastname','email','document','telephone','address','gender','isactive']