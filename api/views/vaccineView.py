from email.policy import HTTP
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from api.models.vaccines import AnimalVaccinations
from api.serializers.vaccinesSerializer import VaccinesSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def vaccine_api_view(request):
    pass
    