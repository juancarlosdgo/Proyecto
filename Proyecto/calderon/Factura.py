from ClaseFactura import *
import sqlite3
con=sqlite3.connect("proyectosena.db")
micursor=con.cursor()
def ver():
    lista=[]
    sentence="SELECT * FROM tb_facturas"
    lista=micursor.execute(sentence).fetchall()
    facturas=[]
    for fila in lista:
        numero=fila[0]
        fecha=fila[1]
        precio=fila[2]
        estado=fila[3]
        id_reserva=fila[4]
        num_hab=fila[5]
        f=Factura(str(numero),str(fecha),str(precio),estado,str(id_reserva),str(num_hab))
        facturas.append(f)
    for factura in facturas:
        print(factura.getDatos())
def datos():
    num=input("Ingrese el número de factura: ")
    sentence=f"SELECT * FROM tb_facturas WHERE num_factura={num}"
    datos=micursor.execute(sentence).fetchall()
    [print(j, end=" ") for i in datos for j in i]
def factura():
    campo=input("¿De qué columna desea ver el dato?: ")
    campo2=input("Específique la columna de donde va a obtener el dato: ")
    operador=input("Ingrese el operador: ")
    campo3=input("Específique el dato: ")
    sentence=f"SELECT {campo} FROM tb_facturas WHERE {campo2}{operador}'{campo3}'"
    datos=micursor.execute(sentence).fetchall()
    for i in datos:
        for j in i:
            print(f"{campo} es {j}")
def registro():
    a=input("Ingrese número de factura: ")
    b=input("Ingrese fecha : ")
    c=input("Ingrese precio total: ")
    d=input("Ingrese estado del pago: ")
    e=input("Ingrese el id de reserva: ")
    sentence=f"INSERT INTO tb_facturas VALUES ('{a}','{b}','{c}','{d}','{e}')"
    micursor.execute(sentence)
    con.commit()
    print("¡¡Registro creado!!")
def modificación():
    columna=input("Ingrese la columna de la que desea modificar el dato: ")
    dato=input("Ingrese el nuevo dato: ")
    a=input("Ingrese la columna: ")
    operador=input("Ingrese el operador: ")
    b=input("Ingrese el dato que desea modificar: ")
    micursor.execute(f"UPDATE tb_facturas SET {columna}='{dato}' WHERE {a}{operador}'{b}'")
    con.commit()
    print("¡¡Modificación exitosa!!")
def eliminar():
    campo=input("Ingrese el campo: ")
    operador=input("Ingrese el operador: ")
    dato=input("Ingrese el campo que desea borrar: ")
    sentence=f"DELETE FROM tb_facturas WHERE {campo}{operador}{dato}"
    micursor.execute(sentence)
    con.commit()
while True:
    try:
        menu=int(input("\nSeleccione una opción: \n1.Ver todas las facturas.\n2.Ver los datos de una factura.\n3.Ver un dato específico de una o varias facturas.\n4.Registrar factura.\n5.Modificar registro\n6.Eliminar factura.\n7.Salir: "))
        match menu:
            case 1:
                ver()
            case 2:
                datos()
            case 3:
                factura()
            case 4:
                registro()
            case 5:
                modificación()
            case 6:
                eliminar()
            case 7:
                break
    except sqlite3.IntegrityError:
       print("Verifique que los datos no estén repetidos y que sean correctos.")