from django.shortcuts import render, redirect
from AppRegistro.models import *
from django.http import HttpResponse
from .forms import *
from .forms import UserRegisterForm

# Create your views here.
"""def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre_usuario = info["username"]  
            email = info["email"]
            contraseña = info["password1"]  
            usuario = Usuario(nombre_usuario=nombre_usuario, email=email, contraseña=contraseña)
            usuario.save()
            formulario_registro = UserRegisterForm()
            return render(request, "AppRegistro.html", {"mensaje": "Usuario creado"})
        else:
            return render(request, "AppRegistro/registro.html", {"mensaje": "Datos inválidos"})
    else:
        formulario_registro = UserRegisterForm()

    return render(request, "AppRegistro/registro.html", {"formulario": formulario_registro})
"""
def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre_usuario = info["username"]
            email = info["email"]
            contraseña = info["password1"]  # Campo correcto para la contraseña
            #form = Usuario(nombre_usuario=nombre_usuario, email=email, contraseña=contraseña)
            form.save()
            return render(request, 'inicio.html')  # Redirigir al usuario después del registro exitoso
        else:
            form = UserRegisterForm()
            return render(request, "AppRegistro/registro.html", {"form": form, "mensaje": "Datos inválidos"})
    else:
        form = UserRegisterForm()

    return render(request, "AppRegistro/registro.html", {"form": form})
