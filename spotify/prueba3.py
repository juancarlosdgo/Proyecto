Números_ganadores=[]
numeros=int(input("Ingrese número: "))
while numeros!=0:
    numeros=int(input("Ingrese número: "))
    Números_ganadores.append(numeros)    
    Números_ganadores.sort()
print(Números_ganadores)