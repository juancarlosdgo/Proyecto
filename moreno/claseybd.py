from clasesreserva import *
import sqlite3
lista=[]

with sqlite3.connect('proyectosena.db') as con:
    micursor=con.cursor()
    new_sql='SELECT * FROM tb_reserva'
    print(micursor.execute(new_sql).fetchall())
    lista=micursor.execute(new_sql).fetchall()

reserva=[]
for fila in lista:
    fecha_entrada=fila[0]
    fecha_salida=fila[1]
    capacidad=[2]
    num_habitacion=[3]
    id_cliente=[4]
    id_reserva=[5]
    ob=Reserva=(fecha_entrada,fecha_salida,capacidad,num_habitacion,id_cliente,id_reserva)
    
print(reserva)

for r in reserva:
    print(r.getIdreserva())

    