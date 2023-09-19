from django.urls import path
from .views import (HoraExtraList,
                    HoraExtraEdit,
                    HoraExtraDelete)


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('editar/<int:pk>/',
         HoraExtraEdit.as_view(), name='edit_hora_extra'),
    path('deletar/<int:pk>/',
         HoraExtraDelete.as_view(), name='delete_hora_extra'),
    # path('novo/',
    #      FuncionarioCreate.as_view(), name='create_funcionario'),
]
