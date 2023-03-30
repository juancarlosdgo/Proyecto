n=int(input("Ingrese un número: "))
cont=0
for i in range(1,n+1):
    if n%i==0:
        cont+=1
if cont>2:
    print("No es primo")
else:
    print("Sí es primo")
