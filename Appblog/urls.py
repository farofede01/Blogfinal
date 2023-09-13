from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('aboutme/', acercademi, name = "acercademi"),
    path('pages/', views.pages, name="pages"),
    path ("", inicio, name="inicio"),
    path('crear_tema/', crear_tema, name='CrearTema'),
    path('editar_tema/<int:tema_id>/', views.editar_tema, name='editar_tema'),
    path('eliminar_tema/<int:tema_id>/', views.eliminar_tema, name='eliminar_tema'),
    path('lista_temas/', views.lista_temas, name='lista_temas'),
]
