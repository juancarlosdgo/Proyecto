def suma():
    palabra=input("Ingrese una palabra: ")
    suma=0
    y=len(palabra)
    for i in palabra:
        if i in " ":
            y-=1
    for j in range(y):
        suma+=j
    print("La suma de",palabra,"es",suma)
suma()