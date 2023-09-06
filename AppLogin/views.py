from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm (request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get ("username")
            contraseña = form.cleaned_data.get ("password")

            user = authenticate (username = usuario, password = contraseña)

            if user is not None:
                login (request, user)

                return render (request, "AppLogin/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render (request, "AppLogin/inicio.html", {"mensaje":"Error, datos incorrectos"})
            
        else :
            return render (request, "AppLogin/inicio.html", {"mensaje": "Error, formulario erroneo"})
    
    form = AuthenticationForm()

    return render (request, "Final/inicio.html", {"form" : form})

@login_required
def inicio (request):
    return render (request, "AppLogin/login.html" )

