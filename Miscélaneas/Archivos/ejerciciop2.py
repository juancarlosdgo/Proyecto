n=int(input("Ingrese un número del 1 al 10: "))
try:
    file=open("tabla-"+str(n)+".txt","r")
    datos=file.read()
    print(datos)
except:
    print("El archivo con la tabla del",n,"no se encuentra.")