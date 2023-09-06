from django.urls import path
from .views import *
from AppRegistro import views

urlpatterns = [
    path("formulario", formulario)
]  
