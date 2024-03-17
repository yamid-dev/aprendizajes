#Ejercicio 2: Crear un sistema para el modelado de animales de un zoológico
#Clases: Animal,Mamifero,Ave, Murcielago
#Metodos: Animal(comer()), Mamifero(amamntar()), Ave(volar())
#Crea una clase Murcielago que hereda de Mamifero y Ave, ese orden, y por lo tanto ser capaz de amamantar y volar, además comer. Finalmente, juega con el orden de herencia de la clase Murcielago y observa como cambia el MRO y el comportamiento de los métodos al usar super() 

class Animal:
    def comer(self):
        print("El animal está comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando")

class Ave(Animal):
    def volar(self):
        print("El animal está volando")

class Murcielago(Ave,Mamifero):
    pass

murcielago = Murcielago()
murcielago.comer()
murcielago.amamantar()
murcielago.volar()
print(Murcielago.mro())
