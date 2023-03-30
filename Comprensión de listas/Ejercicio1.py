Lista=[1,2,5,4,8,9,7,6,3,10]
suma=0
i=0
promedio=0
for i in Lista:
    suma=suma+i
    promedio=suma//10
print("El promedio es", promedio)
Debajo=[x for x in Lista if promedio>x] #Aquí se combinan el for y el if
print("Los números" ,Debajo, "están por debajo del promedio")
Encima=[x for x in Lista if promedio<x] #
print("Los números", Encima, "están por encima del promedio")
Igual=[x for x in Lista if promedio==x] 
print("Los números" ,Igual, "son iguales al promedio")
