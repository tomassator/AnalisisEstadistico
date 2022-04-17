
class Histograma():

    intervalos = []
    frecuencias = []

    def determinarIntervalo(self, numintervalo, datos, tamanomuestra):
        self.frecuencias =[]
        self.intervalos = []
        self.frecuencias.extend([0] * int(numintervalo))

        li = 0
        ls = 2/ int(numintervalo)
        frecuencia_acumulada = 0
        frecuencia_relativa_ac = 0
        for i in range(0, int(numintervalo)):
            if i != 0:
                aux = ls
                li = ls
                ls = aux + (2 / int(numintervalo))
            for p_m in datos:
                if (p_m[4]/p_m[3]) >= li and (p_m[4]/p_m[3]) < ls:
                    self.frecuencias[i] += 1

            frecuencia_acumulada += self.frecuencias[i]
            frecuencia_relativa_ac += (self.frecuencias[i]/int(tamanomuestra))


            #print(self.frecuencias[i] + fac_anterior)
            self.intervalos.append((round(li,2), round(ls,2), round((li+ls)/2 , 4) , self.frecuencias[i], round(self.frecuencias[i]/int(tamanomuestra),4),
                                    frecuencia_acumulada, round(frecuencia_relativa_ac, 4)))

    def determinarIntervaloM2(self , numintervalo, datos, tamanoMuestra):
        self.frecuencias = []
        self.intervalos = []
        self.frecuencias.extend([0] * int(numintervalo))

        li = 0
        ls = 0

        # lee todos los valores y encuentra el menor y mayor
        for num in datos:
            if num < li:
                li = num
            elif num > ls:
                ls = num

        # el incremento da el ancho de los intervalos
        inc = (ls + 0.1 - li) / int(numintervalo)  # el 0.5 es para inacluir el valor maximo

        # luego cambia ls para que sea el limite del primer intervalo
        ls = li + inc

        frecuencia_acumulada = 0
        frecuencia_relativa_ac = 0

        # iteracion para el conteo de frecuencias
        for i in range(0, int(numintervalo)):
            if i != 0:
                li = ls
                ls += inc

            for num in datos:
                if num >= li and num < ls:
                    self.frecuencias[i] += 1

            frecuencia_acumulada += self.frecuencias[i]
            frecuencia_relativa_ac += (self.frecuencias[i] / int(tamanoMuestra))

            self.intervalos.append((
                round(li, 2),
                round(ls, 2),
                round((li + ls) / 2, 4),
                self.frecuencias[i],
                round(self.frecuencias[i] / int(tamanoMuestra), 4),
                frecuencia_acumulada, round(frecuencia_relativa_ac, 4)))
        return self.intervalos
