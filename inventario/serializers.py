from rest_framework import serializers
from .models.item import item
from .models.grupo import grupo


class itemSerializers(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'


class grupoSerializers(serializers.ModelSerializer):
    class Meta:
        model = grupo
        fields = '__all__'
