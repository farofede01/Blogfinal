from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm
from .models import *
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

#@login_required
#def inicio (request):
#    avatares = Avatar.objects.filter(user = request.user.id)
#    return render (request, "inicio.html", {"url": avatares[0].imagen.url})
#def inicio(request):
#    avatares = Avatar.objects.filter(user=request.user.id)
#    if avatares.exists():
#        avatar_url = avatares[0].imagen.url
#    else:
#        avatar_url = None
#
#    return render(request, "inicio.html", {"url": avatar_url})
