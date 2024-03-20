#SRC,OCP,LCP,ISP,DIP
#PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRC) =  Una clase solo tiene que tener una responsabilidad o tarea, tiene que tener una y solo una razón para cambiar.


#ESTO SI SIGUE EL PRINCIPIO DE RESPONSABILIDAD ÚNICA SRC.
class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion +=distancia
            self.tanque.usar_combustible(distancia/2)
            return "El auto se está moviendo"
        else:
            return "No hay sufisciente combustible"
    def obtener_posicion(self):
        return self.posicion

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self,cantidad):
        self.combustible +=cantidad
    
    def obtener_combustible(self):
        return self.combustible
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad
tanque = TanqueDeCombustible()
autito = Auto(tanque)
print(autito.obtener_posicion())
print(autito.mover(10))
print(autito.obtener_posicion())
print(autito.mover(20))
print(autito.obtener_posicion())
print(autito.mover(60))
print(autito.obtener_posicion())
print(autito.mover(100))
print(autito.obtener_posicion())
print(autito.mover(100))
print(autito.obtener_posicion())
