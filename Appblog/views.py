from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .models import Tema
from .forms import crearTemaform

# Create your views here.

def acercademi (request):
    return render(request, "acercademi.html")

def pages(request):
    temas = Tema.objects.all()
    return render(request, "pages.html", {"mensaje": "Blog de Tecnologia", 'temas': temas})

def inicio (request):
    return render(request, "inicio.html")



@login_required
def crear_tema(request):
    if request.method == 'POST':
        form = crearTemaform(request.POST, request.FILES)
        if form.is_valid():
            tema = form.save(commit=False)
            tema.creador = request.user
            tema.save()
            return redirect('pages')
    else:
        form = crearTemaform()
    return render(request, 'crear_tema.html', {'form': form})



@login_required
def editar_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    if request.method == 'POST':
        form = crearTemaform(request.POST, request.FILES, instance=tema)
        if form.is_valid():
            form.save()
            return redirect('lista_temas')
    else:
        form = crearTemaform(instance=tema)

    return render(request, 'editartema.html', {'form': form, 'tema': tema})

@login_required
def eliminar_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    if request.method == 'POST':
        tema.delete()
        return redirect('lista_temas')

    return render(request, 'eliminartema.html', {'tema': tema})

def lista_temas(request):
    temas = Tema.objects.all()
    return render(request, 'lista_temas.html', {'temas': temas})
