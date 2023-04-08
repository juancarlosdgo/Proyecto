class Factura:
    def __init__(self, numero, fecha, precio, estado, id_reserva):
        self.__numero=numero
        self.__fecha=fecha
        self.__precio=precio
        self.__estado=estado
        self.__id_reserva=id_reserva
    def getDatos(self):
        return self.__numero,self.__fecha+" "+self.__precio+" "+self.__estado+" "+self.__id_reserva
class Restaurante(Factura):
    def __init__(self,nombre,documento,metodo_pago,num_hab,id_Reserva,total):
        self.__nombre=nombre
        self.__documento=documento
        self.__metodo_pago=metodo_pago
        self.__num_hab=num_hab
        self.__id_Reserva=id_Reserva
        self.__total=total
    def getFacturarestaurante(self):
        return self.__nombre,self.__documento,self.__metodo_pago,self.__total,self.__num_hab,self.__id_Reserva
class Lavandería(Factura):
    def __init__(self, num_hab,método_pago,num_factura,total):
        self.__num_hab=num_hab
        self.método_pago=método_pago
        self.__num_factura=num_factura
        self.__total=total
    def getLav(self):
        return self.__num_hab, self.__total, self.método_pago, self.__num_factura