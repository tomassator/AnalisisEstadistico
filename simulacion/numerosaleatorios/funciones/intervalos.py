
class GeneradorIntervalos():

    intervalo = []


    def intervalocinco(self, numerosAleatorios):
        self.intervalo= []

        self.intervalo.extend([0,0,0,0,0])

        for num in numerosAleatorios:
            if float(num.valor) <= 0.2:
                self.intervalo[0] += 1
            elif float(num.valor) <= 0.4:
                self.intervalo[1] += 1
            elif float(num.valor) <= 0.6:
                self.intervalo[2] += 1
            elif float(num.valor) <= 0.8:
                self.intervalo[3] += 1
            elif float(num.valor) <= 1:
                self.intervalo[4] += 1

        return self.intervalo
