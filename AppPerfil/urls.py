from django.urls import path
from .views import *
from AppPerfil import views


urlpatterns = [
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path("perfil/", views.perfil, name = "perfil"),
    path("avatar/", views.cargar_avatar, name="cargar_avatar"),
]
