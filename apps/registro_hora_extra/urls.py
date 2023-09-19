from django.urls import path
from .views import (HoraExtraList,
                    HoraExtraEdit)


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('editar/<int:pk>/',
         HoraExtraEdit.as_view(), name='edit_hora_extra'),
    # path('deletar/<int:pk>/',
    #      FuncionarioDelete.as_view(), name='delete_funcionario'),
    # path('novo/',
    #      FuncionarioCreate.as_view(), name='create_funcionario'),
]
