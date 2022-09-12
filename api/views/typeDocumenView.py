from rest_framework import generics
from rest_framework import status,views
from django.http import JsonResponse
from rest_framework.response import Response
from api.models.typeDocument import TypeDocument
from api.serializers.typeDocumentSerializer import TypeDocumentSerializer

class TypeDocumentCreateView(views.APIView):

    def post(self, request):
        serializer = TypeDocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()               
        return Response(None, status=status.HTTP_200_OK)
