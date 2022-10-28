from inventario.models.grupo import grupo
from inventario.models.item import item
from django.db.models import F


class grupoRepository:

    def lista(self):

        datos = grupo.objects.filter(item_id=1)\
            .values(
                'id',
                'nombre',
                codigoItemFk=F('item__id'),
                itemNombre=F('item__nombre')
            )

        return datos


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
    return arGrupo
