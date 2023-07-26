# publicaciones/urls.py

from django.urls import path
from .views import ListaPublicacionesView

urlpatterns = [
    path('publicaciones/', ListaPublicacionesView.as_view(), name='lista_publicaciones'),
]
