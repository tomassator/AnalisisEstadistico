"""simulacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
#from chicuadrado.views import opcionesBondades, pruebaChicuadrado, pruebaKS
#from numerosaleatorios.views import numerosAleatorios, cargaparametros
#from menu.views import opciones, seleccionarMuestra
#from TP2.views import muestra1, muestra2,pruebaChiTP2, pruebaKSTP2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
    #path('', opciones),
    #path('numerosAleatorios/', numerosAleatorios),
    #path('cargaparametros/', cargaparametros),
    #path('pruebaBondades/', opcionesBondades),
    #path('pruebaChicuadrado/', pruebaChicuadrado),
    #path('pruebaKS/', pruebaKS),
    #path('seleccionarMuestra/', seleccionarMuestra),
    #path('muestra1/', muestra1),
    #path('muestra2/', muestra2),
    #path('pruebaChiTP2/', pruebaChiTP2),
    #path('pruebaKSTP2/', pruebaKSTP2),
]
