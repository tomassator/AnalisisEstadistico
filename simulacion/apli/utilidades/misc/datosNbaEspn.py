import os
from openpyxl import load_workbook

def stats_ginobili():
    stats_manu = []    #Aca se guardan los datos que nos interesan
    anios = [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]  #Coincide con los nombres de las hojas del exel
    archivo = os.path.dirname(__file__) + r"\recursos\STATS_MANU.xlsx"
    excel = load_workbook(
        filename=archivo)  # Ruta del exel donde se extraen los datos

    partido=0

    for i in range(len(anios)):
        hoja_seleccionada = excel['{}'.format(anios[i])]
        resultado = hoja_seleccionada['C']
        fecha = hoja_seleccionada['A']
        minutos = hoja_seleccionada['D']
        puntos = hoja_seleccionada['Q']

        for x in range(len(puntos)):
            if (puntos[x].value and minutos[x].value and fecha[x].value) != None:
                try:             #Se hace este try para evitar datos como los titulos de las columnas
                    int(puntos[x].value)
                    partido += 1
                    stats_manu.append((partido, fecha[x].value + '/{}'.format(anios[i]), resultado[x].value, minutos[x].value, puntos[x].value, round((puntos[x].value/minutos[x].value),3)))
                except:
                    pass

    return stats_manu

if __name__ == "__main__":
    print(stats_ginobili())
