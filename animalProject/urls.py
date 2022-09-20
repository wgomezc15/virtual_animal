from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from api import views
from api.views.typeDocumenView import typeDocument_api_view,type_document_detail_api_view

from api.views import enfermedadView
from api.views import vaccineView
from api.views.petView import pet_api_view,pet_detail_api_view
from api.views.petView import pet_api_view,pet_detail_api_view
from api.views.userClientView import user_cliente_api_view,user_cliente_detail_api_view

 main
urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),

    path('typedocument/', typeDocument_api_view, name = 'typeDocument_api_view'),
    path('typedocument/<int:pk>', type_document_detail_api_view, name = 'type_document_detail_api_view'),

    
    path('CreacionEnfermedad/',enfermedadView.enfermedad_create_view,name='enfermedad_create_view'),
    path('enfermedadesnegetall/',enfermedadView.enfermedad_getall_view,name='enfermedad_getall_view'),
    path('enfermedadgetdetail/<int:pk>',enfermedadView.enfermedad_detail_view,name='enfermedad_detail_view'),
    path('enfermedadupdate/<int:pk>',enfermedadView.enfermedad_update_view,name='enfermedad_update_view'),
    path('enfermedaddelete/<int:pk>',enfermedadView.enfermedad_delete_view,name='enfermedad_delete_view'),


    #se adiccionan Urls de la tabla vaccines por Yulany Munevar 
    path('vaccinecreate/',vaccineView.vaccine_create_view,name='vaccine_create_view'),
    path('vaccinegetall/',vaccineView.vaccine_getall_view,name='vaccine_getall_view'),
    path('vaccinegetdetail/<int:pk>',vaccineView.vaccine_detail_view,name='vaccine_detail_view'),
    path('vaccineupdate/<int:pk>',vaccineView.vaccine_update_view,name='vaccine_update_view'),
    path('vaccinedelete/<int:pk>',vaccineView.vaccine_delete_view,name='vaccine_delete_view'),

    #Tabla servicio -- Insertado por Yasmin
    path('serviciogetall/', views.servicioView.servicio_getall_view, name = 'ServicioGetAllView'), 
    path('serviciogetdetail/<int:pk>', views.servicioView.servicio_detail_view, name = 'servicio_detail_views'),    
    path('servicioupdate/<int:pk>', views.servicioView.servicio_update_view, name = 'servicio_update_view'),
    path('serviciodelete/<int:pk>', views.servicioView.servicio_delete_view, name = 'servicio_delete_view'),
    path('serviciocreate/', views.servicioView.servicio_create_view, name = 'servicio_create_view' ),
    #Tabla servicio -- Insertado por Yasmin

    path('pet/', pet_api_view, name = 'pet_api_view'),
    path('pet/<int:pk>', pet_detail_api_view, name = 'pet_detail_api_view'),
    
    path('client/', user_cliente_api_view, name = 'user_client_api_view'),
    path('client/<int:pk>', user_cliente_detail_api_view, name = 'user_client_detail_api_view'),

]