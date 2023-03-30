facturas={}
pendiente=0
cobrada=0
while True:
    opción=int(input("1.Para añadir una nueva factura.\n2.Para pagar una factura.\n3.Para terminar: "))
    if opción==1:
        número=int(input("Ingrese número de la factura: "))
        valor=float(input("Ingrese valor de la factura: "))
        pendiente+=valor
        facturas.setdefault(número,valor)
        print("Cantidad cobrada:", cobrada)
        print("Cantidad pendiente de cobro: ",pendiente)
    elif opción==2:
        número=int(input("Ingrese número de la factura: "))
        facturas.pop(número)
        cobrada+=valor
        pendiente-=valor
        print("Cantidad cobrada:", cobrada)
        print("Cantidad pendiente de cobro: ",pendiente)
    elif opción==3:
        print("Cantidad cobrada:", cobrada)
        print("Cantidad pendiente de cobro: ",pendiente)
        break
