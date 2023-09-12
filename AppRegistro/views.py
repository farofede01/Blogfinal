from django.shortcuts import render
from django.shortcuts import render
from AppRegistro.models import *
from django.http import HttpResponse
from .forms import *
from .forms import UserRegisterForm

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre_usuario = info["username"]  
            nombre = info["nombre"]
            apellidos = info["apellidos"]
            email = info["email"]
            contraseña = info["password1"]  
            usuario = Usuarios(nombre_usuario=nombre_usuario, nombre=nombre, apellidos=apellidos, email=email, contraseña=contraseña)
            usuario.save()
            formulario_registro = UserRegisterForm()
            return render(request, "AppRegistro/registro.html", {"mensaje": "Usuario creado"})
        else:
            return render(request, "AppRegistro/registro.html", {"mensaje": "Datos inválidos"})
    else:
        formulario_registro = UserRegisterForm()

    return render(request, "AppRegistro/registro.html", {"formulario": formulario_registro})


            

