import sqlite3
con=sqlite3.connect('E:\hotelpython\proyectosenadb.db')
print(type(con))
micursor=con.cursor()
print(type(micursor))
new_sql="select * from tb_reseña;"
micursor.execute(new_sql)
lista=micursor.fetchall()
for fila in lista:
    print(fila[1])
    print(fila[2])
    print(fila[3])
    print('*'*50)