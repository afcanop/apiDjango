from django.db import models
class item(models.Model):
    nombre = models.CharField(name="nombre", max_length=10)
    estadoImportado = models.BooleanField(name="estado_importado", default=False)