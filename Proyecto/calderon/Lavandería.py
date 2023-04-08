from ClaseFactura import *
import sqlite3
con=sqlite3.connect("proyectosena.db")
cursor=con.cursor()
def ver():
    lista=[]
    sentence=("SELECT * FROM fac_lavandería")
    lista=cursor.execute(sentence).fetchall()
    lavandería=[]
    for fila in lista:
        num_hab=fila[0]
        método_pago=fila[1]
        num_factura=fila[2]
        total=fila[3]
        fr=Lavandería(str(num_hab),método_pago,str(num_factura),str(total))
        lavandería.append(fr)
    for factura in lavandería:
        print(factura.getLav())
def buscar():
    numero=input("Ingrese el número de la factura: ")
    sentence=f"SELECT * FROM fac_lavandería WHERE num_hab='{numero}'"
    b=cursor.execute(sentence).fetchall()
    for i in b:
        print(i)
def registro():
    num_hab=input("Ingrese el número de habitación: ")
    método_pago=input("Ingrese el método de pago: ")
    num_factura=input("Ingrese el número de factura: ")
    total=int(input("Ingrese el total: "))
    sentence=f"INSERT INTO fac_lavandería VALUES ('{num_hab}','{método_pago}','{num_factura}','{total}')"
    cursor.execute(sentence)
    con.commit()
    print("¡¡Registro exitoso!!")

while True:
    #menu=int(input("1.Restaurante.\n2.Lavandería."))
    menu=int(input("\nSeleccione una opción: \n1.Ver facturas\n2.Buscar una factura\n3.Añadir registro de factura\n4.Salir: "))        
    match menu:
        case 1:
            ver()
        case 2:
            buscar()
        case 3:
            registro()
        case 4:
            break