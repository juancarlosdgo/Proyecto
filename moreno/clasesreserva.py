class Reserva:
    def __init__(self,fecha_entrada,fecha_salida,capacidad,num_habitacion,id_cliente,id_reserva):
        self.__fecha_entrada=fecha_entrada
        self.__fecha_salida=fecha_salida
        self.__capacidad=capacidad
        self.__num_habitacion=num_habitacion
        self.__id_cliente=id_cliente
        self.__id_reserva=id_reserva
    def getfechaEntrada(sefl):
        return sefl.__fecha_entrada 
    def getfechaSalida(self):
        return self.__fecha_salida
    def getCapacidad(self):
        return self.__capacidad
    def numHabitacion(self):
        return self.__num_habitacion
    def idCliente(self):
        return self.__id_cliente
    def getidReserva(self):
        return self.__id_reserva
  