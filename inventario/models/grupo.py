from django.db import models
from .item import item


class grupo(models.Model):
    nombre = models.CharField(name="nombre", max_length=10)
    estadoImportado = models.BooleanField(name="estado_importado", default=False)
    item = models.ForeignKey(item, on_delete=models.SET_NULL, blank=True, null=True, )
