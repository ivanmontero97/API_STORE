from django.urls import path
from . import views


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Api Store",
      default_version='v1',
      description="Documentación de la API",
      terms_of_service="https://www.tusitio.com/terms/",
      contact=openapi.Contact(email="contact@tusitio.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('get/', views.get_prod, name = 'get'),
    path('add/', views.add_or_update_prod, name = 'add'),
    path('get/<int:pk>/', views.get_prod_By_Id, name = 'getById'),
    path('stock/<int:pk>', views.update_stock, name = 'updateStock'),
    path('isvalid/<int:pk>', views.isValid, name = 'isValid'),
    path('isnotvalid/<int:pk>', views.isnotValid, name = 'isnotValid'),
]

