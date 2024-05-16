from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_prod, name = 'get'),
    path('add/', views.add_prod, name = 'add'),
    path('get/<int:pf>/', views.get_prod_By_Id, name = 'getById')
]

