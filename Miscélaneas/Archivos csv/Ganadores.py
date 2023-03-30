class Ganadores:
    def __init__(self,índice,año,edad,nombre,película):
        self.__índice=índice
        self.año=año
        self.edad=edad
        self.nombre=nombre
        self.película=película
    def getdatos(self):
        return self.__índice+" "+self.nombre+" "+self.película