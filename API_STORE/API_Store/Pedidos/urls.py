from django.urls import path
from . import views

urlpatterns = [
    path('historial/', views.historial_comandas, name='historial_comandas'),
    path('historial/cliente/<int:cliente_id>/', views.historial_comandas_cliente, name='historial_comandas_cliente'),
    path('historial/no-finalizadas/', views.comandas_no_finalizadas, name='comandas_no_finalizadas'),
]

