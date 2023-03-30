class Empresa:
    def __init__(self,nombre,teléfono):
        self.nombre=nombre
        self.__teléfono=teléfono
    def getnombre(self):
        return self.nombre
    def getTeléfono(self):
        return self.__teléfono
