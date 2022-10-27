from django.urls import path
from inventario.views import item as itemViews
from inventario.views import grupo as grupoViews

urlpatterns = [
    # item
    path('item/lista', itemViews.item_lista),
    path('item/detalle', itemViews.item_detalle),
    # grupo
    path('grupo/nuevo', grupoViews.grupo_nuevo),

]