import sqlite3
con=sqlite3.connect('proyectosenadb.db')
micursor=con.cursor()

def todo():
    print("puedes solamente ver las tablas servicios,habitaciones,empleados")
    ver=input("que tabla desea seleccionar: ")
    
    if ver=='empleados':
        print("digite 1 para consultar los datos de una tabla")
        print("digite 2 para actualizar los datos de una tabla")
        print("digite 3 para eliminar los datos de una tabla")
        print("digite 4 para crear los datos de una tabla")
        ingrese=int(input("digite el numero: "))        
        if ingrese ==1:
            try:
                e=input("digite el campo que desea consultar: ")
                i=input("digite el operador que desea consultar: ")
                o=input("digite el dato que desea consultar: ")
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
                        print(fila[4])
                        print(fila[5])
                        print('*'*50)
                seleccion('tb_empleados')
            except:
                print("tienes algun error al ingresar los datos") 

        if ingrese ==2:
            try:
                e=input("ingrese el campo que desea actualizar: ")
                i=input("ingrese el dato actualizado: ")
                o=input("ingrese el id_empleado que se desea actualizar: ")
                def modificar(tabla):
                    sentencia=f"UPDATE {tabla} SET {e}='{i}'WHERE id_empleado={o}"
                    print(sentencia)
                    micursor.execute(sentencia)
                    con.commit()
                    print('Modificación Exitosa!!!!')
                modificar('tb_empleados')
            except:
                print("tienes algun error al ingresar los datos")
                
        if ingrese ==3:
            try:
                e=input("ingrese el id_empleado que desea eliminar: ")
                def eliminar(tabla,campo):
                    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{e}'"
                    micursor.execute(sentencia)
                    con.commit()
                    print('Eliminación Exitosa!!!!')

                eliminar('tb_empleados','id_empleado')
                    
            except:
                print("tienes algun error al ingresar los datos")
        if ingrese ==4:       
            try:
                a=input("ingrese el dato a crear en el campo id_empleado: ")
                e=input("ingrese el dato a crear en el campo nombre: ")
                i=input("ingrese el dato a crear en el campo cargo: ")
                o=int(input("ingrese el dato  a crear en  el campo salario: "))
                u=input("ingrese el dato  a crear en  el campo horario_trabajo: ")
                b=input("ingrese el dato  a crear en  el campo fecha_contrato: ")
                def insertar(tabla):                
                    sentencia=f"INSERT INTO {tabla} VALUES ('{a}','{e}','{i}','{o}','{u}','{b}')"
                    micursor.execute(sentencia)
                    con.commit()
                    print('Registro Creado!!!!')
                        
                insertar('tb_empleados')
                seleccion('tb_empleados','id_empleado','=',11)
            except:
                print("tienes algun error al ingresar los datos")
        else:
            print("el dato que ingresaste no se encuentra")
    if ver=='servicios':
        print("digite 1 para consultar los datos de una tabla")
        print("digite 2 para actualizar los datos de una tabla")
        print("digite 3 para eliminar los datos de una tabla")
        print("digite 4 para crear los datos de una tabla")
        ingrese=int(input("digite el numero: "))        
        if ingrese ==1:
            try:
                e=input("digite el campo que desea consultar: ")
                i=input("digite el operador que desea consultar: ")
                o=input("digite el dato que desea consultar: ")
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
                        print(fila[4])
                        print(fila[5])
                        print(fila[6])
                        print('*'*50)
                seleccion('tb_servicios')
            except:
                print("tienes algun error al ingresar los datos") 

        if ingrese ==2:
            try:
                e=input("ingrese el campo que desea actualizar: ")
                i=input("ingrese el dato actualizado: ")
                o=input("ingrese el id_servicio que se desea actualizar: ")
                def modificar(tabla):
                    sentencia=f"UPDATE {tabla} SET {e}='{i}'WHERE id_servicio={o}"
                    print(sentencia)
                    micursor.execute(sentencia)
                    con.commit()
                    print('Modificación Exitosa!!!!')
                modificar('tb_servicios')
            except:
                print("tienes algun error al ingresar los datos")
                
        if ingrese ==3:
            try:
                e=input("ingrese el id_servicio que desea eliminar: ")
                def eliminar(tabla,campo):
                    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{e}'"
                    micursor.execute(sentencia)
                    con.commit()
                    print('Eliminación Exitosa!!!!')

                eliminar('tb_servicios','id_servicio')
                    
            except:
                print("tienes algun error al ingresar los datos")
        if ingrese ==4:       
            try:
                a=input("ingrese el dato a insertar en el campo id_servicio: ")
                e=input("ingrese el dato a insertar en el campo id_reserva: ")
                i=input("ingrese el dato a insertar en el campo restaurante: ")
                o=input("ingrese el dato  a insertar en  el campo habitaciones: ")
                u=input("ingrese el dato  a insertar en  el campo lavanderia: ")
                h=input("ingrese el dato  a insertar en  el campo piscina: ")
                c=input("ingrese el dato  a insertar en  el campo gimnasio: ")
                def insertar(tabla):                
                    sentencia=f"INSERT INTO {tabla} VALUES ('{a}','{e}','{i}','{o}','{u}','{h}','{c}')"
                    micursor.execute(sentencia)
                    con.commit()
                    print('Registro Creado!!!!')
                        
                insertar('tb_servicios')
                seleccion('tb_servicios','id_servicio','=',2)
            except:
                print("tienes algun error al ingresar los datos")
        else:
            print("el dato que ingresaste no se encuentra")
    if ver=='habitaciones':
        print("digite 1 para consultar los datos de una tabla")
        print("digite 2 para actualizar los datos de una tabla")
        print("digite 3 para eliminar los datos de una tabla")
        print("digite 4 para crear los datos de una tabla")
        ingrese=int(input("digite el numero: "))        
        if ingrese ==1:
            try:
                e=input("digite el campo que desea consultar: ")
                i=input("digite el operador que desea consultar: ")
                o=input("digite el dato que desea consultar: ")
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
                e=input("ingrese el campo que desea actualizar: ")
                i=input("ingrese el dato actualizado: ")
                o=input("ingrese el num_habitacion que se desea actualizar: ")
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
                a=input("ingrese el dato a crear en el campo num_habitacion: ")
                e=input("ingrese el dato a crear en el campo precio_noche: ")
                i=input("ingrese el dato a crear en el campo tipo_habitacion: ")
                u=input("ingrese el dato  a crear en  el campo estado: ")
                def insertar(tabla):                
                    sentencia=f"INSERT INTO {tabla} VALUES ('{a}','{e}','{i}','{u}')"
                    micursor.execute(sentencia)
                    con.commit()
                    print('Registro Creado!!!!')
                        
                insertar('tb_habitaciones')
                seleccion('tb_habitaciones','num_habitacion','=',6)
            except:
                print("tienes algun error al ingresar los datos")
        else:
            print("el dato que ingresaste no se encuentra")
todo()