file=open("texto.txt","w+",encoding="utf-8")
texto_user=input("Ingrese el texto: ")
file.write(texto_user)
file.close()