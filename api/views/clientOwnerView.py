from email.policy import HTTP
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from api.models.clientOwner import ClientOwner
from api.serializers.clientOwnerSerializer import ClientOwnerSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])
def client_owner_api_view(request):

    if request.method == 'GET':
        clientOwner = ClientOwner.objects.all()
        if clientOwner:
            serializer = ClientOwnerSerializer(clientOwner, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No se han encontrado enfermedades'},status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = ClientOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAuthenticated])
def client_owner_detail_api_view(request, pk= None):

    clientOwner = ClientOwner.objects.filter(id = pk).first()
    if clientOwner == None:
        return Response({'message': 'No se ha encontrado el cliente'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientOwnerSerializer(clientOwner)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ClientOwnerSerializer(clientOwner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        clientOwner.delete()
        return Response({'message': 'El cliente fue eliminado'},status=status.HTTP_200_OK)