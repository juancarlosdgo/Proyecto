N=int(input("Ingrese el dato máximo: "))
suma=0
for i in range(1,N+1):
    suma=suma+i
    if suma>N:
        break
print("Hay que sumar",i,"números")