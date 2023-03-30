busqueda = "Soy una prueba"
encontrado = False
for cancion in canciones:
    if cancion["Título"] == busqueda:
        print(cancion)
        encontrado = True
        break
if not encontrado:
    print("No se encuentra")