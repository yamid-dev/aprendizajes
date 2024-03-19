#Ejercicio 3: Crear un juego de fusión
'''El juego consiste en crear personajes un juego y que esos personajes se puedan fusionar para formar personajes más poderosos que tengan más poder...

Para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes se fusionen, salga un nuevo personaje con habilidades mejoradas

Una posible formula es: el promedio de las habilidades de ambos al cuadrado'''

class Personaje:
    def __init___(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    def __repr__(self):
        return f"{self.nombre} (fuerza: {self.fuerza}, velocidad: {self.velocidad})"
    
goku = Personaje("Goku",100,100)
print(goku)