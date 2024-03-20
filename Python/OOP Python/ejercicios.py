#Ejercicio 3: Crear un juego de fusión
'''El juego consiste en crear personajes un juego y que esos personajes se puedan fusionar para formar personajes más poderosos que tengan más poder...

Para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes se fusionen, salga un nuevo personaje con habilidades mejoradas

Una posible formula es: el promedio de las habilidades de ambos al cuadrado'''

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    def __repr__(self):
        return f"{self.nombre} (fuerza: {self.fuerza}, velocidad: {self.velocidad})"
    def __add__(self,otro_pj):
        nuevo_nombre = self.nombre+"+"+otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
    
goku = Personaje("Goku",100,100)
vegeta= Personaje("Vegeta",99,99)
jiren = Personaje("Jiden",130,140)
gogeta=goku+vegeta
jireta = gogeta+jiren
print(jireta)
print(gogeta)
print(goku)
print(vegeta)
print(jiren)