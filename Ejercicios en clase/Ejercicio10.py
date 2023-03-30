traducción={}
while True:
    palabra=input("Inrgese una palabra: ")
    inglés=input("Ingrese su traducción en inglés: ")
    traducción.setdefault(palabra,inglés)
    if palabra =="":
        break
frase=input("Diga una frase en español: ")
print(traducción)
for i in frase.split():
        if i in traducción:
            print(traducción[i], end=" ")
        else:
             print(i,end=" ")