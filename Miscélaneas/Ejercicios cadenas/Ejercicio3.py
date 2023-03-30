def valor_códigos():
    cadena=input("Ingrese una palabra: ")
    c=cadena.replace(" ","")
    suma=0
    for i in c:
        x=ord(i)
        suma+=x
    print("El valor númerico según los códigos del alfabeto es: ",suma)
valor_códigos()    