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


class TypeDocumentGetView(generics.RetrieveAPIView):
    queryset = TypeDocument.objects.all()
    serializer_class = TypeDocumentSerializer
   
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TypeDocumentGetAllView(generics.RetrieveAPIView):
 
    def get(self,request):
        obj = list(TypeDocument.objects.values())    
        return JsonResponse(obj, safe=False)
        
class TypeDocumentDeleteView(views.APIView):
 
    def get(self, request, id):
        TypeDocument.objects.filter(id=id).delete()            
        return Response(None, status=status.HTTP_200_OK)

class TypeDocumentUpdateView(views.APIView):
 
    def post(self, request):
        TypeDocument.objects.filter(id=request.data["id"]).update(code=request.data["code"], name = request.data["name"])
        return Response(None, status=status.HTTP_200_OK)


