from django.db import models
from Cliente.models import *
from CarroCompra.models import *
# Create your models here.

class Comanda(models.Model):
    id = models.AutoField(primary_key=True)
    id_carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado_finalizado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""Datos de la comanda: \n
                    id: {self.id},\n
                    id_carreto: {self.id_carreto},\n
                    id_client: {self.id_client},\n
                    estat_finalizado: {self.estado_finalizado},\n
                    created_at: {self.created_at},\n
                    updated_at: {self.updated_at}
                """
        
    class Meta:
        db_table = 'Comanda'
