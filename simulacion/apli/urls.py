
from django.urls import path
from . import views
from .utilidades import globales as g

app_name = 'apli'
urlpatterns = [

    #la pagina principal donde se hace todo
    path('', views.index),

    #el resto de las llamadas al servidor procesan peticiones,
    #devuelven valores o dan archivos html
    path('%s' % g.UNIFORME, views.formDUniforme),
    path('%s' % g.EXPONENCIAL, views.formDExponencial),
    path('%s' % g.NORMAL, views.formDNormal),
    path('%s' % g.POISSON, views.formDPoisson),

    path('%s' % g.URL_NRO_RESULTADOS, views.nro_resultados),
    path('%s' % g.URL_PRUEBA_RESULTADOS_CHI, views.prueba_resultados_chi),
    path('%s' % g.URL_PRUEBA_RESULTADOS_KS, views.prueba_resultados_ks)
    
]