cesta_compra={}
total=0
while True:
    artículo=input("Ingrese nombre del artículo: ")
    precio=float(input("Ingrese precio del artículo: "))
    cesta_compra.setdefault(artículo,precio)
    opción=input("¿Desea ingresar más? Si/No: ")
    if opción=="No":
        break
print(cesta_compra)
for artículo,precio in cesta_compra.items():
    total+=precio
print(total)