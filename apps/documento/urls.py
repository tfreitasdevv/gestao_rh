from django.urls import path
from .views import DocumentoCreate, DocumentoDelete


urlpatterns = [
    path('deletar/<int:pk>/',
         DocumentoDelete.as_view(), name='delete_documento'),
    path('novo/',
         DocumentoCreate.as_view(), name='create_documento'),
]
