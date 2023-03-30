from collections import Counter
canciones=[]
while True:
    print("\n1.Para ingresar nombre de la canción.\n2.Para añadir información adicional.\n3.Para eliminar un artista.\n4.Para buscar un artista.\n5.Para buscar una canción.\n6.Para ver lista.\n7.Para mostrar la canción más larga\n8.Para mostrar la canción más corta\n9.Ver el artista con más canciones ")
    Menú=input("Selecciona una opción. Presione enter para salir: ")
    if Menú=="1":
        canción=input("Ingrese nombre de la canción: ")
    elif Menú=="2":
        artista=input("Ingrese el artista de la canción: ")
        género=input("Ingrese el género de la canción: ")
        duración=input("Ingrese duración: ")
        álbum=input("Ingrese nombre de álbum: ")
        canciones.append({"Título":canción,"Artista":artista,"Género":género,"Álbum":álbum,"Duración":duración})
    elif Menú=="3":
        eliminar=input("Ingrese el artista que desea borrar: ")
        for i, cancion in enumerate(canciones):
            if eliminar.lower() in cancion["Artista"].lower():
                canciones.pop(i)
                print(f"El elemento con nombre {eliminar} ha sido eliminado.")
                break
        else:
            print(f"No se encontró ningún elemento con nombre {eliminar}.")
    elif Menú=="4":
        búsqueda=input("Ingrese el artista que desea buscar: ")
        encontrado = False
        for canción in canciones:
            if canción["Artista"]==búsqueda:
                print("Se encuentra")
                encontrado = True
                break
        if not encontrado:
            print("No se encuentra")
    elif Menú=="5":
        búsqueda=input("Ingrese la canción que desea buscar: ")
        encontrado = False
        for canción in canciones:
            if canción["Título"]==búsqueda:
                print("Se encuentra")
                encontrado = True
                break
        if not encontrado:
            print("No se encuentra")
    elif Menú=="6":
        canciones_ordenadas = sorted(canciones, key=lambda x: x["Título"])
        for valor in canciones_ordenadas:
            print("Título: {} Artista: {} Género: {} Álbum: {} Duración: {}".format(valor["Título"],valor["Artista"],valor["Género"],valor["Álbum"],valor["Duración"]))
    elif Menú=="7":
        canciones.sort(key=lambda x:x["Duración"],reverse=True)
        mas_larga=canciones[0]
        print(mas_larga)
    elif Menú=="8":
        mas_corta = min(canciones, key=lambda x: x["Duración"])
        print(mas_corta)
    elif Menú=="9":
        artistas = [cancion["Artista"] for cancion in canciones]
        counts = Counter(artistas)
        artista_mas_canciones = counts.most_common(1)[0][0]
        print("El artista con más canciones es: ",artista_mas_canciones)
    elif Menú=="":
        break