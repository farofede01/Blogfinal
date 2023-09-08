from django.urls import path
from .views import *
from AppRegistro import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
]  
