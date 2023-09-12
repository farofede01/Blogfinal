from django import forms
from .models import *

class crearTemaform (forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo', 'descripcion','imagen']
    imagen = forms.ImageField(label='Subir Imagen')

