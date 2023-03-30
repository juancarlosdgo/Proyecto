from Empresa import *
from cliente import *
while True:
    op=int(input("1.Ingresar número y teléfono\n2.Salir: "))
    match op:
        case 1:
            nombre=input("Ingrese el nombre del cliente: ")
            teléfono=int(input("Ingrese número de teléfono: "))
        case 2:
            break
    c=cliente(nombre,teléfono)
    with open("lista.txt","a") as file:
        file.write(c.getnombre()+","+str(c.getTeléfono())+"\n")