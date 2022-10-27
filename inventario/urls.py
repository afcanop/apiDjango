from django.urls import path
from inventario import views

urlpatterns = [
    path('item/lista', views.item_lista),
    path('item/detalle', views.item_detalle),
]