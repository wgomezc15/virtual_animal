
from urllib import request
from django.urls import is_valid_path
from rest_framework import generics
from rest_framework import status,views
from django.http import JsonResponse
from rest_framework.response import Response

from api.models.servicio import Tabla_Servicio
from api.serializers.servicioSerializer import servicioSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


#Función para obtener información de todos los registros
@api_view(['GET'])
def servicio_getall_view(request, pk=None):
    if request.method == 'GET':
            servicio_serializer = Tabla_Servicio.objects.all()
            servicio_serializer = servicioSerializer(servicio_serializer, many=True)
            return Response(servicio_serializer.data)

#Función para obtener información de un registro detallado
@api_view(['GET'])
def servicio_detail_view(requests, pk=None):

    if requests.method == 'GET':
        servicio2 =  Tabla_Servicio.objects.filter(id=pk).first()
        servicio_serializer = servicioSerializer(servicio2)
        return Response(servicio_serializer.data)
    
#Función para obtener información de un registro detallado y permite modificarlo
@api_view(['GET', 'PUT'])
def servicio_update_view(requests, pk=None):

    if requests.method == 'GET':
        servicio2 =  Tabla_Servicio.objects.filter(id=pk).first()
        servicio_serializer = servicioSerializer(servicio2)
        return Response(servicio_serializer.data)
    
    elif requests.method == 'PUT':    
            servicio2 =  Tabla_Servicio.objects.filter(id=pk).first()
            servicio_serializer = servicioSerializer(servicio2,data = requests.data)
            if servicio_serializer.is_valid():
                servicio_serializer.save()
                return Response(servicio_serializer.data)
            return Response(servicio_serializer.error)

#Función para obtener información de un registro detallado y eliminarlo
@api_view(['GET','DELETE'])
def servicio_delete_view(requests, pk=None):

    if requests.method == 'GET':
        servicio2 =  Tabla_Servicio.objects.filter(id=pk).first()
        servicio_serializer = servicioSerializer(servicio2)
        return Response(servicio_serializer.data)
    
    elif requests.method == 'DELETE':    
            servicio2 =  Tabla_Servicio.objects.filter(id=pk).first()
            servicio2.delete()
            return Response('Eliminado')

#Función para obtener información de toda la tabla y permite adicionar un nuevo registro
@api_view(['GET','POST'])
def servicio_create_view(request, pk=None):
    if request.method == 'GET':
            servicio_serializer = Tabla_Servicio.objects.all()
            servicio_serializer = servicioSerializer(servicio_serializer, many=True)
            return Response(servicio_serializer.data)

    elif request.method == 'POST':
        servicio_serializer = servicioSerializer(data=request.data)
        if servicio_serializer.is_valid():
            servicio_serializer.save()
            return Response(servicio_serializer.data, status=status.HTTP_201_CREATED)
        return Response(servicio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)