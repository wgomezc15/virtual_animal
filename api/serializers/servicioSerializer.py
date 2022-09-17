
from rest_framework import serializers

from api.models import servicio

class servicioSerializer(serializers.ModelSerializer):
  class Meta:
    model = servicio.Tabla_Servicio
    fields = ['id', 'name']