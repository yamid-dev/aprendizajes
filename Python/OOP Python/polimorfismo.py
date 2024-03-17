#polimorfismo = Muchas formas. Poder enviarle un mensaje sintactico a diferentes objetos pero el mensaje es el mismo pero el resultado que nos tiene que generar es distinto por sus propiedades entendiendo que estas son diferentes

#Por ejemplo le digo a un objeto de la clase SerVivo que camine, ser_humano caminará de una manera, gato caminará de una manera y cien_pies caminará de otra manera

#Todas las variables en Python solo polimorfas (polimorfismo en tiempo de ejecución o de inclusión)

#Python: Si camina como un pato, y suena como un pato entonces es un pato

#Esto es polimorfismo de herencia o de subclases
class Animal:
    def sonido(self):
        pass
    
class Gato(Animal):
    def sonido(self):
        return "Miau"

class Perro(Animal):
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

#esto es polimorfismo porque el mensaje es el mismo solo que estoy cambiando el objeto en el que estoy implementando este método
hacer_sonido(perro)

#Polimorfismo de sobrecarga = Te permite crear una clase con un mismo método pero depende de los parametros que le pases se convierta de un modo u otro