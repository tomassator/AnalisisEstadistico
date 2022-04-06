from django.shortcuts import render
from TP2.funcionesExcel import datosNbaEspn, histograma
# Create your views here.

datos_histograma = histograma.Histograma()

def muestra1(request):
    datos_muestra = datosNbaEspn.stats_ginobili()

    datos_histograma.determinarIntervalo(15, datos_muestra, len(datos_muestra))

    return render(request, 'muestra1.html', {'datos_muestra':datos_muestra, 'datos_histograma':datos_histograma.intervalos})