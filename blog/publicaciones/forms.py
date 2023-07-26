# forms.py
from django import forms
from .models import Publicacion
from .models import Comentario

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'autor']
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('autor', 'contenido',)