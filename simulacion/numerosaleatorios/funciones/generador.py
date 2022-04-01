from numerosaleatorios.funciones import numeroRandom
import random

class Generador():
    semilla = None
    k = None
    g = None
    c = None
    a = None
    m = None
    tamanomuestra = None
    xi_siguiente = None

    def setK(self, k):
        self.k = float(k)

    def setC(self, c):
        self.c = float(c)

    def setG(self, g):
        self.g = float(g)

    def getSemilla(self):
        return self.semilla

    def setSemilla(self, semilla):
        self.semilla = float(semilla)
        self.setXi_siguiente(self.semilla)

    def setXi_siguiente(self, xi_siguiente):
        self.xi_siguiente = xi_siguiente

    def setTamanoMuestra(self, tamanomuestra):
        self.tamanomuestra = tamanomuestra

    def calcularA(self):
        self.a = 1 + 4 * self.k

    def calcularM(self):
        self.m = 2 ** self.g


    def calcularRandom(self):
        lista_numerosAleatorios = []
        for i in range(0, int(self.tamanomuestra)):
            valor = (self.a*self.xi_siguiente) + self.c

            self.xi_siguiente = valor % self.m

            numeroGenerado = self.xi_siguiente/ (self.m)

            numeroR = numeroRandom.NumeroR(i, self.xi_siguiente, numeroGenerado)
            lista_numerosAleatorios.append(numeroR)

        return lista_numerosAleatorios

    def calcularRandomGeneradorLenguaje(self):
        lista_numerosAleatorios = []

        for i in range(0,int(self.tamanomuestra)):
            numeroR = numeroRandom.NumeroR(i, "N/C",  random.random())
            lista_numerosAleatorios.append(numeroR)

        return lista_numerosAleatorios

'''   def calcularRandon(self):       # FUNCION DE PRUEBA
        lista_numeroAleatorio = []
        valores = [0.15, 0.22 ,0.41, 0.65,0.84, 0.81, 0.62, 0.45, 0.32, 0.07, 0.11, 0.29, 0.58,0.73,0.93,0.97,0.79,0.55,0.35,0.09,0.51,0.35,0.02,0.19,0.24,0.99, 0.98, 0.10, 0.31, 0.17]

        for i in range(0, 30):
            numeroR = numeroRandom.NumeroR(i, valores[i], valores[i])
            lista_numeroAleatorio.append(numeroR)

        return lista_numeroAleatorio '''






