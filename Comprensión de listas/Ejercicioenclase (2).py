#Números impares y pares
import random
Lista=[]
Lista=[round(random.random()*100) for i in range(10)]

impar=[x for x in Lista if x%2!=0] #Esta función sirve para determinar los números impares, se coloca la función for y una condicional que determine si el residuo es igual a 0
print(impar)

par=[x for x in Lista if x%2==0]# Esta función sirve para determinar los números pares, y se hace de la misma forma
print(par)

par2=[0 if x%2!=0 else x for x in Lista]# Esta función sirve para determinar los números pares con el else
print(par2)