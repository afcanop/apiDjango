from django.urls import path
from inventario.views import item
from inventario.views import grupo as grupoViews



urlpatterns = [
    # item
    path('item/', item.ItemView.as_view({
        'get': 'item_lista',
    }), name='item_detalle'),
    path('item/detalle', item.ItemView.as_view({
        'get': 'item_detalle',
    }), name='item_detalle'),
    path('item/nuevo', item.ItemView.as_view({
        'post': 'item_nuevo',
    }), name='item_nuevo'),
    # grupo
    # path('grupo/lista', grupoViews.grupo_lista),
    # path('grupo/nuevo', grupoViews.grupo_nuevo),

]
