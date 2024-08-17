from django.contrib import admin
from django.urls import path, include
from reservas.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('reservas/', include('reservas.urls')),
    # otras rutas aquí
]
