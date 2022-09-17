import imp
from rest_framework import generics
from rest_framework import status,views
from django.http import JsonResponse
from rest_framework.response import Response
from api.models import servicio
from api.models.servicio import Tabla_Servicio
from api.serializers.servicioSerializer import servicioSerializer

#funcion para crear registro de servicio
class ServicioCreateView(views.APIView):

    def post(self, request):
        serializer = servicioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()               
        return Response(None, status=status.HTTP_200_OK)

#Función para obtener información de los registros
class ServicioGetView(generics.RetrieveAPIView):
    queryset = servicio.objects.all()
    serializer_class = servicioSerializer
   
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#Función para obtener valores de los registros
class ServicioGetAllView(generics.RetrieveAPIView):
 
    def get(self,request):
        obj = list(servicio.objects.values())    
        return JsonResponse(obj, safe=False)

#función para eliminar registros
class ServicioDeleteView(views.APIView):
 
    def get(self, request, id):
        servicio.objects.filter(id=id).delete()            
        return Response(None, status=status.HTTP_200_OK)

#Funcion para actualizar un registro
class ServicioUpdateView(views.APIView):
 
    def post(self, request):
        servicio.objects.filter(id=request.data["id"]).update(name = request.data["name"])
        return Response(None, status=status.HTTP_200_OK)