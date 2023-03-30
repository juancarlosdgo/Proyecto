moneda={"Euro":"E","Dollar":"$","Yen":"Y"}
divisa=input("Ingrese la divisa que desea ver: ")
if divisa in moneda:
    print(moneda[divisa])
else:
    print("No se encuentra.")