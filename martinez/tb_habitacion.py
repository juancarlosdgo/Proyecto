import sqlite3
con=sqlite3.connect('proyectosenadb.db')
micursor=con.cursor()

def todo():
    print("digite 1 para seleccionar los datos de una tabla")
    print("digite 2 para modifficar los datos de una tabla")
    print("digite 3 para eliminar los datos de una tabla")
    print("digite 4 para insentar los datos de una tabla")
    
    ingrese=int(input("digite el numero: "))
    if ingrese ==1:
        try:
            e=input("digite el campo que desea seleccionar: ")
            i=input("digite el operador que desea seleccionar: ")
            o=input("digite el dato que desea seleccionar: ")
            def seleccion(tabla):
                sentencia=f"SELECT * FROM {tabla} WHERE {e}{i}'{o}'"
                #print(sentencia)
                micursor.execute(sentencia)    
                lista=micursor.fetchall()
                for fila in lista:
                    print(fila[0])
                    print(fila[1])
                    print(fila[2])
                    print(fila[3])
                    print('*'*50)
            seleccion('tb_habitaciones')
        except:
            print("tienes algun error al ingresar los datos") 

    if ingrese ==2:
        try:
            e=input("ingrese el campo que desea modificar: ")
            i=input("ingrese el dato modificado: ")
            o=input("ingrese el id_modificar que se desea modificar: ")
            def modificar(tabla):
                sentencia=f"UPDATE {tabla} SET {e}='{i}'WHERE num_habitacion={o}"
                print(sentencia)
                micursor.execute(sentencia)
                con.commit()
                print('Modificación Exitosa!!!!')
            modificar('tb_habitaciones')
        except:
            print("tienes algun error al ingresar los datos")
        
        
    if ingrese ==3:
        try:
            e=input("ingrese el num_habitacion que desea eliminar: ")
            def eliminar(tabla,campo):
                sentencia=f"DELETE FROM {tabla} WHERE {campo}='{e}'"
                micursor.execute(sentencia)
                con.commit()
                print('Eliminación Exitosa!!!!')

            eliminar('tb_habitaciones','num_habitacion')
            
        except:
            print("tienes algun error al ingresar los datos")
    if ingrese ==4:       
        try:
            a=input("ingrese el dato a insertar en el campo num_habitacion: ")
            e=input("ingrese el dato a insertar en el campo precio_noche: ")
            i=input("ingrese el dato a insertar en el campo tipo_habitacion: ")
            o=input("ingrese el dato  a insertar en  el campo estado: ")
            def insertar(tabla):                
                sentencia=f"INSERT INTO {tabla} VALUES ('{a}','{e}','{i}','{o}')"
                micursor.execute(sentencia)
                con.commit()
                print('Registro Creado!!!!')
                
            insertar('tb_habitaciones')
            seleccion('tb_habitaciones','num_habitacion','=',6)
        except:
                print("tienes algun error al ingresar los datos")
todo()