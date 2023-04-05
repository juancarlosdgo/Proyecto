class Factura:
    def __init__(self, num_factura, fecha_emision, precio_total, estado_pago, id_reserva):
        self.__num_factura=num_factura
        self.__fecha_emision=fecha_emision
        self.__precio_total=precio_total
        self.__estado_pago=estado_pago
        self.__id_reserva=id_reserva
    def getDatos(self):
        return self.__num_factura, self.__fecha_emision, self.__precio_total, self.__estado_pago, self.__id_reserva