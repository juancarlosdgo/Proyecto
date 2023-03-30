import csv
with open ("C:\\Users\\catalina\\Desktop\\Python\\Miscélaneas\\Archivos csv\\Oscares.csv", "r") as archivo:
    r=csv.reader(archivo)
    for i in r:
        print(i)