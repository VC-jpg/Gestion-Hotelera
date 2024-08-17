from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Reserva  # Importa tus modelos aquí

class MyAdminSite(AdminSite):
    site_header = 'Administración de Hotel Duerme Bien'
    site_title = 'Hotel Duerme Bien Admin'
    index_title = 'Bienvenido al panel de administración'

admin_site = MyAdminSite(name='myadmin')

# Registra tus modelos aquí
admin_site.register(Reserva)

# Si tienes otros modelos, regístralos de la siguiente manera
# admin_site.register(OtroModelo)
