from django.shortcuts import render
from chicuadrado.funcionesBondad import calculosPruebaBondad
from numerosaleatorios import views


# Create your views here.

generador = views.generador
valoresHistograma = views.generadorIntervalos
tablaChicuadrado = calculosPruebaBondad.tablaChicuadrado()

def opcionesBondades(request):
    if request.method == "GET":
        return render(request, 'opcionesbondades.html')





def pruebaChicuadrado(request):
    if request.method == "GET":
        tablaChicuadrado.setTamanoMuestra(generador.tamanomuestra)
        tablaChicuadrado.setDatosHistograma(valoresHistograma.intervalos)
        tablaChicuadrado.calcularFrecuenciaEsperada()

        tablaChicuadrado.datosTabla()


    return render(request, 'pruebaChicuadrado.html', {"datos":tablaChicuadrado})