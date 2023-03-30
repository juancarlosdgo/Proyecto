frutas={"Plátano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
fruta=input("Ingrese la fruta que desea buscar: ").title()
kilos=float(input("¿Cuántos kilos?: "))
if fruta in frutas:
    print(kilos,"kilos valen",frutas[fruta]*kilos)
else:
    print("No existe en el diccionario")
        