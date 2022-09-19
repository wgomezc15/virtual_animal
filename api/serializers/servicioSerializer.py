
from rest_framework import serializers
from django.http import HttpResponse,JsonResponse
from api.models import servicio

class servicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = servicio.Tabla_Servicio
        fields = ['id', 'name']

    def ServicioCreateSerializer(self, validated_data): 
        userInstance=servicio.objects.create(**validated_data)
        return userInstance

    #def ServicioTo_representation(self, obj): 
     #   typeDocument = servicio.objects.get(id=obj.id)
      #  return {
       #   "id": servicio.id,
        #  "name": servicio.name
        #}

    

    