from email.policy import HTTP
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from api.models.userClient import UserClient
from api.serializers.userClienteSerializer import UserClienteSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])
def user_cliente_api_view(request):

    if request.method == 'GET':
        userCliente = UserClient.objects.all()
        if userCliente:
            serializer = UserClienteSerializer(userCliente, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No se han encontrado clientes registrados'},status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = UserClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAuthenticated])
def user_cliente_detail_api_view(request, pk= None):

    userCliente = UserClient.objects.filter(id = pk).first()
    if userCliente == None:
        return Response({'message': 'No se ha encontrado el cliente'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserClienteSerializer(userCliente)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = UserClienteSerializer(userCliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userCliente.delete()
        return Response({'message': 'El cliente fue eliminado'},status=status.HTTP_200_OK)