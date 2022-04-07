from django.shortcuts import render
from TP2.funcionesExcel import datosNbaEspn,datosBitcoin
# Create your views here.


def muestra1(request):

    datos_muestra = datosNbaEspn.stats_ginobili()
    return render(request, 'muestra1.html', {'datos_muestra':datos_muestra})


def muestra2(request):
    
    datos_muestra = datosBitcoin.stats_bitcoin()
    return render(request, 'muestra2.html', {'datos_muestra':datos_muestra})