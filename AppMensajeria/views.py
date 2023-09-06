from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import FormularioMensaje

def chat(request):
    mensajes = Mensaje.objects.all()
    formulario = FormularioMensaje()

    if request.method == 'POST':
        formulario = FormularioMensaje(request.POST)
        if formulario.is_valid():
            nuevo_mensaje = formulario.save(commit=False)
            nuevo_mensaje.remitente = request.user
            nuevo_mensaje.save()
            return redirect('chat')  # Redirige a la página de chat

    return render(request, 'chat.html', {'mensajes': mensajes, 'formulario': formulario})



    