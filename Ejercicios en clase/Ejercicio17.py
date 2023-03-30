cantidad=int(input("Ingrese cantidad: "))
interés_anual=int(input("Ingrese interés anual: "))
número_años=int(input("Ingrese cantidad de número de años: "))
capital=cantidad*interés_anual
for i in range(1,capital,número_años):
    print(i)
    break