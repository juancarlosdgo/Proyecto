n=int(input("Ingrese un número del 1 al 10: "))
m=int(input("Ingrese otro número del 1 al 10: "))
try:
    w=open("tabla-"+str(n)+".txt","r")
    y=w.readlines()
    print(y[m-1])
except:
    print("No se encuentra.")


