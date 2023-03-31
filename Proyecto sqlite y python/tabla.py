import sqlite3
conn=sqlite3.connect("proyectosena.db")
cursor=conn.cursor()
tabla=input("Ingrese el nombre de la tabla")

cursor.execute("PRAGMA table_info({})".format(tabla))
columnas=cursor.fetchall()

print("número de columnas: ",len(columnas))
conn.close()