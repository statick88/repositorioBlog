# publicaciones/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.vista_bienvenida, name='vista_bienvenida'),
]