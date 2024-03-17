#herencia = pilar fundamental de la OOP que permite a la clase hija acceder a todos los métodos y propiedades de todos los padres por ejemplo: persona y estudiante.

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print ("Hola, estoy hablando un poco...")   
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")
#Esta es una clase hija llamnada Empleado que hereda caracteristicas de la clase padre Persona   = Herencia simple
class EmpleadoArtista(Persona,Artista): #Superclase es Persona y Empleado es Subclase
    def __init__(self,nombre,edad,nacionalidad,habilidad,empresa,salario):
        #constructor dentro de otro constructor
        super().__init__(nombre,edad,nacionalidad)
        self.habilidad = habilidad
        self.salario  = salario
        self.empresa = empresa
    def presentarse(self):
        return(f'Mi habilidad es: {self.mostrar_habilidad()}')
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

roberto = EmpleadoArtista("Roberto",43,"Colombiano","Cantar","programador",1000000)



roberto.hablar()
roberto.mostrar_habilidad()