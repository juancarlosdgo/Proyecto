import sqlite3
con=sqlite3.connect('C:\\Users\\Juan Camilo\\Desktop\\Proyecto\\lopez\\CRUD tablas\\proyectosena.db')
micursor=con.cursor()

def todo():
    print("digite 1 para seleccionar los datos de una tabla")
    print("digite 2 para modificar los datos de una tabla")
    print("digite 3 para eliminar los datos de una tabla")
    print("digite 4 para insentar los datos de una tabla")
    
    ingrese=int(input("Digite un numero para escoger una opcion: "))
    if ingrese ==1:
        try:
            e=input("digite el campo que desea seleccionar: ")
            o=input("digite el dato que desea seleccionar: ")
            def seleccion(tabla):
                sentencia=f"SELECT * FROM {tabla} WHERE {e}='{o}'"
                #print(sentencia)
                micursor.execute(sentencia)    
                lista=micursor.fetchall()
                for fila in lista:
                    print(fila[0])
                    print(fila[1])
                    print(fila[2])
                    print(fila[3])
                    print(fila[4])
                    print('*'*50)
            seleccion('tb_inventario')
        except:
            print("tienes algun error al ingresar los datos") 

    if ingrese ==2:
        try:
            e=input("ingrese el campo que desea modificar: ")
            i=input("ingrese el dato modificado: ")
            o=input("ingrese el id_inventario que se desea modificar: ")
            def modificar(tabla):
                sentencia=f"UPDATE {tabla} SET {e}='{i}'WHERE id_inventario={o}"
                print(sentencia)
                micursor.execute(sentencia)
                con.commit()
                print('Modificación Exitosa!!!!')
            modificar('tb_inventario')
        except:
            print("tienes algun error al ingresar los datos")
        
        
    if ingrese ==3:
        try:
            e=input("ingrese el id_cliente que desea eliminar: ")
            def eliminar(tabla,campo):
                sentencia=f"DELETE FROM {tabla} WHERE {campo}='{e}'"
                micursor.execute(sentencia)
                con.commit()
                print('Eliminación Exitosa!!!!')

            eliminar('tb_inventario','id_inventario')
            
        except:
            print("tienes algun error al ingresar los datos")
    if ingrese ==4:       
        try:
            a=int(input("ingrese el dato a insertar en el campo id_inventario: "))
            e=int(input("ingrese el dato a insertar en el campo alimentos: "))
            i=int(input("ingrese el dato a insertar en el campo bebidas: "))
            o=int(input("ingrese el dato  a insertar en  el campo articulos_limpieza: "))
            u=int(input("ingrese el dato  a insertar en  el campo articulos_cama: "))

            def insertar(tabla):                
                sentencia=f"INSERT INTO {tabla} VALUES ('{a}','{e}','{i}','{o}','{u}')"
                micursor.execute(sentencia)
                con.commit()
                print('Registro Creado!!!!')
                
            insertar('tb_inventario')
            seleccion('tb_inventario','id_inventario','=',2)
        except:
                print("tienes algun error al ingresar los datos")
    else:
        print("el dato que ingresaste no se encuentra")
todo()