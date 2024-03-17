#mro = metodo de resolución de orden.  Determinar el orden en el que buscará los métodos y atributos de esas clases base cuando se llame a un método o se acceda a un atributo desde una instancia de esa clase derivada.

class A:
    def hablar(self):
        print("Hablando desde A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass
#D>B>C>A
d=D()
d.hablar()