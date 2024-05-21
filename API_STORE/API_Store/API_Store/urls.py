
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('producto/', include('Catalago.urls')),
    path('carreto/',include('CarroCompra.urls')),
    path('admin/',admin.site.urls)
]
