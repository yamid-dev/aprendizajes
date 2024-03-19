#métodos especiales = son funciones que tienen un nombre especial reservado (__nombre_metodo_especial__) creados con la única finalidad de que nosotros podamos crear funcionalidades especiales que con métodos normales no podríamos

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    #el método especial str que devuelve una representacion del objeto en una cadena de texto
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'

persona = Persona("Yamid",21)
print(persona)