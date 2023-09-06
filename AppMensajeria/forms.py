from django import forms
from .models import Mensaje

class FormularioMensaje(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['contenido']
        