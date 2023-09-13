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
            # Usamos set_password para establecer la nueva contraseña
            usuario.set_password(informacion['password1'])
            usuario.save()

            return render(request, "inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario})

@login_required
def perfil(request):
    perfil_usuario, created = UserProfile.objects.get_or_create(
        user=request.user)
    return render(request, 'perfil.html', {'perfil_usuario': perfil_usuario,  "profile_form": AvatarUpdateForm()})


def cargar_avatar(request):
    if request.method == 'POST':
        profile_form = AvatarUpdateForm(
            request.POST, request.FILES)

        if profile_form.is_valid():
            avatar_anterior = Avatar.objects.filter(user=request.user)
            if (len(avatar_anterior) > 0):
                avatar_anterior.delete()
            avatar_nuevo = Avatar(
                user=request.user, profile_image=profile_form.cleaned_data["profile_image"])
            avatar_nuevo.save()
            # profile_form.save()
            return redirect('inicio')
    else:
        profile_form = AvatarUpdateForm()
    return render(request, 'Appblog/inicio.html', {'profile_form': profile_form})

