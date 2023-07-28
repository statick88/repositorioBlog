# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PublicacionForm, ComentarioForm
from .models import Publicacion, Comentario
from rest_framework import generics
from .serializers import PublicacionSerializer, ComentarioSerializer

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'lista_publicaciones.html', {'publicaciones': publicaciones})

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm()
    return render(request, 'crear_publicacion.html', {'form': form})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    comentarios = Comentario.objects.filter(publicacion=publicacion)

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.save()
            return redirect('detalle_publicacion', pk=pk)
    else:
        comentario_form = ComentarioForm()

    context = {
        'publicacion': publicacion,
        'comentarios': comentarios,
        'comentario_form': comentario_form,
    }
    return render(request, 'detalle_publicacion.html', context)

def actualizar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'crear_publicacion.html', {'form': form})

def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('lista_publicaciones')
    return render(request, 'eliminar_publicacion.html', {'publicacion': publicacion})

def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = ComentarioForm()
    return render(request, 'crear_comentario.html', {'form': form})

def lista_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'lista_comentarios.html', {'comentarios': comentarios})

def actualizar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST, instance=comentario)
        if comentario_form.is_valid():
            comentario_form.save()
            return redirect('detalle_publicacion', pk=comentario.publicacion.pk)
    else:
        comentario_form = ComentarioForm(instance=comentario)

    context = {
        'comentario_form': comentario_form,
    }
    return render(request, 'actualizar_comentario.html', context)

def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    publicacion_pk = comentario.publicacion.pk
    comentario.delete()
    return redirect('detalle_publicacion', pk=publicacion_pk)

class ListaPublicaciones(generics.ListCreateAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class DetallePublicacion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class ListaComentarios(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class DetalleComentario(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer