from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_prod, name = 'get'),
    path('add/', views.add_or_update_prod, name = 'add'),
    path('get/<int:pk>/', views.get_prod_By_Id, name = 'getById'),
    path('stock/<int:pk>', views.update_stock, name = 'updateStock'),
    path('isvalid/<int:pk>', views.isValid, name = 'isValid'),
    path('isnotvalid/<int:pk>', views.isnotValid, name = 'isnotValid'),
    path('isnotvalid/<int:pk>', views.isnotValid, name = 'isnotValid')
]

