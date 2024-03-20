#SRC,OCP,LCP,ISP,DIP
#PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRC) =  Una clase solo tiene que tener una responsabilidad o tarea, tiene que tener una y solo una razón para cambiar.


#ESTO NO SIGUE EL PRINCIPIO DE RESPONSABILIDAD ÚNICA
class Auto():
    def __init__(self):
        self.posicion = 0
        self.combustible = 100
    def mover(self,distancia):
        if self.comustible >= distancia/2:
            self.posicion +=distancia
            self.combustible -= distancia/2
        else:
            print("No hay suficiente combustible")
    def agregar_combustible(self,cantidad):
        self.combustible +=cantidad
    
    def obtener_combustible(self):
        return self.combustible
