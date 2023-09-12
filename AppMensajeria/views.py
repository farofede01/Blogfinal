from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import FormularioMensaje
from django.urls import reverse 
def mensajeria (request):
    mensajes = Mensaje.objects.all()
    formulario = FormularioMensaje()
    if request.method == 'POST':
        formulario = FormularioMensaje(request.POST)
        if formulario.is_valid():
            nuevo_mensaje = formulario.save(commit=False)
            nuevo_mensaje.remitente = request.user
            nuevo_mensaje.save()
            return redirect(reverse('mensajeria'))

    return render(request, "AppMensajeria/mensajeria.html", {'mensajes': mensajes, 'formulario': formulario})




    