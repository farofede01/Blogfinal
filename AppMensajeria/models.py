from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.remitente.username}: {self.contenido}'

