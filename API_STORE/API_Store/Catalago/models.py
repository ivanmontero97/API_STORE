from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    precio = models.FloatField()
    stock = models.IntegerField(default=10)
    isActive = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
     
    def __str__(self):
        return f"""Datos producto: \n
                    id: {self.id},\n
                    nombre: {self.nombre},\n 
                    descripcion: {self.descripcion},\n
                    precio: {self.precio},\n
                    stock: {self.stock},\n
                    isActive: {self.isActive},\n
                """
    class Meta:
        db_table = 'Producte' 

                    
    