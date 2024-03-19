
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
    
    #property es un decorador especial porque es un decorador reservado para las clases, que le dice esto es un getter, usalo como una propiedad
    @property
    def nombre(self):
        return self.__nombre


persona = Persona("Yamid",21)

#property le dice no trates el getter como una función sino como una propiedad, compara con el archivo de encapsulamiento
nombre = persona.nombre
persona.nombre = "Horacio"
print(nombre)
