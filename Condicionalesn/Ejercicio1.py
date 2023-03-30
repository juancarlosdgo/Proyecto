a=int(input("Ingrese un número: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el tercer número: "))
if a>b>c:
    print(a)
elif a>b<c:
    print(c)
elif a<b>c:
    print(b)
elif b>a>c:
    print(c)
elif b<a>c:
    print(b)
elif b<a>c:
    print(a)
elif c>b>a:
    print(c)
elif c<b>a:
    print(b)
elif c<b>a:
    print(a)

