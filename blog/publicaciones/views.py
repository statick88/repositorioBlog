# publicaciones/views.py

from django.shortcuts import render
from django.views.generic import ListView
from .models import Publicacion

class ListaPublicacionesView(ListView):
    model = Publicacion
    template_name = 'lista_publicaciones.html'
    context_object_name = 'publicaciones'
