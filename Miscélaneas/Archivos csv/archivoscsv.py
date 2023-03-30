from Ganadores import *
import csv
listaganadores=[]
with open("C:\\Users\\catalina\\Desktop\\Python\\Miscélaneas\\Archivos csv\\Oscares.csv","r") as file:
    r=csv.reader(file)
    for row in r:
        m=Ganadores(row[0],row[1],row[2],row[3],row[4])
        listaganadores.append(m)
with open("C:\\Users\\catalina\\Desktop\\Python\\Miscélaneas\\Archivos csv\\Oscaresm.csv","r") as archivo:
    l=csv.reader(archivo)
    for columna in l:
        h=Ganadores(columna[0],columna[1],columna[2],columna[3],columna[4])
        listaganadores.append(h)

buscar=input("Ingrese un nombre de película: ")
for b in listaganadores:
    if buscar in b.getdatos():
        print("Sí se encuentra")
        break
else:
    print("No se encuentra")