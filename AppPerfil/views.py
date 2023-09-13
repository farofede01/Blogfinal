from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, AvatarUpdateForm
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

            return render(request, "Appblog/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario})

def cargar_avatar(request):
    if request.method == 'POST':
        profile_form = AvatarUpdateForm(request.POST, request.FILES, instance=request.user.avatar)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('inicio')
    else:
        profile_form = AvatarUpdateForm(instance=request.user.avatar)
    return render(request, 'Appblog/inicio.html', {'profile_form': profile_form})


@login_required
def perfil(request):
    perfil_usuario, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'perfil.html', {'perfil_usuario': perfil_usuario})
