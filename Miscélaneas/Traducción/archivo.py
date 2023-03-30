español=['Maleta', 'Cuaderno', 'Pegante', 'Lápiz', 'Crayolas', 'Tijeras', 'Regla', 'Borrador', 'Resaltador', 'Esfero', 'Transportador', 'Cartuchera', 'Marcador', 'Tajalápiz', 'Carpeta', 'Notas', 'Calculadora', 'Colores', 'Corrector', 'Compás', 'Diccionario', 'Pincel']
ing=['Bag', 'Notebook', 'Glue', 'Pencil', 'Crayons,', 'Scissors', 'Ruler', 'Eraser', 'Highlehter pen', 'Pen', 'Conveyor', 'Pencil case', 'Marker', 'Sharpener', 'Folder', 'Sticky notes', 'Calculator', 'Colors', 'Concealer', 'Compass', 'Dictionary', 'Brush']
franc=["Valise","Cahier","Colle","Crayon","Des crayons","paire de ciseaux","Régle","La gomme","surligneur","Sphére","Convoyeur","Poche","Marqueur","Taille-crayon","Dossier","Remarques","Calculatrice","Couleurs","Correcteur","Le compas","Dictionnaire","Brosse"]
inglés={}
francés={}
tipo_palabra={}
sin_tilde=(("a","á"),("e","é"),("i","í"),("o","ó"),("u","ú"))
for i in range(len(español)): #Acá se concatenan ambas listas(español e ing con las palabras en inglés)
    inglés[español[i]]=ing[i] 
for j in range(len(español)): #Acá se concatenan ambas listas(español y franc con las palabras en francés)
    francés[español[j]]=franc[j]
tipo="sustantivo"
for l in español:
    tipo_palabra[l]=tipo
def esp_ingl():
    buscar=input("Ingrese la palabra que desea traducir: ").lower()
    for key in inglés.keys():
        for a,b in sin_tilde:
            if key.lower()==buscar.replace(a,b):
                return "La traducción al inglés significa "+inglés[key]+"\n"
    else:
        return "La palabra ingresada no se encuentra.\n"
def esp_fran():
    buscar=input("Ingrese la palabra que desea traducir: ").lower()
    for key in francés:
        for a,b in sin_tilde:
            if key.lower()==buscar.replace(a,b):
                return "La traducción al francés es: "+francés[key]+"\n"
    else:
        return "La palabra ingresada no se encuentra.\n"
def tipo():
    buscar=input("Ingrese la palabra: ").lower()
    for key in tipo_palabra.keys():
        for a,b in sin_tilde:
            if key.lower()==buscar.replace(a,b):
                return "Es un "+tipo_palabra[key]+"\n"
    else:
        return "La palabra no existe en el diccionario\n"
def ing_esp():
    buscar=input("Ingrese la palabra: ").lower()
    for key,value in inglés.items():
        if value.lower()==buscar:
            return "La traducción al español es: "+key+"\n"
    return "No se encuentra.\n"
def fran_esp():
    buscar=input("Ingrese la palabra: ").lower()
    p=buscar.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    for key,value in francés.items():
        if value.lower()==p:
            return "La traducción al español es: "+key+"\n"
    return "No se encuentra\n"
def todo_al_tiempo():
    buscar=input("Ingrese una palabra: ").lower()
    for dic in [inglés,francés,todo_al_tiempo]:
        for key,value in dic.items():
            if key.lower()==buscar:
                return "Inglés: "+inglés[key]+ "\nFrancés: "+francés[key]+"\nTipo de palabra: "+tipo_palabra[key]+"\n"
            if value.lower()==buscar:
                return "Español:"+key+ "\nFrancés:"+francés[key]+"\nTipo de palabra: "+tipo_palabra[key]+"\n"
            for key,value in francés.items():
                if value.lower()==buscar:
                    return "Español: "+key+ "\nInglés: "+inglés[key]+"\nTipo de palabra: "+tipo_palabra[key]+"\n"
        return "La palabra ingresada no se encuentra\n"
def mostrar_menú():
    while True:
        try:
            opción=int(input("1.Traducir del español al inglés.\n2.Traducir del español al francés\n3.Averiguar que tipo de palabra es\n4.Traducir del inglés al español\n5.Traducir del francés al español\n6.Todo al tiempo\n7.Salir:"))
            match opción:
                case 1:
                    print(esp_ingl())
                case 2:
                    print(esp_fran())
                case 3:
                    print(tipo())
                case 4:
                    print(ing_esp())
                case 5:
                    print(fran_esp())
                case 6:
                    print(todo_al_tiempo())
                case 7:
                    break
            if opción>7:
                print("Número inválido, tiene que escoger una opción del 1 al 7.\n")
        except:
            print("El dato ingresado no es válido, tiene que ingresar un número.\n")