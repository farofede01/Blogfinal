from django.urls import path
from . import views

urlpatterns = [
    path('mensajeria/', views.mensajeria, name='mensajeria'), 
]
