# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    # Este método faz com que o funcionário logado seja atribuído
    # à empresa no momento da criação caso seja válido o form
    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('Ok')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']
