from Empresa import *
class cliente(Empresa):
    def __init__(self,nombre,teléfono):
        Empresa.__init__(self,nombre,teléfono)
    def getdatos(self):
        print(super().getnombre())
        print(super().getTeléfono())