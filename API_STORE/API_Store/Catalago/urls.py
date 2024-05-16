from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_prod, name = 'get'),
    path('add/', views.add_or_update_prod, name = 'add'),
    path('get/<int:pk>/', views.get_prod_By_Id, name = 'getById'),
    path('stock/', views.get_stock, name = 'getStock')
]

