from django.urls import path
from . import views

urlpatterns = [
    path('addCarreto/', views.add_Carreto, name = 'addCarreto'),
    path('addProduct/', views.add_Products, name = 'addProduct'),
    path('deleteProduct/<int:pk_product>/', views.delete_Producto, name = 'deleteProduct'),
    path('deleteAllProducts/<int:pk_carreto>/', views.delete_AllProductsFromLista, name = 'deleteAllProductsFromCarreto'),
    path('updateProductQuantity/<int:pk_product>/', views.update_product_quantity, name = 'updateProductQuantity'),
    path('get_products_in_carreto/<int:pk_carreto>/', views.get_products_in_carreto, name='get_products_in_carreto'),
    path('update_estat_carreto/<int:pk_carreto>/', views.update_estat_carreto, name='update_estat_carreto'),
    path('comprar/<int:pk_carreto>/', views.comprar, name='comprar'),  
]