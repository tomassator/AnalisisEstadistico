import math

class tablaks():
    datosTab = []
    datosMuestra = []
    datosHistograma = None
    tamanoMuestra = None
    frecuencia_esperada = None
    max_c = None

    #METODOS PARA LA DISTRIBUCION NORMAL
    def calcularMedia(self):
        valores_acum = 0
        try:
            for valor in self.datosMuestra:
                valores_acum += valor[4] / valor[3]
        except:
            for valor in self.datosMuestra:
                valores_acum += valor[1]
        self.media = valores_acum / self.tamanoMuestra

    def setDatosMuestra(self, datos):
        self.datosMuestra = datos

    def calcularVarianza(self):
        sumatoria_cuadrada = 0

        try:
            for valor in self.datosMuestra:
                p_m = valor[4] / valor[3]
                sumatoria_cuadrada += (p_m - self.media) ** 2
        except:
            for valor in self.datosMuestra:
                p_m = valor[1]
                sumatoria_cuadrada += (p_m - self.media) ** 2
        self.varianza = (1 / (self.tamanoMuestra - 1)) * sumatoria_cuadrada

    def calcularDesviacion(self):
        self.calcularVarianza()
        self.desviacion = math.sqrt(self.varianza)

    def calcularFuncionProbabilidad(self , li , ls, marcaClase):
        frecuencia_esperada = ((1/(self.desviacion * math.sqrt(2*math.pi))) * math.exp(-0.5*(((marcaClase - self.media)/self.desviacion)**2))) * (ls-li)
        return frecuencia_esperada

    def datosTablaKSNormal(self):
        self.datosTab = []
        prob_esperada_acum = 0
        prob_observada_acum = 0
        self.max_c = 0
        for datosH in self.datosHistograma:
            li = datosH[0]
            ls = datosH[1]
            mc = datosH[2]
            fo = datosH[3]
            prob_esperada = self.calcularFuncionProbabilidad(li, ls ,mc)
            fe = self.tamanoMuestra * prob_esperada
            prob_observada = fo/ self.tamanoMuestra
            prob_esperada_acum += prob_esperada
            prob_observada_acum += prob_observada

            diferencia= abs(prob_observada_acum - prob_esperada_acum)


            #CALCULO DEL MAXIMO C
            if diferencia > self.max_c:
               self.max_c = diferencia

            self.datosTab.append((li, ls, fo, round(fe,4), round(prob_observada,4),
                                  round(prob_esperada,4), round(prob_observada_acum,4),
                                  round(prob_esperada_acum,4), round(diferencia,4),round(self.max_c,4) ))

    def resultadoPruebaKSNormal(self):
        self.grados_libertad = self.tamanoMuestra

        if self.grados_libertad > 35:
            if self.max_c <= (1.36/(math.sqrt(self.tamanoMuestra))):
                return "NO SE RECHAZA LA HIPOTESIS", 1.36/(math.sqrt(self.tamanoMuestra)), self.grados_libertad
            else:
                return "SE RECHAZA LA HIPOTESIS", 1.36/(math.sqrt(self.tamanoMuestra)), self.grados_libertad













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
            if abs(probac_fo-probac_fe) > max_c:
                max_c = abs(probac_fo-probac_fe)

            self.datosTab.append((datosKS[0], datosKS[1], datosKS[3], round(self.frecuencia_esperada,4), round((datosKS[3]/int(self.tamanoMuestra)),4),
                                  round(self.frecuencia_esperada/int(self.tamanoMuestra),4), round(probac_fo,4), round(probac_fe,4), abs(round(probac_fo-probac_fe,4)), round(max_c,4)))