import sqlite3

conec=sqlite3.connect("proyectosena.db")
micursor=conec.cursor()
while True:
    try:
        opcion=int(input("\nSeleccione la opción que desea: \n1.Visualizar todas las reseñas.\n2.Ver todos los datos de un campo seleccionado\n3.Ver un dato en específico.\n4.Actualizar un dato\n5.Eliminar\n6.Insertar datos\n7.Salir: "))
        match opcion:
            case 1:
                sentence=f"SELECT * FROM tb_reseña"
                lista=micursor.execute(sentence).fetchall()
                for i in lista:
                    print(i)
            case 2:
                #tabla=input("Ingrese nombre de la tabla: ").lower()
                a=input("Ingrese el nombre de la columna: ")
                b=input("Ingrese el operador: ")
                c=input("Ingrese el valor que desea especificar: ")
                sentence2=f"SELECT * FROM tb_reseña WHERE {a}{b}'{c}'"
                ab=micursor.execute(sentence2).fetchall()
                for fila in ab:
                    print(fila)
            case 3:
                #tabla=input("Ingrese nombre de la tabla: ").lower()
                a=input("Ingrese el campo que desea observar: ")
                b=input("Ingrese el valor que desea seleccionar: ")
                c=input("Ingrese el operador: ")
                d=input("Ingrese el valor que desea observar: ")
                sentence3=f"SELECT {a} FROM tb_reseña WHERE {b}{c}'{d}'"
                datos=micursor.execute(sentence3).fetchall()
                for fila in datos:
                    for i in fila:
                        print(f"{a} es {i}")
            case 4:
                #tabla=input("Ingrese nombre de la tabla: ").lower()
                columna=input("De qué columna: ")
                dato=input("Ingrese el nuevo dato: ")
                b=input("Especifique el dato: ")
                c=input("Especifique el valor que desea modificar: ")
                sentence4=f"UPDATE tb_reseña SET {columna}='{dato}' WHERE {b}='{c}'"
                micursor.execute(sentence4)
                conec.commit()
                print("¡¡Modificación exitosa!!")
            case 5:
                #tabla=input("Ingrese nombre de la tabla: ").lower()
                a=input("Ingrese la columna: ")
                b=input("Ingrese el operador: ")
                c=input("Ingrese el dato: ")
                sentence5=f"DELETE FROM tb_reseña WHERE {a}{b}'{c}'"
                micursor.execute(sentence5)
                conec.commit()
                print("Eliminación exitosa...")
            case 6:
                #tabla=input("Ingrese nombre de la tabla: ").lower()
                x=f"PRAGMA table_info (tb_reseña)"
                colum=micursor.execute(x)
                campos=[]
                dates=[]
                for i in colum:
                    a=i[1]
                    campos.append(a)
                    nuevo=input(f"Ingrese valor para {a}: ")
                    dates.append(nuevo)
                frase = f"INSERT INTO tb_reseña ({', '.join(campos)}) VALUES ({', '.join(['?']*len(campos))})"
                micursor.execute(frase,dates)
                conec.commit()
                print("¡¡Regstro creado!!")
            case 7:
                break
    except (sqlite3.OperationalError,sqlite3.IntegrityError):
        print("Verifica que los datos sean correctos, que no estén repetidos o que se encuentren en la tabla.")

