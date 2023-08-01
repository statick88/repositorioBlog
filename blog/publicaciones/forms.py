# forms.py
from django import forms
from .models import Publicacion
from .models import Comentario
from ckeditor.widgets import CKEditorWidget

class PublicacionForm(forms.ModelForm):
    contenido = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido' , 'autor']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['contenido'].widget = CKEditorWidget()    
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('autor', 'contenido',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contenido'].widget = CKEditorWidget()