from django.shortcuts import render
from TP2.funcionesExcel import datosNbaEspn,datosBitcoin
from numerosaleatorios.funciones import intervalos, generador
from numerosaleatorios.funciones import intervalos_muestras
# Create your views here.


def muestra1(request):

    datos_muestra = datosNbaEspn.stats_ginobili()
    return render(request, 'muestra1.html', {'datos_muestra':datos_muestra})


def muestra2(request):
    
    entradas = datosBitcoin.stats_bitcoin()
    datos = [entradas[i][1] for i in range(len(entradas))]
    
    generadorIntervalos = intervalos_muestras.GeneradorIntervaloMuestra()
    generadorIntervalos.determinarIntervalo(10,
    generador.Generador.transformarNrosDeEntradaAListaR(datos),
    len(datos))
    
    return render(request, 'muestra2.html', {'datos_muestra':entradas, "histograma": generadorIntervalos})