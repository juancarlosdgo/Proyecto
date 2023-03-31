import sqlite3
con=sqlite3.connect("proyectosena.db")
micursor=con.cursor()
def seleccion(tabla, campo, operador, dato):
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    lista=micursor.execute(sentencia)
    return lista.fetchall()
print(seleccion("tb_clientes", "nombre","=","Angel"))