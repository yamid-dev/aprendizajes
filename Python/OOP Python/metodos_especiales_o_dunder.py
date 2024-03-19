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

#Sobrecarga de operadores = ó operator overloading. Es una caracteristica que permite definir cómo deben comportarse los operadores cuando se aplica a tipos de datos personalizados, como clases y objetos. Permite proporcionar una implementación personalizada para operadores estándar como +,-,*,/,%, ==, !=, etc. en tus propias clases. Puedes definir el significado de estos operadores para tus propios tipos de datos, lo que les permite comportarse de la misma manera que los tipos de datos incorporados por el lenguaje.

'''
Otros métodos especiales:
-------Aritméticos-------
__add__(self,other): Sobrecarga de operador de suma (+)
__sub__(self,other): Sobrecarga de operador de resta (-)
__mul__(self,other): Sobrecarga de operador de multiplicación (*)
__div__(self,other): Sobrecarga de operador de división (/)
__mod__(self,other): Sobrecarga de operador de módulo (%)
__pow__(self,other): Sobrecarga de operador de exponenciación (**)

-------Comparación---------
__eq__(self,other): Sobrecarga de operador de igualdad (==)
__ne__(self,other): Sobrecarga de operador de desigualdad (!=)
__lt__(self,other): Sobrecarga de operador de menor que (<)
__gt__(self,other): Sobrecarga de operador de mayor que (>)
__le__(self,other): Sobrecarga de operador de menor o igual que (<=)
__ge__(self,other): Sobrecarga de operador de mayor o igual que (>=)

-------Asignación---------
__iadd__(self,other): Sobrecarga de operador de suma en asignación (+=)
__isub__(self,other): Sobrecarga de operador de resta en asignación (-=)
__imult__(self,other): Sobrecarga de operador de multiplicación en asignación (*=)
__idiv__(self,other): Sobrecarga de operador de división en asignación (/=)
__imod__(self,other): Sobrecarga de operador de módulo en asignación (%=)
__ipow__(self,other): Sobrecarga de operador de exponenciación en asignación (**=)

-------Otros---------
__str__(self): Sobrecarga de operador str(). Devuelve una representación legible como cadena del objeto
__len__(self): Sobrecarga de operador len(). Devuelve la longitud del objeto
__getitem__(self,index): Sobrecarga del operador de indexación([]). Permite acceder a elementos del objeto por indice
'''