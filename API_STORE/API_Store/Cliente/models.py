from django.db import models

# Create your models here.


class Cliente (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"""Datos cliente: \n
                id: {self.id}
                nombre :{self.nombre},\n 
                apellidos: {self.apellidos},\n
                email: {self.email}
                """ 
    
    class Meta:
        db_table = 'Cliente'
        
        