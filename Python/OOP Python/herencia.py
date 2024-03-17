#herencia = pilar fundamental de la OOP que permite a la clase hija acceder a todos los métodos y propiedades de todos los padres por ejemplo: persona y estudiante.

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print ("Hola, estoy hablando un poco...")    
#Esta es una clase hija llamnada Empleado que hereda caracteristicas de la clase padre Persona   = Herencia simple
class Empleado(Persona): #Superclase es Persona y Empleado es Subclase
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        #constructor dentro de otro constructor
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario  = salario
    #Aquí sobreescribí método
    # def hablar(self):
    #     print("Noooo")

class Estudiante(Persona): #Superclase es Persona y Empleado es Subclase
    def __init__(self,nombre,edad,nacionalidad,universidad,notas):
        #constructor dentro de otro constructor
        super().__init__(self,nombre,edad,nacionalidad)
        self.universidad = universidad
        self.notas  = notas
    #Aquí sobreescribí método
    # def hablar(self):
    #     print("Noooo")

roberto = Empleado("Roberto",43,"Colombiano","programador",1000000)



roberto.hablar()
print(roberto.trabajo)