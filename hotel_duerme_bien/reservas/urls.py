from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_reserva, name='crear_reserva'),
]
