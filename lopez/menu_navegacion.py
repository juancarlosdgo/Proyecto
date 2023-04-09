def menu():
    print("==== Navega por nuestro hotel ====")
    print("1. Ver reservaciones")
    print("2. Hacer una reservación")
    print("3. Cancelar una reservación")
    print("4. Ver habitaciones disponibles")
    print("5. Asignar una habitación")
    print("6. Liberar una habitación")
    print("7. Ver estado de la habitación")
    print("8. Generar factura")
    print("9. Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        ver_reservaciones()
    elif opcion == "2":
        hacer_reservacion()
    elif opcion == "3":
        cancelar_reservacion()
    elif opcion == "4":
        ver_habitaciones_disponibles()
    elif opcion == "5":
        asignar_habitacion()
    elif opcion == "6":
        liberar_habitacion()
    elif opcion == "7":
        ver_estado_habitacion()
    elif opcion == "8":
        generar_factura()
    elif opcion == "9":
        salir()
    else:
        print("Opción inválida, por favor intente de nuevo.")
        menu()

def ver_reservaciones():

    print("=== Reservaciones ===")
    if len(reservaciones) == 0:
        print("No hay reservaciones")
    else:
        for reservacion in reservaciones:
            print(f"{reservacion['nombre']} ha reservado la habitación {reservacion['habitacion']} del {reservacion['fecha_inicio']} al {reservacion['fecha_fin']}")
    input("Presione enter para continuar...")
    menu()

def hacer_reservacion():

    nombre = input("Ingrese su nombre: ")
    fecha_inicio = input("Ingrese la fecha de inicio de la reserva (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin de la reserva (YYYY-MM-DD): ")
    habitacion = input("Ingrese el número de habitación: ")
    reservacion = {
        "nombre": nombre,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "habitacion": habitacion
    }
    reservaciones.append(reservacion)
    print("Reservación realizada con éxito.")
    input("Presione enter para continuar...")
    menu()

def cancelar_reservacion():

    print("=== Cancelar Reservación ===")
    if len(reservaciones) == 0:
        print("No hay reservaciones para cancelar.")
    else:
        nombre = input("Ingrese su nombre: ")
        habitacion = input("Ingrese el número de habitación: ")
        for reservacion in reservaciones:
            if reservacion['nombre'] == nombre and reservacion['habitacion'] == habitacion:
                reservaciones.remove(reservacion)
                print("Reservación cancelada con éxito.")
                break
        else:
            print("No se encontró una reservación con los datos proporcionados.")
    input("Presione enter para continuar...")
    menu()

def ver_habitaciones_disponibles():

    print("=== Habitaciones Disponibles ===")
    if len(habitaciones) == 0:
        print("No hay habitaciones disponibles.")
    else:
        for habitacion in habitaciones:
            if habitacion not in [reservacion['habitacion'] for reservacion in reservaciones]:
                print(f"Habitación {habitacion} está disponible.")
            else:
                print(f"Habitación {habitacion} no está disponible.")
    input("Presione enter para continuar...")
    menu()

def asignar_habitacion():

    print("=== Asignar Habitación ===")
    if len(habitaciones) == 0:
        print("No hay habitaciones disponibles.")
    else:
        nombre = input("Ingrese su nombre: ")
        habitacion = input("Ingrese el número de habitación: ")
        for reservacion in reservaciones:
            if reservacion['nombre'] == nombre and reservacion['habitacion'] == habitacion:
                reservacion['estado'] = 'ocupada'
                print("Habitación asignada con éxito.")
                break
        else:
            print("No se encontró una reservación con los datos proporcionados.")
    input("Presione enter para continuar...")
    menu()

def liberar_habitacion():

    print("=== Liberar Habitación ===")
    if len(habitaciones) == 0:
        print("No hay habitaciones disponibles.")
    else:
        nombre = input("Ingrese su nombre: ")
        habitacion = input("Ingrese el número de habitación: ")
        for reservacion in reservaciones:
            if reservacion['nombre'] == nombre and reservacion['habitacion'] == habitacion:
                reservacion['estado'] = 'libre'
                print("Habitación liberada con éxito.")
                break
        else:
            print("No se encontró una reservación con los datos proporcionados.")
    input("Presione enter para continuar...")
    menu()

def ver_estado_habitacion():

    print("=== Estado de Habitación ===")
    if len(habitaciones) == 0:
        print("No hay habitaciones disponibles.")
    else:
        habitacion = input("Ingrese el número de habitación: ")
        reservada = False
        for reservacion in reservaciones:
            if reservacion['habitacion'] == habitacion:
                print(f"La habitación {habitacion} está reservada por {reservacion['nombre']} del {reservacion['fecha_inicio']} al {reservacion['fecha_fin']}")
                reservada = True
                break
        if not reservada:
            print(f"La habitación {habitacion} está disponible.")
    input("Presione enter para continuar...")
    menu()

def generar_factura():

    print("=== Generar Factura ===")
    if len(habitaciones) == 0:
        print("No hay habitaciones disponibles.")
    else:
        nombre = input("Ingrese su nombre: ")
        habitacion = input("Ingrese el número de habitación: ")
        for reservacion in reservaciones:
            if reservacion['nombre'] == nombre and reservacion['habitacion'] == habitacion:
                dias = (reservacion['fecha_fin'] - reservacion['fecha_inicio']).days
                costo = dias * TARIFA_DIARIA
                print(f"Nombre del huésped: {nombre}")
                print(f"Número de habitación: {habitacion}")
                print(f"Fecha de entrada: {reservacion['fecha_inicio']}")
                print(f"Fecha de salida: {reservacion['fecha_fin']}")
                print(f"Días de estancia: {dias}")
                print(f"Costo total: ${costo}")
                break
        else:
            print("No se encontró una reservación con los datos proporcionados.")
    input("Presione enter para continuar...")
    menu()

def salir():

    print("Gracias por utilizar nuestro software de hotel. ¡Hasta pronto!")
    exit()

menu()