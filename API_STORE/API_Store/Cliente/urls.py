from django.urls import path
from . import views

urlpatterns = [
    path('cliente/', views.cliente_list, name='cliente_list'),          
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
]

