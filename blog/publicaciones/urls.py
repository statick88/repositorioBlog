# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_publicaciones, name='lista_publicaciones'),
    path('crear/', views.crear_publicacion, name='crear_publicacion'),
    path('actualizar/<int:pk>/', views.actualizar_publicacion, name='actualizar_publicacion'),
    path('eliminar/<int:pk>/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('crear_comentario/', views.crear_comentario, name='crear_comentario'),
    path('lista_comentarios/', views.lista_comentarios, name='lista_comentarios'),
    path('actualizar_comentario/<int:pk>/', views.actualizar_comentario, name='actualizar_comentario'),
    path('eliminar_comentario/<int:pk>/', views.eliminar_comentario, name='eliminar_comentario'),
]