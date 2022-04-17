from django.http import HttpRequest
from django.shortcuts import render
from .utilidades import globales as g

#carga la aplicacion
def index(request):
    return render(request, 'index.html', { 
        "selecDist": g.SELEC_DISTRIBUCION,
        "selecInter": g.SELEC_INTERVALOS,
        "selecPrueba": g.SELEC_PRUEBA,
        "distribuciones": g.DISTRIBUCIONES.items(),
        "intervalos": g.INTERVALOS.items(),
        "pruebas": g.PRUEBAS.items(),
        "url_nros": g.URL_NRO_RESULTADOS,
        "url_pruebas": g.URL_NRO_RESULTADOS
        })

#esta parte crear los html de las distintas opciones segun el tipo de distribucion
def formDUniforme(request):
    return render(request, 'form-DUniforme.html', {
        "inputA": g.INPUT_A,
        "inputB": g.INPUT_B
    })

def formDExponencial(request):
    return render(request, 'form-DExponencial.html', {
        "inputMedia": g.INPUT_MEDIA
    })

def formDNormal(request):
    return render(request, 'form-DNormal.html', {
        "selecMetodo": g.SELEC_METODO_NORMAL,
        "inputMedia": g.INPUT_MEDIA,
        "inputDesviacion": g.INPUT_DESVIACION,
        "metodos": g.METODOS_NORMAL.items()
    })

def formDPoisson(request):
    return render(request, 'form-DPoisson.html', {
        "inputMedia": g.INPUT_MEDIA
    })


#manejo del los parametros para calcular los valores
def nro_resultados(request: HttpRequest):
    #TODO: terminar
    from .utilidades.vars_aleatorias import DISTs
    dist_elegida = DISTs[request.POST[g.SELEC_DISTRIBUCION]]
    resultados = dist_elegida.calc_valores(int(g.INTERVALOS[request.POST[g.SELEC_INTERVALOS]]))
    return render(request, 'nros-resultados.html', {
        "resultados": resultados
    })


#manejo del calculo de cada prueba de bondad
def prueba_resultados_chi(request):
    return render(request, "prueba-resultados-chi.html", {})

def prueba_resultados_ks(request):
    return render(request, "prueba-resultados-ks.html", {})
