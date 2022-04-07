from django.shortcuts import render
from TP2.funcionesExcel import datosNbaEspn,datosBitcoin, histograma
from numerosaleatorios.funciones import intervalos, generador
from numerosaleatorios.funciones import intervalos_muestras
from chicuadrado.funcionesBondad import tablaChi, tablaKS
# Create your views here.


datos_histograma = histograma.Histograma()
datos_tablaChi = tablaChi.tablaChicuadrado()
datos_tablaKS = tablaKS.tablaks()
datos_muestra = datosNbaEspn.stats_ginobili()
def muestra1(request):

    datos_histograma.determinarIntervalo(20, datos_muestra, len(datos_muestra))


    return render(request, 'muestra1.html',
                  {'datos_muestra': datos_muestra, 'datos_histograma': datos_histograma.intervalos})

def pruebaChiTP2(request):
    datos_tablaChi.setDatosHistograma(datos_histograma.intervalos)
    datos_tablaChi.setDatosMuestra(datos_muestra)
    datos_tablaChi.setTamanoMuestra(len(datos_muestra))
    datos_tablaChi.calcularMedia()
    datos_tablaChi.calcularDesviacion()
    datos_tablaChi.datosTablaDNormal()
    datos_tablaChi.datosTablaDNormal2()
    resultado, chi_tab, grados_l = datos_tablaChi.resultadoPruebaChiNormal()
    return render(request, 'pruebaChiTP2.html', {"datosTabla":datos_tablaChi.datosTab, "datosTabla2":datos_tablaChi.datosTab2, "resultado":resultado
                                                 , "chi_tab":chi_tab, "gradoslibertad":grados_l})


def pruebaKSTP2(request):
    datos_tablaKS.setDatosHistograma(datos_histograma.intervalos)
    datos_tablaKS.setDatosMuestra(datos_muestra)
    datos_tablaKS.setTamanoMuestra(len(datos_muestra))
    datos_tablaKS.calcularMedia()
    datos_tablaKS.calcularDesviacion()
    datos_tablaKS.datosTablaKSNormal()

    resultado, ks_tab, grados_l = datos_tablaKS.resultadoPruebaKSNormal()

    return render(request, 'pruebaKSTP2.html', {"datosTabla":datos_tablaKS.datosTab, "resultado":resultado
                                                 , "chi_tab":ks_tab, "gradoslibertad":grados_l})













def muestra2(request):
    
    entradas = datosBitcoin.stats_bitcoin()
    datos = [entradas[i][1] for i in range(len(entradas))]
    
    generadorIntervalos = intervalos_muestras.GeneradorIntervaloMuestra()
    generadorIntervalos.determinarIntervalo(10,
    generador.Generador.transformarNrosDeEntradaAListaR(datos),
    len(datos))
    
    return render(request, 'muestra2.html', {'datos_muestra':entradas, "histograma": generadorIntervalos})