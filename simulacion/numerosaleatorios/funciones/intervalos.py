
class GeneradorIntervalos():

    intervalos = []
    frecuencias = []

    def determinarIntervalo(self, numintervalo, numerosAleatorios, tamanomuestra):
        self.frecuencias =[]
        self.intervalos = []
        self.frecuencias.extend([0] * int(numintervalo))

        li = 0
        ls = 1 / int(numintervalo)
        frecuencia_acumulada = 0
        frecuencia_relativa_ac = 0
        for i in range(0, int(numintervalo)):
            if i != 0:
                aux = ls
                li = ls
                ls = aux + (1 / int(numintervalo))
            for num in numerosAleatorios:
                print(num.valor)
                if num.valor >= li and num.valor < ls:
                    self.frecuencias[i] += 1

            frecuencia_acumulada += self.frecuencias[i]
            frecuencia_relativa_ac += (self.frecuencias[i]/int(tamanomuestra))


            #print(self.frecuencias[i] + fac_anterior)
            self.intervalos.append((round(li,2), round(ls,2), round((li+ls)/2 , 4) , self.frecuencias[i], self.frecuencias[i]/int(tamanomuestra),
                                    frecuencia_acumulada, round(frecuencia_relativa_ac, 4)))
        return self.intervalos
