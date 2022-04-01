from django.shortcuts import render, HttpResponse
from numerosaleatorios.funciones import generador, intervalos



# Create your views here.
a = 1
generador = generador.Generador()
generadorIntervalos = intervalos.GeneradorIntervalos()


def cargaparametros(request):
    return render(request, "cargaparametros.html")


def numerosAleatorios(request):
    if request.method == "GET":
        valorSemilla = request.GET["valorSemilla"]
        valorG = request.GET["valorG"]
        valorK = request.GET["valorK"]
        valorC = request.GET["valorC"]
        tamanoMuestra = request.GET["tamañoMuestra"]
        numintervalos = request.GET["valorIntervalos"]


        generador.setSemilla(valorSemilla)
        generador.setG(valorG)
        generador.setK(valorK)
        generador.setC(valorC)
        generador.setTamanoMuestra(tamanoMuestra)
        generador.calcularA()
        generador.calcularM()
        numerosAleatorios = generador.calcularRandom()
        generadorIntervalos.determinarIntervalo(numintervalos , numerosAleatorios, tamanoMuestra)
        return render(request, "numerosaleatorios.html",
                      {"numerosAleatorios": numerosAleatorios, "histograma": generadorIntervalos})

    if request.method == "POST":
        tamanoMuestra = request.POST["tamañoMuestraGL"]
        numintervalos = request.POST["valorIntervalosGL"]
        generador.setTamanoMuestra(tamanoMuestra)
        numerosAleatorios = generador.calcularRandomGeneradorLenguaje()


        generadorIntervalos.determinarIntervalo(numintervalos,numerosAleatorios, tamanoMuestra )
        return render(request, "numerosaleatorios.html", {"numerosAleatorios": numerosAleatorios, "histograma":generadorIntervalos})



