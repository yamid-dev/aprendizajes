#métodos especiales = son funciones que tienen un nombre especial reservado (__nombre_metodo_especial__) creados con la única finalidad de que nosotros podamos crear funcionalidades especiales que con métodos normales no podríamos

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    #el método especial str que devuelve una representacion del objeto en una cadena de texto
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'

persona = Persona("Yamid",21)
repre = repr(persona) #repre es la representación del objeto para luego reconstruirlo
resultado = eval(repre) #resultado ya es el objeto reconstruido, eval se utiliza para evaluar una cadena de texto que representa una expresión o declaración en Python. En este caso repre contiene una representación en forma de cadena del objeto Persona generada utilizando __repr__.

#Cuando se llama eval(repre) se evalua la cadena repre, que contiene la representación de la instancia de la clase Persona. Esto tiene en el efecto de reconstruir un nuevo objeto Persona utilizando la cadena de representación. En esencia, 'eval' ejecuta el código representado por la cadena. Se debe utilizar con precaución especialmente en aplicaciones que interactuan con usuarios externos o datos no confiables ya que ejecuta el código de la cadena de manera directa y puede ser una puerta trasera pra inyección de código malicioso.

print(repre)
print(resultado.nombre)