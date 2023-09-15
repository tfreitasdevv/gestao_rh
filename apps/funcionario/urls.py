from django.urls import path
from .views import FuncionariosList

urlpatterns = [
    path('funcionarios', FuncionariosList.as_view(), name='list_funcionarios'),
]
