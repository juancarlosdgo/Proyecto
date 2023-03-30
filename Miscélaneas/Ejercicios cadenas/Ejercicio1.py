def sin_repetir():
    palabra=input("Ingrese una palabra: ").lower()
    p=palabra.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    x=len(set(p))
    print(x)
sin_repetir()