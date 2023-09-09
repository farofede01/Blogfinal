from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='imagen_perfil/', blank=True, null=True)

    def _str_(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega campos personalizados para el perfil de usuario si es necesario
    # Por ejemplo: avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username

