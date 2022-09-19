from email.policy import HTTP
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from api.models.Enfermedad import tabla_Enfermedad
from api.serializers.EnfermedadSerializer import EnfermedadSerializer

@api_view(['GET','POST'])
def enfermedad_create_view(request,pk=None):
    if request.method == 'GET':
        Enfermedad = tabla_Enfermedad.objects.all()
        serializer = EnfermedadSerializer(Enfermedad, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    elif request.method == 'POST':
        serializer = EnfermedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Metodo para obtener toda la informacion de toda la tabla
@api_view(['GET'])
def enfermedad_getall_view(request,pk=None):
    if request.method == 'GET':
        Enfermedad= tabla_Enfermedad.objects.all()
        serializer = EnfermedadSerializer(Enfermedad, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])# obtener un registro detallado
def enfermedad_detail_view(requests, pk=None):

    if requests.method == 'GET':
        Enfermedad =  tabla_Enfermedad.objects.filter(id=pk).first()
        enfermedad_Serializer = EnfermedadSerializer(Enfermedad)
        return Response(enfermedad_Serializer.data)


@api_view(['GET', 'PUT'])#actualizar
def enfermedad_update_view(request, pk= None):

    Enfermedad = tabla_Enfermedad.objects.filter(id = pk).first()
    if Enfermedad == None:
        return Response({'message': 'No se ha encontrado enfermedad'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EnfermedadSerializer(Enfermedad)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = EnfermedadSerializer(Enfermedad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])#borrar
def enfermedad_delete_view(request, pk= None):

    Enfermedad = tabla_Enfermedad.objects.filter(id = pk).first()
    if Enfermedad == None:
        return Response({'message': 'No se ha encontrado Enfermedad'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EnfermedadSerializer(Enfermedad)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        Enfermedad.delete()
        return Response('Eliminado')