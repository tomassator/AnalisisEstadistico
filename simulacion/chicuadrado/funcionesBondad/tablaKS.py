

class tablaks():
    datosTab = []
    datosHistograma = None
    tamanoMuestra = None
    frecuencia_esperada = None


    def setDatosHistograma(self, data):
        self.datosHistograma = data

    def setTamanoMuestra(self, n):
        self.tamanoMuestra = n

    def calcularCantidadIntervalos(self):
        return int(len(self.datosHistograma))

    def calcularFrecuenciaEsperada(self ):
        self.frecuencia_esperada = (int(self.tamanoMuestra) / self.calcularCantidadIntervalos())

    def datosTabla(self):
        probac_fo = 0
        probac_fe = 0
        max_c = 0
        self.datosTab=[]
        for datosKS in self.datosHistograma:
            probac_fo += (datosKS[3]/int(self.tamanoMuestra))
            probac_fe += (self.frecuencia_esperada/int(self.tamanoMuestra))

            print(abs(probac_fo-probac_fe), max_c)
            if abs(probac_fo-probac_fe) > max_c:
                max_c = abs(probac_fo-probac_fe)

            self.datosTab.append((datosKS[0], datosKS[1], datosKS[3], round(self.frecuencia_esperada,4), (datosKS[3]/int(self.tamanoMuestra)),
                                  (self.frecuencia_esperada/int(self.tamanoMuestra)), round(probac_fo,4), round(probac_fe,4), abs(round(probac_fo-probac_fe,4)), round(max_c,4)))