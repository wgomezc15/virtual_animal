from email.policy import HTTP
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from api.models.consultaMedica import ConsultaMedica
from api.serializers.consultaMedicaSerializer import ConsultaMedicaSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def consulta_api_view(request):

    if request.method == 'GET':
        consulta = ConsultaMedica.objects.all()
        if consulta:
            serializer = ConsultaMedicaSerializer(consulta, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No se han encontrado consultas registradas'},status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = ConsultaMedicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def consulta_detail_api_view(request, pk= None):

    consulta = ConsultaMedica.objects.filter(id = pk).first()
    if consulta == None:
        return Response({'message': 'No se ha encontrado la consulta'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConsultaMedicaSerializer(consulta)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ConsultaMedicaSerializer(consulta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        consulta.delete()
        return Response({'message': 'La consulta fue eliminada'},status=status.HTTP_200_OK)