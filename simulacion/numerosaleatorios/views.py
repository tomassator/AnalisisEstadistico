from django.shortcuts import render, HttpResponse
from numerosaleatorios.funciones import generador


# Create your views here.

generador = generador.Generador()


def inicio(request):
    return render(request, "inicio.html")


def numerosAleatorios(request):
    if request.method == "GET":
        valorSemilla = request.GET["valorSemilla"]
        valorG = request.GET["valorG"]
        valorK = request.GET["valorK"]

        generador.setSemilla(valorSemilla)
        generador.setG(valorG)
        generador.setK(valorK)
        generador.calcularA()
        generador.calcularM()
        numerosAleatorios = generador.calcularRandom()
        return render(request, "numerosaleatorios.html", {"numerosAleatorios": numerosAleatorios})
