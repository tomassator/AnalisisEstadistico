
from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.opciones),
    path('numerosAleatorios/', views.numerosAleatorios),
    path('cargaparametros/', views.cargaparametros),
    path('pruebaBondades/', views.opcionesBondades),
    path('pruebaChicuadrado/', views.pruebaChicuadrado),
    path('pruebaKS/', views.pruebaKS),
    path('seleccionarMuestra/', views.seleccionarMuestra),
    path('muestra1/', views.muestra1),
    path('muestra2/', views.muestra2),
    path('pruebaChiTP2/', views.pruebaChiTP2),
    path('pruebaKSTP2/', views.pruebaKSTP2)
]