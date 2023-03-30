base_datos={}
while True:
    opción=int(input("Menú: \n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar: "))
    if opción==1:
        Nif=int(input("Ingrese nif: "))
        if Nif in base_datos:
            print("Lo sentimos, el nif ingresado ya existe. Intente con otro.")
            Nif=int(input("Ingrese nif: "))
        else:
            nombre=input("Ingrese nombre del cliente: ")
            dirección=input("Ingrese dirección del cliente: ")
            teléfono=int(input("Ingrese número del cliente: "))
            correo=input("Ingrese correo del cliente: ")
            preferente=input("¿Cliente preferente?: ")
        datos_cliente={"Nombre":nombre,"Dirección":dirección,"Teléfono":teléfono,"Correo":correo,"Preferente":True}
        base_datos.setdefault(Nif,(datos_cliente))
    elif opción==2:
        Nif=int(input("Ingrese nif: "))
        if Nif in base_datos:
            base_datos.pop(Nif)
            print("El cliente con el nif ",Nif,"fue eliminado de la lista.")
        else:
            print("Lo sentimos, el nif ingresado no se encuentra.")
    elif opción==3:
        Nif=int(input("Ingrese nif: "))
        if Nif in base_datos:
            print(base_datos[Nif])
        else:
            print("Lo sentimos, el nif ingresado no existe.")
    elif opción==4:
        for key,value in base_datos.items():
            print(key,value)
    elif opción==5:
        clientes_pref=[cliente for cliente, details in datos_cliente.items() if details["Preferente"]==True]
        print(clientes_pref)
    elif opción==6:
        break
    