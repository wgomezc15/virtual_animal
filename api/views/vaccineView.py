from email.policy import HTTP
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from api.models.vaccines import Tabla_Vacunas
from api.serializers.vaccinesSerializer import VaccinesSerializer

#Este metodo permite realizar la insercion de una nueva vacuna
@api_view(['GET','POST'])
def vaccine_create_view(request,pk=None):
    if request.method == 'GET':
        vaccine = Tabla_Vacunas.objects.all()
        serializer = VaccinesSerializer(vaccine, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    elif request.method == 'POST':
        serializer = VaccinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Metodo para obtener toda la informacion de toda la tabla
@api_view(['GET'])
def vaccine_getall_view(request,pk=None):
    if request.method == 'GET':
        vaccine = Tabla_Vacunas.objects.all()
        serializer = VaccinesSerializer(vaccine, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])# obtener un registro detallado
def vaccine_detail_view(requests, pk=None):

    if requests.method == 'GET':
        vaccine =  Tabla_Vacunas.objects.filter(id=pk).first()
        vaccine_serializer = VaccinesSerializer(vaccine)
        return Response(vaccine_serializer.data)


@api_view(['GET', 'PUT'])#actualizar
def vaccine_update_view(request, pk= None):

    vaccine = Tabla_Vacunas.objects.filter(id = pk).first()
    if vaccine == None:
        return Response({'message': 'No se ha encontrado el documento'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VaccinesSerializer(vaccine)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = VaccinesSerializer(vaccine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])#borrar
def vaccine_delete_view(request, pk= None):

    vaccine = Tabla_Vacunas.objects.filter(id = pk).first()
    if vaccine == None:
        return Response({'message': 'No se ha encontrado el documento'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VaccinesSerializer(vaccine)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        vaccine.delete()
        return Response('Eliminado')

    
    