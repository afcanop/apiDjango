from django.urls import path
from inventario.views import item as itemViews
from inventario.views import grupo as grupoViews

urlpatterns = [
    # item
    path('item/lista', itemViews.item_lista),
    path('item/detalle', itemViews.item_detalle),
    path('item/nuevo', itemViews.item_nuevo),
    # grupo
    path('grupo/lista', grupoViews.grupo_lista),
    path('grupo/nuevo', grupoViews.grupo_nuevo),

]