from django.db import models
from Pedidos.models import *
# Create your models here.
from django.db import models

class Pagos(models.Model):
    id = models.AutoField(primary_key=True)
    id_comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    import_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    num_tarj = models.CharField(max_length=16)
    data_caducitat_tarj = models.DateField()
    cvc_tarj = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""Datos del pago: \n
                    id: {self.id},\n
                    id_comanda: {self.id_comanda},\n
                    import_total: {self.import_total},\n
                    data_pagament: {self.data_pagament},\n
                    num_tarj: {self.num_tarj},\n
                    data_caducitat_tarj: {self.data_caducitat_tarj},\n
                    cvc_tarj: {self.cvc_tarj},\n
                    created_at: {self.created_at},\n
                    updated_at: {self.updated_at}
                """
    class Meta:
        db_table = 'Pagos'