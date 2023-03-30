países={"Colombia":"Bogotá D.C","Argentina":"Buenos Aires","Australia":"Canberra","Canadá":"Ottawa"}
def capital(búsqueda):
    if búsqueda in países:
        print(países[búsqueda])
    else:
        print("No se encuentra.")
búsqueda=input("Ingrese nombre del país: ")
capital(búsqueda)