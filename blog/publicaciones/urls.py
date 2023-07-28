# urls.py
from django.urls import path
from . import views


urlpatterns = [
    # Rutas de Publicaciones
    path('', views.lista_publicaciones, name='lista_publicaciones'),
    path('lista/', views.lista_publicaciones, name='lista_publicaciones'),
    path('crear/', views.crear_publicacion, name='crear_publicacion'),
    path('detalle/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('actualizar/<int:pk>/', views.actualizar_publicacion, name='actualizar_publicacion'),
    path('eliminar/<int:pk>/', views.eliminar_publicacion, name='eliminar_publicacion'),

    # Rutas de Comentarios
    path('<int:pk>/actualizar_comentario/', views.actualizar_comentario, name='actualizar_comentario'),
    path('<int:pk>/eliminar_comentario/', views.eliminar_comentario, name='eliminar_comentario'),

    # Rutas de API
    path('publicaciones/', views.ListaPublicaciones.as_view(), name='lista_publicaciones'),
    path('publicaciones/<int:pk>/', views.DetallePublicacion.as_view(), name='detalle_publicacion'),
    path('comentarios/', views.ListaComentarios.as_view(), name='lista_comentarios'),
    path('comentarios/<int:pk>/', views.DetalleComentario.as_view(), name='detalle_comentario'),
]