class GeneradorIntervaloMuestra:
    '''Esta clase funciona igual que GeneradorIntervalo, esta cambiada para aceptar valores que 
    abarquen las muestras que no van necesariamente entre 0 y 1, tambien aplica para negativos'''
    intervalos = []
    frecuencias = []

    def determinarIntervalo(self, numintervalo, numerosAleatorios, tamanomuestra):
        self.frecuencias =[]
        self.intervalos = []
        self.frecuencias.extend([0] * int(numintervalo))

        li = 0
        ls = 0

        #lee todos los valores y encuentra el menor y mayor
        for num in numerosAleatorios:
            if num.valor < li:
                li = num.valor
            elif num.valor > ls:
                ls = num.valor
        
        #el incremento da el ancho de los intervalos
        inc = (ls + 0.1 - li) / int(numintervalo) # el 0.5 es para inacluir el valor maximo

        #luego cambia ls para que sea el limite del primer intervalo
        ls = li + inc

        frecuencia_acumulada = 0
        frecuencia_relativa_ac = 0

        #iteracion para el conteo de frecuencias
        for i in range(0, int(numintervalo)):
            if i != 0:
                li = ls
                ls += inc
            
            for num in numerosAleatorios:
                if num.valor >= li and num.valor < ls:
                    self.frecuencias[i] += 1

            frecuencia_acumulada += self.frecuencias[i]
            frecuencia_relativa_ac += (self.frecuencias[i]/int(tamanomuestra))

            self.intervalos.append((
                round(li,2),
                round(ls,2),
                round((li+ls)/2 , 4),
                self.frecuencias[i],
                round(self.frecuencias[i]/int(tamanomuestra),4),
                frecuencia_acumulada, round(frecuencia_relativa_ac, 4)))
        return self.intervalos