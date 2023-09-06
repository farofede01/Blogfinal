from django.shortcuts import render
from django.shortcuts import render
from AppRegistro.models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.
def formulario(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre_usuario = info ["nombreusuario"] 
            nombre = info ["nombre"]
            apellidos = info ["apellidos"]
            email = info ["email"]
            contraseña = info ["contraseña"]
            usuario = Usuario(nombre_usuario = nombre_usuario, nombre = nombre, apellidos = apellidos ,email = email, contraseña = contraseña)
            usuario.save()
            formulario_registro = usuarioForm()
            return render (request, "AppRegistro/registro.html", {"mensaje":"Usuario creado"})
        else:
            return render (request, "AppRegistro/registro.html", {"mensaje": "Datos invalidos"})
    else:   
        formulario_registro = usuarioForm()
    
    return render(request, "AppCoder/registro.html", {"formulario": formulario_registro})

            

