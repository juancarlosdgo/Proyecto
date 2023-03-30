class lector:
    def __init__(self,nombre,dirección,teléfono):
        self.__nombre=nombre
        self.__dirección=dirección
        self.__teléfono=teléfono
    def getDatos(self):
        return self.__nombre,self.__dirección,self.__teléfono
class estudiante(lector):
    def __init__(self,nombre,dirección,teléfono,código):
        self.__código=código
        lector.__init__(self,nombre,dirección,teléfono)
    def datos(self):
        print(super().getDatos())
    def getcódigo(self):
        return "Estudiante: ",self.__código
class docente(lector):
    def __init__(self,nombre,dirección,teléfono,códigodoc):
        self.__códigodoc=códigodoc
        lector.__init__(self,nombre,dirección,teléfono)
    def dates(self):
        print(super().getDatos())
    def getdocente(self):
        return "Docente",self.__códigodoc
class Pedido:
    def __init__(self,IDusuario,títulomat,códigomat):
        self.__IDusuario=IDusuario
        self.títulomat=títulomat
        self.__códigomat=códigomat
    def getPedido(self):
        return self.__IDusuario,self.títulomat,self.__códigomat
class libro(Pedido):
    def __init__(self,IDusuario,títulomat,códigomat,título,tipo,autor,editorial):
        self.__título=título
        self.tipo=tipo
        self.autor=autor
        self.editorial=editorial
        Pedido.__init__(self,IDusuario,títulomat,códigomat)
    def getLibro(self):
        print(super().getPedido())
    def gettítulo(self):
        return self.__título,self.tipo,self.autor,self.editorial
class revista(Pedido):
    def __init__(self,IDusuario,títulomat,códigomat,título,tipo,autor,editorial):
        self.__título=título
        self.tipo=tipo
        self.autor=autor
        self.editorial=editorial
        Pedido.__init__(self,IDusuario,títulomat,códigomat)
    def getRevista(self):
        print(super().getPedido())
    def getTítuloRe(self):
        return self.__título,self.tipo,self.autor,self.editorial
r=revista("2133","papel","23456","Vampyr","terror","Carolina Andújar","ISBN")
print(r.getTítuloRe())
d=estudiante("Cata","Calle 17 A no.10-32","3102144051","21454")
print(d.getcódigo())