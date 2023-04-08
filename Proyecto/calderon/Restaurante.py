from ClaseFactura import *
import sqlite3
con=sqlite3.connect("proyectosena.db")
cursor=con.cursor()

def ver():
    lista=[]
    sentence=("SELECT * FROM fac_restaurante")
    lista=cursor.execute(sentence).fetchall()
    restaurante=[]
    for fila in lista:
        nombre=fila[0]
        documento=fila[1]
        método_pago=fila[2]
        num_hab=fila[3]
        id_reserva=fila[4]
        total=fila[5]
        fr=Restaurante(nombre,str(documento),método_pago,str(total),str(num_hab),str(id_reserva))
        restaurante.append(fr)
    for factura in restaurante:
        print(factura.getFacturarestaurante())
def buscar():
    numero=input("Ingrese el número de la factura: ")
    sentence=f"SELECT * FROM fac_restaurante WHERE num_hab='{numero}'"
    b=cursor.execute(sentence).fetchall()
    for i in b:
        print(i)
def registro():
    nombre=input("Ingrese el nombre: ")
    documento=int(input("Ingrese el número de documento: "))
    método_pago=input("Ingrese el método de pago: ")
    num_hab=input("Ingrese el número de habitación: ")
    num_factura=input("Ingrese el número de factura: ")
    total=int(input("Ingrese el total: "))
    sentence=f"INSERT INTO fac_restaurante VALUES ('{nombre}','{documento}','{método_pago}','{num_hab}','{num_factura}','{total}')"
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