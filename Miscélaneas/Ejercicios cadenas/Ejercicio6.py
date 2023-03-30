palabra=input("Ingrese cualquier palabra: ")
def aguda(palabra):
    última=palabra[-1]
    if última in "áéíóúns" or palabra in "áéíóú":
        print("La palabra",palabra,"es aguda.")
    elif última not in "aeiou":
        print("La palabra",palabra,"es aguda.")
    else:
        print("La palabra",palabra,"no es aguda.")   
aguda(palabra)
def grave(palabra):
    última=palabra[-1]
    resto=palabra[0:-1]
    for i in resto:
        if i in "áéíóú" and última in "nsaeiou" or última in "áéíóú":
            print("No es grave.")
            break
    else:
        print("Es grave")       
grave(palabra)
def esdrújula(palabra):
    sílaba=""
    for i in palabra:
        if i in "aeiouáéíóú":
            sílaba+=i+"-"
        else:
            sílaba+=i
    if sílaba.endswith("-"):
        sílaba=sílaba[:-1]
    antepenúltima=sílaba[:-5]
    for j in antepenúltima:
        if j in "áéíóú":
            print("Es esdrújula")
            break
    else:
        print("No es esdrújula.")
esdrújula(palabra)
def sobreesdrújula(palabra):
    if palabra.endswith("elo") or palabra.endswith("mente") or palabra.endswith("ela"):
        print("Es sobreesdrújula.")
    else:
        print("No es sobreesdrújula.")
sobreesdrújula(palabra)        