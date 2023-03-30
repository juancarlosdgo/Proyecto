a=int(input("Ingrese un número: "))
b=int(input("Ingrese el divisor: "))
cont=0
while a>=b:
    cont=cont+1
    a=a-b
print(cont)
print(a)