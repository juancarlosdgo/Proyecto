X=int(input("Ingrese un número: "))
n=int(input("Ingrese el exponente: "))
contador=1
elevado=1
while contador<=n:
    elevado=elevado*X
    contador=contador+1
print("La potencia de",X,"es: ",elevado)