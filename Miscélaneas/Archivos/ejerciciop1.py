n=int(input("Ingrese un número del 1 al 10: "))
file=open("tabla-"+str(n)+".txt","w")
for i in range(1,10+1):
    file.write(str(n)+"X"+str(i)+"="+str(n*i)+"\n")