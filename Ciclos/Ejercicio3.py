N=int(input("Ingrese un número: "))
suma=0
for i in range(1,N):
    if N%i==0:
        suma+=i
if suma==N:
    print("Es un número perfecto.")
else:
    print("No es un número perfecto.")
