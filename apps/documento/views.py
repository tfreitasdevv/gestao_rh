from django.urls import reverse
from django.views.generic.edit import (DeleteView,
                                       CreateView)
from .models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('edit_funcionarios',
                       args=[self.kwargs['funcionario_id']])


class DocumentoDelete(DeleteView):
    pass
