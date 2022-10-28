from inventario.models.grupo import grupo
from inventario.models.item import item


class grupoRepository:

    # def lista(self):
    #     datos = grupo.objects.all().order_by('-id')
    #     return datos
    #
    # def detalle(self):
    #     data = grupo.objects.values('id', 'nombre', ).get(pk=2)
    #     return data

    def nuevo(self):
        arItem = item.objects.get(pk=1)
        arGrupo = grupo()
        arGrupo.nombre = "nuevo item"
        arGrupo.estado_importado = False
        arGrupo.estado_disponible = False
        arGrupo.item = arItem
        arGrupo.save()
        print(arGrupo)
        return arGrupo
