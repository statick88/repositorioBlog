# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('lista/', views.lista_publicaciones, name='lista_publicaciones'),
    path('crear/', views.crear_publicacion, name='crear_publicacion'),
]