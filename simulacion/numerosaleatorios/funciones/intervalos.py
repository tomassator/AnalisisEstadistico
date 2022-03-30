
class GeneradorIntervalos():

    intervalos = []
    frecuencias = []

    def determinarIntervalo(self, numintervalo, numerosAleatorios):
        self.frecuencias =[]
        self.intervalos = []
        self.frecuencias.extend([0] * int(numintervalo))

        li = 0
        ls = 1 / int(numintervalo)

        for i in range(0, int(numintervalo)):
            if i != 0:
                aux = ls
                li = ls
                ls = aux + (1 / int(numintervalo))
            for num in numerosAleatorios:
                if num.valor >= li and num.valor <= ls:
                    self.frecuencias[i] += 1
            self.intervalos.append((round(li,2), round(ls,2), self.frecuencias[i]))
        return self.intervalos
