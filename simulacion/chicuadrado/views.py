from django.shortcuts import render

# Create your views here.


def opcionesBondades(request, valores):



    return render(request, 'opcionesbondades.html')



def pruebaChicuadrado(request):

    return render(request, 'pruebaChicuadrado.html')