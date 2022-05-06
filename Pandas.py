import csv

def strFloat(nmrStrig):
    nmString = nmrStrig.replace(","," ")
    nmrStrig = nmrStrig.strip()
    return float(nmrStrig)

with open("Cloud.csv") as archivo:
    lst_reader = csv.DictReader(archivo)
    lst_datos = list(lst_reader)

lstWBO = []

for pelicula in lst_datos:
    lstWBO.append([strFloat(pelicula["partida"])])

lstWBO.sort(reverse=True)

for pelicual in lst_datos:
    print(lstWBO)
