from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuarios (AbstractUser):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def _str_(self):
        return f"{self.nombre_usuario}-{self.nombre}-{self.apellidos}-{self.email}"
    