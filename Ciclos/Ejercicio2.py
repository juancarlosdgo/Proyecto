N=int(input("Ingrese un número: "))
cont=0
for i in range(1,N+1):
    if N%i==0:
        cont+=1
if cont>2:
    print("No es primo")
else:
    print("Sí es primo")