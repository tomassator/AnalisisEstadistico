from django.shortcuts import render
from TP2.funcionesExcel import datosNbaEspn
# Create your views here.


def muestra1(request):

    datos_muestra = datosNbaEspn.stats_ginobili()
    return render(request, 'muestra1.html', {'datos_muestra':datos_muestra})