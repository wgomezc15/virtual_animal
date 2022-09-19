from email.policy import HTTP
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from api.models.typeDocument import TypeDocument
from api.serializers.typeDocumentSerializer import TypeDocumentSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def typeDocument_api_view(request):

    if request.method == 'GET':
        typeDocument = TypeDocument.objects.all()
        if typeDocument:
            serializer = TypeDocumentSerializer(typeDocument, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No se han encontrado documentos'},status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = TypeDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def type_document_detail_api_view(request, pk= None):

    typeDocument = TypeDocument.objects.filter(id = pk).first()
    if typeDocument == None:
        return Response({'message': 'No se ha encontrado el documento'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TypeDocumentSerializer(typeDocument)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = TypeDocumentSerializer(typeDocument, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        typeDocument.delete()
        return Response({'message': 'El Documento fue eliminado'},status=status.HTTP_200_OK)