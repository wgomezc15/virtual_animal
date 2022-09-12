from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from api import views

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
]