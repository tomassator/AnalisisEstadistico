from . import globales as g

class DistribucionProbabilidad:
    #TODO: implementar DistProb
    def __init__(self, params: dict) -> None:
        pass
    
    def crearValores():
        #TODO: implementar la generacion de valores
        pass
    
class DistribucionUniforme(DistribucionProbabilidad):
    #TODO: implementar DistUniform
    def __init__(self, params: dict) -> None:
        super().__init__(params)
        self._a = params[g.INPUT_A]
        self._b = params[g.INPUT_B]

class DistribucionExponencial(DistribucionProbabilidad):
    #TODO: implementar DistExp
    def __init__(self, params: dict) -> None:
        super().__init__(params)
        self._media = params[g.INPUT_MEDIA]
        self._lambda = 1 / self._media

class DistribucionNormal(DistribucionProbabilidad):
    #TODO: implementar DistNormal
    def __init__(self, params: dict) -> None:
        super().__init__(params)
        self._varianza = params[g.INPUT_VARIANZA]
        self._desviacion = params[g.INPUT_DESVIACION]

class DistribucionPoisson(DistribucionProbabilidad):
    #TODO: implementar DistPoisson
    def __init__(self, params: dict) -> None:
        super().__init__(params)
        self._media = params[g.INPUT_MEDIA]
        self._lambda = self._media

DISTs = {
    '%s' % g.UNIFORME : DistribucionUniforme,
    '%s' % g.EXPONENCIAL : DistribucionExponencial,
    '%s' % g.NORMAL : DistribucionNormal,
    '%s' % g.POISSON : DistribucionPoisson
}