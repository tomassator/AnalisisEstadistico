'''Clases para calcular los tipos de distribuciones'''
from . import globales as g
import random as r
import math as m

class DistribucionProbabilidad:
    '''Clase abstracta, no se instancia ni se usa mas alla de este archivo'''

    def __init__(self, params: dict) -> None:
        self._valores = []
    
    def calc_valores(self, cant: int):
        '''retorna la lista de RNDs de la distribucion, tambien los guarda en el objeto'''
        return self._valores

    def get_valores(self):
        '''solo devuelve los valores calculados'''
        return self._valores
    
class DistribucionUniforme(DistribucionProbabilidad):
    def __init__(self, params: dict) -> None:
        super().__init__(params)
        self._a = params[g.INPUT_A]
        self._b = params[g.INPUT_B]
    
    def calc_valores(self, cant: int):
        for it in range(cant):
            rnd = r.random()
            calc = self._a + rnd * (self._b - self._a)
            self._valores.append(calc)
        
        return self._valores

class DistribucionExponencial(DistribucionProbabilidad):
    def __init__(self, params: dict) -> None:
        super().__init__(params)
        self._media = params[g.INPUT_MEDIA]
        self._lambda = 1 / self._media

    def calc_valores(self, cant: int):
        for it in range(cant):
            rnd = r.random()
            calc = (-1 / self._lambda) * m.log(1 - rnd)
            self._valores.append(calc)
        
        return self._valores

class DistribucionNormal(DistribucionProbabilidad):
    def __init__(self, params: dict) -> None:
        super().__init__(params)
        self._media = params[g.INPUT_MEDIA]
        self._desviacion = params[g.INPUT_DESVIACION]
        self._metodo_elegido = {
            g.MET_BOX_MULLER: self._iteracion_box_muller,
            g.MET_CONV: self._iteracion_convolucion}.get(params[g.SELEC_METODO_NORMAL])

        # valores adicionales para manejar box muller 
        self._primer_valor_de_calc = True
        self._cache_n = 0

    def _iteracion_box_muller(self):
        '''hace el calculo por metodo box-muller'''
        if not self._primer_valor_de_calc:
            self._primer_valor_de_calc = True
            return self._cache_n

        rnd1 = r.random()
        rnd2 = r.random()
        n1 = (m.sqrt(-2 * m.log(rnd1)) * m.cos(2 * m.pi * rnd2)) * self._desviacion + self._media
        n2 = (m.sqrt(-2 * m.log(rnd1)) * m.sin(2 * m.pi * rnd2)) * self._desviacion + self._media

        self._cache_n = n2
        self._primer_valor_de_calc = False

        return n1


    def _iteracion_convolucion(self):
        '''hace el calculo por metodo convolucion'''
        suma_rnds = 0
        for i in range(12):
            rnds += r.random()
        calc = (suma_rnds - 6) * self._desviacion +self._media
        return calc
        

    def calc_valores(self, cant: int):
        for it in range(cant):
            calc = self._metodo_elegido()
            self._valores.append(calc)
        
        return self._valores

class DistribucionPoisson(DistribucionProbabilidad):
    def __init__(self, params: dict) -> None:
        super().__init__(params)
        self._media = params[g.INPUT_MEDIA]
        self._lambda = self._media
    
    def _iteracion_poisson(self):
        '''algoritmo de poisson'''
        p = 1
        x = -1
        a = m.exp(- self._lambda)
        while p >= a:
            u = r.random()
            p = p * u
            x += 1
        
        return x

    def calc_valores(self, cant: int):
        for it in range(cant):
            calc = self._iteracion_poisson()
            self._valores.append(calc)
        
        return self._valores

DISTs = {
    '%s' % g.UNIFORME : DistribucionUniforme,
    '%s' % g.EXPONENCIAL : DistribucionExponencial,
    '%s' % g.NORMAL : DistribucionNormal,
    '%s' % g.POISSON : DistribucionPoisson
}