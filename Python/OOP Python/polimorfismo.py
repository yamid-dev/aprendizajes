def recorrer(elemento):
    for item in elemento:
        print(f'El elemento actual es: {item}')

lista=[1,2,3,[4,5,6]]
lista2=["Maria","Juan",["Maria","Cristina","Ocampo"]]
palabra="polimorfismo"

#Esto es polimorfismo pues implementamos el mismo método para diferentes objetos
recorrer(lista)
recorrer(lista2)
recorrer(palabra)

#Duck Typing = Se refiere al enfoque de determinar el tipo de un objeto basado en su comportamiento en lugar de en su tipo espífico. "SI PARECE UN PATO, NADA COMO PATO Y GRAZNA COMO UN PATO, ENTONCES PROBABLEMENTE ES UN PATO". En lugar de enfocarse por el tipo específico de un objeto, nos enfocamnos en lo que ese objeto puede hacer, es decir, qué metodos o atributos soporta

#se trata de un símil en el que los patos son objetos y hablar/andar métodos. Es decir, que si un determinado objeto tiene los métodos que nos interesan, nos basta, siendo su tipo irrelevante. El concepto de duck typing se fundamenta en el razonamiento inductivo, donde una serie de premisas apoyan la conclusión, pero no la garantizan. 

#Dicho de otra manera, no mires si es un pato. Fíjate si habla como un pato, camina como un pato, etc. Si cumple con todas estas características, ¿no podríamos acaso decir que se trata de un pato?

#Es una filosofía de diseño de código que fomenta la felxibilidad y la reutlización, permitiendo que los programadores se concentren en lo que un objeto puede hacer. en lugar de en lo que es. Sin embargo, tambi´3n requiere una comprensión clara del comportamiento esperado de los objetos de un programa.

#El Duck typing es una forma de tipado estructural que permite definir interfaces de objetos, que no estando relacionados, se comportan de forma similar. Es decir, si el objeto cumple con la interfaz definida, entonces es un pato (dando igual que sea un pato o una gallina).


'''Ejemplo de Duck Typing:
class Pato:
    def quack(self):
        print("¡Quack!")

class Persona:
    def quack(self):
        print("¡Imitando un pato!")

def hacer_quack(objeto):
    objeto.quack()

pato = Pato()
persona = Persona()

hacer_quack(pato)     # Salida: ¡Quack!
hacer_quack(persona)  # Salida: ¡Imitando un pato!

'''
#Enlaces dínamicos: En Python, el enlace de métodos y funciones es dinámico por naturaleza. Esto significa que la resolución de qué método o función se invoca se realiza en tiempo de ejecución, basándose en el tipo real del objeto al que se refiere la referencia.

'''
Los términos "enlaces dinámicos" y "enlaces estáticos" se refieren a cómo se resuelven las referencias a funciones o métodos durante la ejecución de un programa, especialmente en el contexto de los lenguajes de programación.
'''

#Enlaces estáticos:En el enlace estático, las referencias a funciones o métodos se resuelven en tiempo de compilación. Esto significa que el compilador determina qué función o método se invocará en tiempo de ejecución y genera el código necesario para realizar la llamada directamente.

#El enlace estático tiene la ventaja de ser más eficiente en términos de rendimiento, ya que no se necesita realizar ninguna búsqueda en tiempo de ejecución para determinar qué función o método se debe llamar. Sin embargo, esto también significa que las referencias a funciones o métodos son fijas y no pueden cambiar durante la ejecución del programa.


#Tipo real vs Tipo declarado:  se refieren a la diferencia entre el tipo de datos que realmente contiene un objeto en tiempo de ejecución y el tipo de datos que se declara o especifica en el código.

#Tipo Declarado: Es el tipo de datos que se especifica explícitamente al declarar una variable o un objeto en el código. Este tipo se conoce en tiempo de compilación y se utiliza por el compilador para realizar verificaciones de tipo estático y para asignar memoria adecuada para el objeto.
'''
// Tipo declarado: Animal
Animal animal = new Perro();

En este caso, animal se declara como tipo Animal, pero en tiempo de ejecución realmente contiene un objeto de tipo Perro. El tipo declarado Animal es utilizado por el compilador para verificar que animal solo pueda acceder a los miembros de la clase Animal.
'''

#Tipo Real: Es el tipo de datos que realmente contiene un objeto en tiempo de ejecución. Este tipo es determinado por la clase concreta del objeto que se ha creado y asignado a la variable.

'''
// Tipo declarado: Animal
// Tipo real: Perro
Animal animal = new Perro();

En este caso, el tipo real del objeto al que apunta animal es Perro. Aunque se declara como tipo Animal, en tiempo de ejecución contiene un objeto de tipo Perro.
'''

# La diferencia entre el tipo declarado y el tipo real es relevante especialmente en el contexto de la herencia y la polimorfismo. El tipo declarado determina qué métodos y miembros pueden accederse a través de la variable, mientras que el tipo real determina qué implementación específica de esos métodos se ejecutará en tiempo de ejecución. 