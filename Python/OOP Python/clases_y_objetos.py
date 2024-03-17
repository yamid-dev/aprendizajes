#Ejercicio 1: Crear una clase estudiante que tenga los atributos nombre, edad y grado,además crear un método que se llame estudiar que imprima el mensaje "El estudiante (nombre) está estudiando.Crear una instancia de esta clase y utilizar el método, para esto se debe interactuar con el usuario y este debe brindar los atributos, y a continuación instanciar esta clase y mostrar los datos de la clase creada, si después de registrar al estudiante el usuario escribe estudiar ponen el estudiante a estudiar"

class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        return (f"El estudiante {self.nombre} está estudiando")
while True:    
    print('Ejercicio 1: Ingresa los siguientes datos, al terminar escribe la palabra estudiar para comenzar: \n')

    nombre = input("Escribe tu nombre: ")
    edad = input("Escribe tu edad: ")
    grado = input("Escribe tu grado: ")
    escribir = input(": ")

    if escribir.lower()=="estudiar":
        estudiante= Estudiante(nombre,edad,grado)
        print(f'''
DATOS DEL ESTUDIANTE:
Nombre:{estudiante.nombre} 
Edad: {estudiante.edad}
Grado: {estudiante.grado}
''')
        print(estudiante.estudiar())
        break
    elif escribir.lower()=="cancelar":
        break   
    else:
        print('¡Debes escribir la palabra estudiar para empezar, sino escribe cancelar!')