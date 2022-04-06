from django.shortcuts import render
from chicuadrado.funcionesBondad import tablaChi, tablaKS
from numerosaleatorios import views


# Create your views here.

generador = views.generador
valoresHistograma = views.generadorIntervalos
tablaChicuadrado = tablaChi.tablaChicuadrado()
tablaK_S = tablaKS.tablaks()

def opcionesBondades(request):
    if request.method == "GET":
        return render(request, 'opcionesbondades.html')





def pruebaChicuadrado(request):
    if request.method == "GET":
        tablaChicuadrado.setTamanoMuestra(generador.tamanomuestra)
        tablaChicuadrado.setDatosHistograma(valoresHistograma.intervalos)
        tablaChicuadrado.calcularFrecuenciaEsperada()
        tablaChicuadrado.datosTabla()
        resultado = tablaChicuadrado.pruebaBondad()


    return render(request, 'pruebaChicuadrado.html', {"datos":tablaChicuadrado, "resultado":resultado})


def pruebaKS(request):
    if request.method == "GET":
        tablaK_S.setDatosHistograma(valoresHistograma.intervalos)
        tablaK_S.setTamanoMuestra(generador.tamanomuestra)
        tablaK_S.calcularFrecuenciaEsperada()
        tablaK_S.datosTabla()


    return render(request, 'pruebaKS.html', {"datos":tablaK_S})