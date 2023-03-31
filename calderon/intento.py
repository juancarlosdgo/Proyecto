import sqlite3
con=sqlite3.connect("proyectosena.db")
mi_cursor=con.cursor()
tabla=input("Ingrese el nombre de la tabla: ")
número=int(input("¿Cuántos valores desea moficar: "))
for i in range(número):
    opcion=input("Ingrese el campo que desea modificar: ")
    sentencia=f"INSERT INTO {tabla} VALUES({i})"
mi_cursor.execute(sentencia)
con.commit()
print("Registro creado")