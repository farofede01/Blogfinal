from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=50, null=True)
    def __str__(self):
        return f"{self.nombre_usuario}-{self.nombre}-{self.apellidos}-{self.email}"-{self.contraseña}
    