import sqlite3
con=sqlite3.connect("proyectosena.db")
micursor=con.cursor()
campo=input("Ingrese un dato: ")

sentence=f"SELECT {campo} FROM tb_facturas INNER JOIN fac_restaurante ON tb_facturas.Num_factura=fac_restaurante.Numero_fac"
c=micursor.execute(sentence)
for i in c:
    print(i)