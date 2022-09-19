from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from api import views
from api.views.typeDocumenView import typeDocument_api_view,type_document_detail_api_view


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),

    path('typedocument/', views.TypeDocumentCreateView.as_view()),
    path('typedocument/<int:pk>/', views.TypeDocumentGetView.as_view()),
    path('typedocumentall/', views.TypeDocumentGetAllView.as_view()),
    path('typedocumentadelete/<int:id>/', views.TypeDocumentDeleteView.as_view()),
    path('typedocumentupdate/', views.TypeDocumentUpdateView.as_view()),
    path('typedocument/', typeDocument_api_view, name = 'typeDocument_api_view'),
    path('typedocument/<int:pk>', type_document_detail_api_view, name = 'type_document_detail_api_view'),

    
    #Tabla servicio -- Insertado por Yasmin
    path('serviciogetall/', views.servicioView.servicio_getall_view, name = 'ServicioGetAllView'), 
    path('serviciogetdetail/<int:pk>', views.servicioView.servicio_detail_view, name = 'servicio_detail_views'),    
    path('servicioupdate/<int:pk>', views.servicioView.servicio_update_view, name = 'servicio_update_view'),
    path('serviciodelete/<int:pk>', views.servicioView.servicio_delete_view, name = 'servicio_delete_view'),
    path('serviciocreate/', views.servicioView.servicio_create_view, name = 'servicio_create_view' ),
    #Tabla servicio -- Insertado por Yasmin

]


