from rest_framework import serializers
from api.models import userClient

class UserClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = userClient
        fields = ['id','name','lastname','email','typeDocument','document','telephone','address','gender','isActive']