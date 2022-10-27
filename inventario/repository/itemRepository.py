from inventario.models.item import item


class itemRepository:

    def lista(self):
        datos = item.objects.all().order_by('-id')
        return datos

    def detalle(self):
        data = item.objects.values('id', 'nombre', ).get(pk=2)
        return data

    def nuevo(self):
        arItem = item()
        arItem.nombre = "nuevo item"
        arItem.estado_importado = False
        arItem.estado_disponible = False
        arItem.save()
        return arItem
