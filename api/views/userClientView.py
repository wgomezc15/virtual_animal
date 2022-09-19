from rest_framework import generics
from rest_framework import status,views
from rest_framework.response import Response
from django.http import JsonResponse
from django.urls import is_valid_path

from api.models.userClient import UserClient_Tabla
from api.serializers.userClientSerializer import userClientSerializer
from virtual_animal.api.models import user
from virtual_animal.api.serializers.userClientSerializer import userClient


def userClientGetview(request):
    if request.method == 'GET':
        userClient_serializer = UserClient_Tabla.objects.all()
        userClient_serializer = userClientSerializer(userClient_serializer, many=True)
        return Response(userClient_serializer.data)

def userClientUpdateView(request):
    if request.method == 'GET':
        userClient = UserClient_Tabla.objects.first()
        userClient_serializer = userClientSerializer(userClient)
        return Response(userClient_serializer.data)

    elif request.method == 'PUT':
        userClient = UserClient_Tabla.objects.first()
        userClient_serializer = userClientSerializer(userClient,data = request.data)
        if userClient_serializer.is_valid():
            userClient_serializer.save()
            return Response(userClient_serializer.data)
        return Response(userClient_serializer.error)

def userClientDeleteView(request):
    if request.method == 'GET':
        userClient = UserClient_Tabla.objects.firts()
        userClient_serializer = userClientSerializer(userClient)
        return Response(userClient_serializer.data)
    
    elif request.method == 'DELETE':
        userClient = UserClient_Tabla.objects.first()
        userClient.delete()
        return Response('Eliminado')

def userClientCreateView(request):
    if request.method == 'GET':
        userClient_serializer = UserClient_Tabla.objects.all()
        userClient_serializer = userClientSerializer(userClient_serializer, many=True)
        return Response(userClient_serializer.data)

    elif request.method == 'POST':
        userClient_serializer = userClientSerializer(data=request.data)
        if userClient_serializer.is_valid():
            userClient_serializer.save()
            return Response(userClient_serializer.data, status=status.HTTP_201_CREATED)
        return Response(userClient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        