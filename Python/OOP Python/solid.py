#SRC,OCP,LCP,ISP,DIP
#PRINCIPIO DE SEGREGACIÓN DE LA INTERFAZ (ISP) = Ningun cliente tiene que ser forzado a depender de interfaces que no utilice.

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass
class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

#Esto no violará el principio de segregación de interfaces
class Humano(Trabajador,Durmiente,Comedor):
    def comer(self):
        print("El humano está comiendo")
    def trabajar(self):
        print("El humano está trabajando")
    def dormir(self):
        print("El humano está durmiendo")

class Robot(Trabajador):
    
    def trabajar(self):
        print("El robot está trabajando")

robot = Robot()
robot.trabajar()