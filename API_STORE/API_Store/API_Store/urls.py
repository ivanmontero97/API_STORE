
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('producto/', include('Catalago.urls')),
]
