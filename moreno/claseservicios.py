class Servicios:
    def __init__(self,idservicio,idreserva,restaurante,habitaciones,lavanderia,piscina,gimnasio):
        self.__idservicio=idservicio
        self.__idreserva=idreserva
        self.__restaurante=restaurante
        self.__habitaciones=habitaciones
        self.__lavanderia=lavanderia
        self.__piscina=piscina
        self.__gimnasio=gimnasio
    def getIdservicio(self):
        return self.__idservicio
    def getIdreserva(self):
        return self.__idreserva
    def getRestaurante(self):
        return self.__restaurante
    def getHabitaciones(self):
        return self.__habitaciones
    def getLavanderia(self):
        return self.__lavanderia
    def getPiscina(self):
        return self.__piscina
    def getGimnasio(self):
        return self.__lavanderia
    def datos(self):
        return self.__idreserva+str(self.__habitaciones)

#id=Servicios('1')
#s1=Servicios('Vino blanco')
#print(s1.getIdservicio())
#print(s1.getIdreserva())