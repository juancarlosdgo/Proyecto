import sqlite3
conn=sqlite3.connect("proyectosena.db")
cursor=conn.cursor()
tabla=input("Ingrese el nombre de la tabla")
cursor.execute(f"PRAGMA table_info ({tabla})")
columnas=cursor.fetchall()
print(len(columnas))
conn.close()