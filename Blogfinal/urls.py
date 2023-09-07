"""
URL configuration for Blogfinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from AppLogin.views import *
from AppMensajeria.views import *
from AppPerfil.views import *
from AppRegistro.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="inicio"),
    path("AppLogin/", include("AppLogin.urls")),
    path("AppMensajeria/", include("AppMensajeria.urls")),
    path("AppPerfil/", include("AppPerfil.urls")),
    path("AppRegistro/", include("AppRegistro.urls")),
]


# Para las imagenes:


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
