

class Generador():
    semilla = None
    k = None
    g = None
    c = 7
    a = None
    m = None
    xi_siguiente = None

    def setK(self, k):
        self.k = int(k)


    def setG(self, g):
        self.g = int(g)

    def getSemilla(self):
        return self.semilla

    def setSemilla(self, semilla):
        self.semilla = int(semilla)
        self.setXi_siguiente(self.semilla)

    def setXi_siguiente(self, xi_siguiente):
        self.xi_siguiente = xi_siguiente


    def calcularA(self):
        self.a = 1 + 4 * self.k


    def calcularM(self):
        self.m = 2 ** self.g


    def calcularRandom(self):
        lista_numerosAleatorios = []
        for i in range(0,8):
            valor = (self.a*self.xi_siguiente) + self.c

            self.xi_siguiente = valor % self.m

            numeroRandom = self.xi_siguiente/ (self.m - 1)

            lista_numerosAleatorios.append(numeroRandom)

        return lista_numerosAleatorios




