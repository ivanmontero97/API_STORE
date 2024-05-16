from rest_framework import serializers
from .models import *

class CarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreto
        fields = '__all__'
class ListaProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaProductos
        fields = '__all__'