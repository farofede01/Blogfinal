from django.shortcuts import render

# Create your views here.

def acercademi (request):
    return render(request, "acercademi.html")

def pages (request):
    return render(request, "pages.html", {"mensaje": "Blog de Tecnologia"})
   

def inicio (request):
    return render(request, "inicio.html")


