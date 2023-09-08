from django.urls import path
from .views import *
from AppPerfil import views


urlpatterns = [
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path("perfil/", perfil, name = "perfil"),
]


