from rest_framework import serializers
from .models import item


class itemSerializers(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = ['id', 'nombre', 'estado_importado']
