#herencia = pilar fundamental de la OOP que permite a la clase hija acceder a todos los métodos y propiedades de todos los padres por ejemplo: persona y estudiante.

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print ("Hola, estoy hablando un poco...")    
#Esta es una clase hija llamnada Empleado que hereda caracteristicas de la clase padre Persona   
class Empleado(Persona):
    pass
roberto = Empleado("Roberto",43,"Colombiano")

roberto.hablar()
print(roberto.nacionalidad)