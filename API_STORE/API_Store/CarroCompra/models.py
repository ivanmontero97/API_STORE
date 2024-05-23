from django.db import models
from Cliente.models import *
from Catalago.models import *

# Create your models here.
from django.db import models

class Carreto(models.Model):
    id = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ESTADO_CHOICES = (
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
    )
    estat = models.CharField(max_length=7, choices=ESTADO_CHOICES, default='abierto')

    def __str__(self):
        return f"""Datos del carretó: \n
                    id: {self.id},\n
                    id_client: {self.id_client},\n
                    estat: {self.estat},\n
                """
    class Meta:
        db_table = 'Carreto' 



class ListaProductos(models.Model):
    id = models.AutoField(primary_key=True)
    id_carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  
    unitats = models.IntegerField()

    def __str__(self):
        return f"""Datos de la lista de productos: \n
                    id: {self.id},\n
                    id_carreto: {self.id_carreto},\n
                    producto: {self.producto},\n
                    unitats: {self.unitats}
                """
    
    class Meta:
        db_table = 'ListaProductos' 

