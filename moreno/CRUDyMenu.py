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
        def seleccion(tabla):
            try:
                e=input("digite el campo que desea seleccionar: ")
                i=input("digite el operador que desea seleccionar: ")
                o=input("digite el dato que desea seleccionar: ")
                
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
            except:
                print("tienes algun error al ingresar los datos")   
        seleccion("tb_servicios")
        
    if ingrese==2:
        def modificar(tabla):
            try:
                e=input("ingrese el campo que desea modificar: ")
                i=input("ingrese el dato modificado: ")
                o=input("ingrese el servicios que se desea modificar: ")
                sentencia=f"UPDATE {tabla} SET {e}='{i}'WHERE id_servicio={o}"
                print(sentencia)
                micursor.execute(sentencia)
                con.commit()
                print('Modificación Exitosa!!!!')
            except:
                print("tienes algun error al ingresar los datos")
        modificar('tb_servicios')
    if ingrese==3:
        try:
            e=input("ingrese el id_eventos que desea eliminar: ")
            def eliminar(tabla,campo):
                sentencia=f"DELETE FROM {tabla} WHERE {campo}='{e}'"
                micursor.execute(sentencia)
                con.commit()
                print('Eliminación Exitosa!!!!')
            eliminar('tb_servicios','id_reserva')
        except:
            print("tienes algun error al ingresar los datos")
    if ingrese==4:
        try:
            a=input("ingrese el dato a insertar en el campo detalles_eventos: ")
            e=input("ingrese el dato a insertar en el campo fecha: ")
            i=input("ingrese el dato a insertar en el campo hora: ")
            o=input("ingrese el dato  a insertar en  el campo numero de invitados: ")
            u=input("ingrese el dato a insertar en el campo salon: ")
            p=input("ingre el dato a insertar en el campo id_servicios: ")
            
            def insertar(tabla):
                sentencia=f"INSERT INTO {tabla} VALUES ('{a}','{e}','{i}','{o}','{u}','{p}')"
                micursor.execute(sentencia)
                con.commit()
                print('Registro Creado!!!!')

            insertar('tb_servicios')
            #seleccion('tb_habitaciones','','=',11)
            #'bautizo','23/02/23','4:00 PM','100','3','11'
        except:
            print("tienes algun error al ingresar los datos")
    else:
        print("el dato ingresado no existe")
todo()