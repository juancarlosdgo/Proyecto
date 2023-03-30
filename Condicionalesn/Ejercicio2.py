a=int(input("Ingrese un número: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el tercer número: "))
if a==b and b==c:
    print("Los tres son iguales")
elif a==b or b==c:
    print("Hay dos iguales")
elif a==c or b==a:
    print("Hay dos iguales")
elif b==c or b==a:
    print("Hay dos iguales")
else:
    print("Todos son diferentes")