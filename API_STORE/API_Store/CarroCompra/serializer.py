# serializers.py

from rest_framework import serializers
from .models import Carreto, ListaProductos

class CarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreto
        fields = ['id_client', 'estat']

class ListaProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaProductos
        fields = ['id_carreto', 'producto', 'unitats']

class UpdateUnitatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaProductos
        fields = ['unitats']  # Solo permitir el campo 'unitats'