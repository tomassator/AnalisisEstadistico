class tablaChicuadrado():
    datosHistograma = None
    frecuencia_esperada = None
    tamanoMuestra = None
    datosTab = []

    def setTamanoMuestra(self, tm):
        self.tamanoMuestra = tm


    def setDatosHistograma(self, datosHistograma):
        self.datosHistograma = datosHistograma

    def calcularC(self, fo):
        return (((fo-self.frecuencia_esperada)**2)/self.frecuencia_esperada)

    def calcularFrecuenciaEsperada(self ):
        print(self.tamanoMuestra, self.calcularCantidadIntervalos())
        self.frecuencia_esperada = (int(self.tamanoMuestra) / self.calcularCantidadIntervalos())


    def calcularCantidadIntervalos(self):
        return int(len(self.datosHistograma))

    def datosTabla(self):
        self.datosTab = []
        c_acumulado = 0
        for datosH in self.datosHistograma:
            c_acumulado += self.calcularC(datosH[3])
            print(datosH)
            print(datosH[0] , " - ", datosH[1])
            self.datosTab.append((datosH[0],datosH[1], datosH[3], round(self.frecuencia_esperada,4), round(self.calcularC(datosH[3]),4), c_acumulado))


