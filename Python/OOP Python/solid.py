#SRC,OCP,LCP,ISP,DIP
#PRINCIPIO DE SEGREGACIÓN DE LA INTERFAZ (ISP) = Ningun cliente tiene que ser forzado a depender de interfaces que no utilice.

from abc import ABC, abstractmethod

class Trabajador(ABC):

    @abstractmethod
    def comer(self):
        pass
    @abstractmethod
    def trabajar(self):
        pass
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador):
    def comer(self):
        print("El humano está comiendo")
    def trabajar(self):
        print("El humano está trabajando")
    def dormir(self):
        print("El humano está durmiendo")

#Esto violaría el principio de segregación de interfaz pues un Robot no come ni duerme.
class Robot(Trabajador):
    def comer(self):
        pass
    def trabajar(self):
        print("El robot está trabajando")
    def dormir(self):
        pass