from rest_framework import serializers
from api.models import client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = ['id','name','lastname','email','typedocument','document','telephone','address','gender','isactive']