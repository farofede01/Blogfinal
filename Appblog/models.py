from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tema(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.creador} - {self.titulo}"
    
