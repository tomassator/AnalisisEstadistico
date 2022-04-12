from django.shortcuts import render

from django.shortcuts import render, HttpResponse
from .utilidades import tablaChi, tablaKS, generador, intervalos
#from numerosaleatorios import views
#from utilidades import generador, intervalos



# variables de numerosaleatorios que movi aca para que ande
a = 1
generador = generador.Generador()
generadorIntervalos = intervalos.GeneradorIntervalos()
# --------------------------------------------------------

# Views de ChiCuadrado
generador = generador
valoresHistograma = generadorIntervalos
tablaChicuadrado = tablaChi.tablaChicuadrado()
tablaK_S = tablaKS.tablaks()

def opcionesBondades(request):
    if request.method == "GET":
        return render(request, 'opcionesbondades.html')

def pruebaChicuadrado(request):
    if request.method == "GET":
        tablaChicuadrado.setTamanoMuestra(generador.tamanomuestra)
        tablaChicuadrado.setDatosHistograma(valoresHistograma.intervalos)
        tablaChicuadrado.calcularFrecuenciaEsperada()
        tablaChicuadrado.datosTabla()
        resultado = tablaChicuadrado.pruebaBondad()


    return render(request, 'pruebaChicuadrado.html', {"datos":tablaChicuadrado, "resultado":resultado})


def pruebaKS(request):
    if request.method == "GET":
        tablaK_S.setDatosHistograma(valoresHistograma.intervalos)
        tablaK_S.setTamanoMuestra(generador.tamanomuestra)
        tablaK_S.calcularFrecuenciaEsperada()
        tablaK_S.datosTabla()


    return render(request, 'pruebaKS.html', {"datos":tablaK_S})



#views del menu
def opciones(request):
    return render(request, 'opciones.html')


def seleccionarMuestra(request):
    return render(request, 'seleccionarMuestra.html')


# views de numerosaleatorios

#aca iban las variables de numerosaleatorios
#-------------------------------------------

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


# views del tp2 
from django.shortcuts import render
from TP2.funcionesExcel import datosNbaEspn,datosBitcoin, histograma
from numerosaleatorios.funciones import intervalos, generador
from numerosaleatorios.funciones import intervalos_muestras
from chicuadrado.funcionesBondad import tablaChi, tablaKS
# Create your views here.


datos_histograma = histograma.Histograma()
datos_tablaChi = tablaChi.tablaChicuadrado()
datos_tablaKS = tablaKS.tablaks()
datos_muestra = None



def muestra1(request):
    global datos_muestra
    datos_muestra = datosNbaEspn.stats_ginobili()
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





'''def muestra2(request):
    
    entradas = datosBitcoin.stats_bitcoin()
    datos = [entradas[i][1] for i in range(len(entradas))]
    
    generadorIntervalos = intervalos_muestras.GeneradorIntervaloMuestra()
    generadorIntervalos.determinarIntervalo(10,
    generador.Generador.transformarNrosDeEntradaAListaR(datos),
    len(datos))

    print(generadorIntervalos.intervalos)
    
    return render(request, 'muestra2.html', {'datos_muestra':entradas, "histograma": generadorIntervalos})
'''

def muestra2(request):
    global datos_muestra
    datos_muestra = datosBitcoin.stats_bitcoin()
    datos = [datos_muestra[i][1] for i in range(len(datos_muestra))]

    datos_histograma.determinarIntervaloM2(10, datos, len(datos))



    return render(request, 'muestra2.html', {'datos_muestra': datos_muestra, "histograma": datos_histograma})
