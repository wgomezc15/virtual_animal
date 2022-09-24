from rest_framework import serializers
from api.models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id','name','age','race','sex','species','features','isactive','client']