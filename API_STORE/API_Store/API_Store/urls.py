
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Tu API",
      default_version='v1',
      description="Documentación de la API",
      terms_of_service="",
      contact=openapi.Contact(email="contact@tusitio.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('producto/', include('Catalago.urls')),
    path('carreto/',include('CarroCompra.urls')),
    path('admin/',admin.site.urls),
    path('pedidos/', include('Pedidos.urls')),
    path('pagos/', include('Pagos.urls')),
    path('cliente/', include('Cliente.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
