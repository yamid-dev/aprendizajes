#mro = metodo de resolución de orden.  Determinar el orden en el que buscará los métodos y atributos de esas clases base cuando se llame a un método o se acceda a un atributo desde una instancia de esa clase derivada.

class A:
    def hablar(self):
        print("Hablando desde A")

class B(A):
    def hablar(self):
        print("Hablando desde B")

class C(A):
    def hablar(self):
        print("Hablando desde C")

class D(B,C):
    def hablar(self):
        print("Hablando desde D")

d=D()
d.hablar()