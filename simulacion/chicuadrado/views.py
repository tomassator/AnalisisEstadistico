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
        print("AAAAAAAAA", generador.tamanomuestra)
        tablaChicuadrado.setTamanoMuestra(generador.tamanomuestra)
        tablaChicuadrado.setDatosHistograma(valoresHistograma.intervalos)
        tablaChicuadrado.calcularFrecuenciaEsperada()
        tablaChicuadrado.datosTabla()


    return render(request, 'pruebaChicuadrado.html', {"datos":tablaChicuadrado})


def pruebaKS(request):
    if request.method == "GET":
        tablaK_S.setDatosHistograma(valoresHistograma.intervalos)
        tablaK_S.setTamanoMuestra(generador.tamanomuestra)
        tablaK_S.calcularFrecuenciaEsperada()
        tablaK_S.datosTabla()


    return render(request, 'pruebaKS.html', {"datos":tablaK_S})