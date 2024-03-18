
#Getters y Setters: Getters obtenedor y setters establecedor. Dos métodos para acceder a propiedades privadas que tienen las clases o incluso modificarlas.
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
   
    #Getter es un método que nos permite acceder a un valor "privado" o "muy privado"
    def get_nombre(self):
        return self.__nombre
    
    #Setter es un método que permite establecer un valor "privado" o "muy privado"
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

#En este bloque instancié un objeto de la clase Persona, después accedí a un atributo privado nombre con el getter, lo imprimí, establecí un nuevo nombre con setter, después volví a acceder al mismo con getter para finalmente volverlo a imprimir
persona = Persona("Yamid",21)
nombre = persona.get_nombre()
print(nombre)
persona.set_nombre("Pepito")
nombre = persona.get_nombre()
print(nombre)

