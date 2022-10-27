from rest_framework import serializers
from .models.item import item


class itemSerializers(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = ['id', 'nombre', 'estado_importado']
