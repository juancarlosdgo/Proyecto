canciones={"For whom the bell tols":"5:09"}
nombre_canción=input("Ingrese nombre de la canción: ")
duración=input("Ingrese duración: ")
canciones.setdefault(nombre_canción,duración)
print(canciones)
def mayor_duración():
    mayor=max(canciones)
    print("La canción con mayor duración es:",mayor)
def menor_duración():
    menor=min(canciones)
    print("La canción con menor duración es:",menor)
mayor_duración()
menor_duración()



