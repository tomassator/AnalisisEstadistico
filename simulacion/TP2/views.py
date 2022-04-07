from django.shortcuts import render
from TP2.funcionesExcel import datosNbaEspn,datosBitcoin, histograma
from numerosaleatorios.funciones import intervalos, generador
from numerosaleatorios.funciones import intervalos_muestras
from chicuadrado.funcionesBondad import tablaChi
# Create your views here.


datos_histograma = histograma.Histograma()
datos_tablaChi = tablaChi.tablaChicuadrado()

def muestra1(request):
    datos_muestra = datosNbaEspn.stats_ginobili()

    datos_histograma.determinarIntervalo(20, datos_muestra, len(datos_muestra))

    datos_tablaChi.setDatosHistograma(datos_histograma.intervalos)
    datos_tablaChi.setDatosMuestra(datos_muestra)
    datos_tablaChi.setTamanoMuestra(len(datos_muestra))
    datos_tablaChi.calcularMedia()
    datos_tablaChi.calcularDesviacion()
    datos_tablaChi.datosTablaDNormal()
    datos_tablaChi.datosTablaDNormal2()

    return render(request, 'muestra1.html',
                  {'datos_muestra': datos_muestra, 'datos_histograma': datos_histograma.intervalos})

def pruebaChiTP2(request):
    return render(request, 'pruebaChiTP2.html', {"datosTabla":datos_tablaChi.datosTab, "datosTabla2":datos_tablaChi.datosTab2})


def muestra2(request):
    
    entradas = datosBitcoin.stats_bitcoin()
    datos = [entradas[i][1] for i in range(len(entradas))]
    
    generadorIntervalos = intervalos_muestras.GeneradorIntervaloMuestra()
    generadorIntervalos.determinarIntervalo(10,
    generador.Generador.transformarNrosDeEntradaAListaR(datos),
    len(datos))
    
    return render(request, 'muestra2.html', {'datos_muestra':entradas, "histograma": generadorIntervalos})