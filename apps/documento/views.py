from django.views.generic.edit import (DeleteView,
                                       CreateView)
from .models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']


class DocumentoDelete(DeleteView):
    pass
