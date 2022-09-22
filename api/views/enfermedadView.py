from email.policy import HTTP
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from api.models.enfermedad import Enfermedad
from api.serializers.enfermedadSerializer import EnfermedadSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def enfermedad_api_view(request):

    if request.method == 'GET':
        enfermedad = Enfermedad.objects.all()
        if enfermedad:
            serializer = EnfermedadSerializer(enfermedad, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No se han encontrado enfermedades'},status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = EnfermedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def enfermedad_detail_api_view(request, pk= None):

    enfermedad = Enfermedad.objects.filter(id = pk).first()
    if enfermedad == None:
        return Response({'message': 'No se ha encontrado la enfermedad'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EnfermedadSerializer(enfermedad)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = EnfermedadSerializer(enfermedad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        enfermedad.delete()
        return Response({'message': 'La enfemedad fue eliminada'},status=status.HTTP_200_OK)