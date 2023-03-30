personas={"123456789":["Brandon","Rodríguez"],"123987564":["Ana María","Fernández"]}
búsqueda=input("Ingrese el valor que desea buscar: ")
encontrado=False
for key,value in personas.items():
    if búsqueda in value and type(value)==list:
        print(búsqueda,"Se encuentra.")
        encontrado=True
if not encontrado:
    print("No se encuentra.")
def eliminar(borrar):
    if borrar in personas:
        del personas[borrar]
        print("El elemento", borrar,"fue eliminado. ")
    else:
        print("No se encuentra. ")
borrar=input("Ingrese el valor que desea borrar: ")
eliminar(borrar)
def añadir():
    while True:
        try:
            número=int(input("Ingrese número de identificación: "))
            nombres=input("Ingrese nombres: ")
            apellidos=input("Ingrese apellidos: ")
            personas.setdefault(número,[nombres,apellidos])
            print(personas)
            break
        except ValueError:
            print("Valor incorrecto")
añadir()