from django.db import models
from django.urls import reverse
from apps.funcionario.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self
                                                   .funcionario.id])

    def __str__(self):
        return self.descricao
