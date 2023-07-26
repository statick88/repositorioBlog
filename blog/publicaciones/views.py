# publicaciones/views.py

from django.http import HttpResponse

def vista_bienvenida(request):
    return HttpResponse("¡Bienvenido al blog!")