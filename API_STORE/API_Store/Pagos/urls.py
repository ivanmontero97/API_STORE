from django.urls import path
from . import views

urlpatterns = [
    path('pagoTarjeta/<int:pk>', views.get_datos_pago, name = 'get_datos_pago'),
    path('comanda/<int:pk>/', views.consultar_estado_comanda, name='consultar_estado_comanda'),
]
