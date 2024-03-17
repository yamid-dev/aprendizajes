#polimorfismo = Muchas formas. Poder enviarle un mensaje sintactico a diferentes objetos pero el mensaje es el mismo pero el resultado que nos tiene que generar es distinto por sus propiedades entendiendo que estas son diferentes

#Por ejemplo le digo a un objeto de la clase SerVivo que camine, ser_humano caminará de una manera, gato caminará de una manera y cien_pies caminará de otra manera

#Todas las variables en Python solo polimorfas (polimorfismo en tiempo de ejecución o de inclusión)

class Gato:
    def sonido(self):
        return "Miau"
class Perro:
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())    

gato = Gato()
perro = Perro()

#esto es polimorfismo porque el mensaje es el mismo solo que estoy cambiando el objeto en el que estoy implementando este método
hacer_sonido(perro)
hacer_sonido(gato)