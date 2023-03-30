Respuesta="si"
print("¿En un juego de preguntas a las que se responde ""si"" o ""no"", gana quién responda correctamente a las preguntas. Si responde mal a cualquiera de ellas, ya no se pregunta la siguiente y termina el juego.\nLas preguntas son: ")
Pregunta1=input("¿Colón descubrió América?:")
if Respuesta==Pregunta1.lower():
    print("Correcto")
    Pregunta2=input("¿La independencia de Colombia fue en el año 1810?: ")
    if Respuesta==Pregunta2.lower():
        print("Correcto")
        Pregunta3=input("¿The Doors fue un grupo de rock americano?: ")
        if Respuesta==Pregunta3.lower():
            print("Felicidades, has ganado el juego")
        else:
            print("Incorrecto, has perdido el juego")
    else:
        print("Incorrecto, fin del juego")
        
else:
    print("Incorrecto, fin del juego")