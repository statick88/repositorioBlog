from django.db import models

class Publicacion(models.Model):

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=90)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):

    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    autor = models.CharField(max_length=90)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.publicacion}"
