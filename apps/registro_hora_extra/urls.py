from django.urls import path
from .views import (HoraExtraList)


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('editar/<int:pk>/',
    #      FuncionarioEdit.as_view(), name='edit_funcionarios'),
    # path('deletar/<int:pk>/',
    #      FuncionarioDelete.as_view(), name='delete_funcionario'),
    # path('novo/',
    #      FuncionarioCreate.as_view(), name='create_funcionario'),
]
