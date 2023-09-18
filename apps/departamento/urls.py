from django.urls import path
from .views import (DepartamentoList,
                    DepartamentoCreate,
                    DepartamentoDelete,
                    DepartamentoEdit)

urlpatterns = [
    path('list', DepartamentoList.as_view(), name='list_departamentos'),
    path('novo/',
         DepartamentoCreate.as_view(), name='create_departamento'),
    path('deletar/<int:pk>/',
         DepartamentoDelete.as_view(), name='delete_departamento'),
    path('editar/<int:pk>/',
         DepartamentoEdit.as_view(), name='edit_departamento'),
]
