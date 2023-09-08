from django.urls import path
from .views import acercademi,pages, inicio

urlpatterns = [
    path('aboutme/', acercademi, name = "acercademi"),
    path('pages/', pages, name = "pages"),
    path ("inicio", inicio, name="inicio"),
]
