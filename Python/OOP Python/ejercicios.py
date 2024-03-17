#Ejercicio 2: Crear un sistema para una escuela
#Clases: Persona, Estudiante
#Atributos: Persona(nombre, edad) ,Estudiante(Personas(),grado)
#Metodos: Persona(presentacion(nombre,edad), grado())
#Reutilizar el codigo de la clase padre Persona, luego crea una instancia de la clase Estudiante e imprime sus atributos, además utiliza sus métodos

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def presentacion(self):
        print(f"Mi nombre es {self.nombre} y mi edad es {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def grad(self):
        print(f"Grado: {self.grado}")

yamid = Estudiante('Yamid',21,'5 semestre')
print(f'''
DATOS DEL ESTUDIANTE: 
Nombre: {yamid.nombre}
Edad: {yamid.edad}
Grado: {yamid.grado}
''')
yamid.presentacion()
yamid.grad()