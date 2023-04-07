class Factura:
    def __init__(self, numero, fecha, precio, estado, id_reserva, num_hab):
        self.__numero=numero
        self.__fecha=fecha
        self.__precio=precio
        self.__estado=estado
        self.__id_reserva=id_reserva
        self.__num_hab=num_hab
    def getDatos(self):
        return self.__numero,self.__fecha+" "+self.__precio+" "+self.__estado+" "+self.__id_reserva+""+self.__num_hab
    def Datosrest(self):
        return self.__id_reserva,self.__num_hab
class Restaurante(Factura):
    def __init__(self,nombre,documento,metodo_pago,total,num_hab,id_reserva):
        self.__nombre=nombre
        self.__documento=documento
        self.metodo_pago=metodo_pago
        self.total=total
        self.num_hab=num_hab
        self.id_reserva=id_reserva
    def getFacturarestaurante(self):
        return self.__nombre,self.__documento,self.metodo_pago,self.total
    def Datosrest(self):
        print(super().Datosrest())
