class tablaChicuadrado():
    datosHistograma = None
    frecuencia_esperada = None
    tamanoMuestra = None
    datosTab = []
    m= 0 #UNICAMENTE PARA FRECUENCIAS UNIFORMES
    grados_libertad = None
    c_acumulado = None


    def setTamanoMuestra(self, tm):
        self.tamanoMuestra = tm


    def setDatosHistograma(self, datosHistograma):
        self.datosHistograma = datosHistograma

    def calcularGradosLibertad(self):
        self.grados_libertad = self.calcularCantidadIntervalos() - 1 - self.m

    def calcularC(self, fo):
        return (((fo-self.frecuencia_esperada)**2)/self.frecuencia_esperada)

    def calcularFrecuenciaEsperada(self ):
        self.frecuencia_esperada = (int(self.tamanoMuestra) / self.calcularCantidadIntervalos())


    def calcularCantidadIntervalos(self):
        return int(len(self.datosHistograma))

    def datosTabla(self):
        self.datosTab = []
        self.c_acumulado = 0
        for datosH in self.datosHistograma:
            self.c_acumulado += self.calcularC(datosH[3])
            self.datosTab.append((datosH[0],datosH[1], datosH[3], round(self.frecuencia_esperada,4), round(self.calcularC(datosH[3]),4),
                                  round(self.c_acumulado,4)))

    def pruebaBondad(self):
        self.calcularGradosLibertad()
        if self.grados_libertad == 4:
            if self.c_acumulado <= 9.49:
                return "NO SE RECHAZA LA HIPOTESIS"
            else:
                return "SE RECHAZA LA HIPOTESIS"
        elif self.grados_libertad == 7:
            if self.c_acumulado <= 14.1:
                return "NO SE RECHAZA LA HIPOTESIS"
            else:
                return "SE RECHAZA LA HIPOTESIS"
        elif self.grados_libertad == 9:
            if self.c_acumulado <= 16.9:
                return "NO SE RECHAZA LA HIPOTESIS"
            else:
                return "SE RECHAZA LA HIPOTESIS"
        elif self.grados_libertad == 11:
            if self.c_acumulado <= 19.7:
                return "NO SE RECHAZA LA HIPOTESIS"
            else:
                return "SE RECHAZA LA HIPOTESIS"
