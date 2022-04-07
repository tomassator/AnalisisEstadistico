import math

class tablaChicuadrado():
    datosMuestra = None
    datosHistograma = None
    frecuencia_esperada = None
    tamanoMuestra = None
    datosTab = []
    datosTab2 =[]
    m= 0 #UNICAMENTE PARA FRECUENCIAS UNIFORMES
    grados_libertad = None
    c_acumulado = None
    media = None
    varianza = None
    desviacion = None

    #METODOS QUE SE HICIERON PARA LA TABLA DE DISTRIBUCION NORMAL
    def calcularMedia(self):
        valores_acum = 0
        try:
            for valor in self.datosMuestra:
                valores_acum +=  valor[4]/valor[3]
        except:
            for valor in self.datosMuestra:
                valores_acum += valor[1]
        self.media = valores_acum / self.tamanoMuestra


    def calcularVarianza(self):
        sumatoria_cuadrada = 0

        try:
            for valor in self.datosMuestra:
                p_m = valor[4]/valor[3]
                sumatoria_cuadrada += (p_m - self.media)**2
        except:
            for valor in self.datosMuestra:
                p_m = valor[1]
                sumatoria_cuadrada += (p_m - self.media)**2
        self.varianza = (1/(self.tamanoMuestra-1)) * sumatoria_cuadrada

    def calcularDesviacion(self):
        self.calcularVarianza()
        self.desviacion = math.sqrt(self.varianza)


    def calcularFuncionProbabilidad(self , li , ls, marcaClase):
        frecuencia_esperada = ((1/(self.desviacion * math.sqrt(2*math.pi))) * math.exp(-0.5*(((marcaClase - self.media)/self.desviacion)**2))) * (ls-li)
        return frecuencia_esperada

    def datosTablaDNormal(self):
        self.datosTab = []
        for datosH in self.datosHistograma:
            li = datosH[0]
            ls = datosH[1]
            mc = datosH[2]
            fo = datosH[3]
            prob = self.calcularFuncionProbabilidad(datosH[0], datosH[1], datosH[2])
            fe = self.tamanoMuestra * prob
            self.datosTab.append((li, ls, mc, fo, prob, fe))

    def datosTablaDNormal2(self):
        self.datosTab2 = []
        self.c_acumulado = 0
        fe_acum = 0
        fo_acum = 0
        li_ultimo = None
        ls_ultimo = self.datosTab[len(self.datosTab)-1][1]
        bandera = False

        for datosTab1 in self.datosTab:
            fe = datosTab1[5]
            fo = datosTab1[3]
            fe_acum += fe
            fo_acum += fo

            print(fe_acum)
            if (fe > 5) and (bandera == False):
                li = datosTab1[0]
                ls = datosTab1[1]
                c = self.calcularC(fo, fe)
                self.c_acumulado += c
                self.datosTab2.append((li, ls, fo, fe, c , self.c_acumulado))
                fe_acum = 0
                fo_acum = 0

            elif fe_acum > 5:
                ls = datosTab1[1]
                print("hola")
                bandera = False
                self.c_acumulado += self.calcularC(fo_acum, fe_acum)
                self.datosTab2.append(
                    (li_ultimo, ls, fo_acum, fe_acum, self.calcularC(fo_acum, fe_acum), self.c_acumulado))
                fe_acum = 0
                fo_acum = 0

            elif bandera == False:
                bandera = True
                li_ultimo = datosTab1[0]

        if bandera == True:
            if fe_acum < 5:
                intervalo_anterior = self.datosTab2.pop()
                li_ultimo = intervalo_anterior[0]
                fo_acum_anterior = intervalo_anterior[2]
                fe_acum_anterior = intervalo_anterior[3]
                c_anterior = self.calcularC(fo_acum_anterior, fe_acum_anterior)

                fo_acum += fo_acum_anterior
                fe_acum += fe_acum_anterior
                self.c_acumulado += (self.calcularC(fo_acum, fe_acum)- c_anterior)

                self.datosTab2.append(
                    (li_ultimo, ls_ultimo, fo_acum, fe_acum, self.calcularC(fo_acum, fe_acum), self.c_acumulado))
            else:
                ls = ls_ultimo
                self.c_acumulado += self.calcularC(fo_acum, fe_acum)
                self.datosTab2.append(
                (li_ultimo, ls, fo_acum, fe_acum, self.calcularC(fo_acum, fe_acum), self.c_acumulado))





    def resultadoPruebaChiNormal(self):
        self.grados_libertad = len(self.datosTab2) - 1 - 2

        if self.grados_libertad == 9:
            if self.c_acumulado <= 16.9:
                return "NO SE RECHAZA LA HIPOTESIS", 16.9, self.grados_libertad
            else:
                return "SE RECHAZA LA HIPOTESIS", 16.9, self.grados_libertad
        if self.grados_libertad == 3:
            if self.c_acumulado <= 7.81:
                return "NO SE RECHAZA LA HIPOTESIS", 7.81, self.grados_libertad
            else:
                return "SE RECHAZA LA HIPOTESIS", 7.81, self.grados_libertad







#HASTA ACA

    def setTamanoMuestra(self, tm):
        self.tamanoMuestra = tm

    def setDatosMuestra(self, datos):
        self.datosMuestra = datos

    def setDatosHistograma(self, datosHistograma):
        self.datosHistograma = datosHistograma

    def calcularGradosLibertad(self):
        self.grados_libertad = self.calcularCantidadIntervalos() - 1 - self.m

    def calcularC(self, fo, fe):
        return (((fo-fe)**2)/fe)

    def calcularFrecuenciaEsperada(self ):
        self.frecuencia_esperada = (int(self.tamanoMuestra) / self.calcularCantidadIntervalos())


    def calcularCantidadIntervalos(self):
        return int(len(self.datosHistograma))

    def datosTabla(self):
        self.datosTab = []
        self.c_acumulado = 0
        for datosH in self.datosHistograma:
            self.c_acumulado += self.calcularC(datosH[3], self.frecuencia_esperada)
            self.datosTab.append((datosH[0],datosH[1], datosH[3], round(self.frecuencia_esperada,4), round(self.calcularC(datosH[3],self.frecuencia_esperada),4),
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
