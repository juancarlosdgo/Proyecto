#Hacer una lista con elementos aleatorios, buscar el número que indique el usuario, decir en que posiciones está, y cuántas veces se repite (con una lista comprimida).
Lista=[1,2,5,4,8,6,9,6,7,7,7,10]
Num=int(input("Ingrese el número: "))

posición=[x for x in Lista if Num==Lista[x]]
print("El número", Num, "se ha encontrado en la posición:", posición, "\nSe ha encontrado", Lista.count(Num),"veces")

Número_veces=[x for x in Lista if Num!=Lista]
print("No se encontró el número")
Lista.append(Num)
print(Lista)