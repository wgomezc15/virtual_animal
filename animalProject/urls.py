from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from api import views
from api.views.typeDocumenView import typeDocument_api_view,type_document_detail_api_view
from api.views import enfermedadView
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

]