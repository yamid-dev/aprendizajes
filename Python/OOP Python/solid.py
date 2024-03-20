#SRC,OCP,LCP,ISP,DIP
#PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP) = Establece dos cosas:

#1- Los módulos de alto nivel no tienen que depender de los de bajo nivel, sino que los dos tienen que depender de las abstracciones.
#2- Las abstracciones no deben depender de los detalles, sino los detalles depender de las abstracciones.

class Diccionario:
    def verificar_palabra(self,palabra):
        #Lógica para verificar palabras
        pass

#la clase más importante es corrector ortográfico y está dependiendo de la clase Diccionario que es una 'mini-interfaz'
class CorrectorOrtografico:
    def __init__(self):
        self.diccionario = Diccionario()
    def corregir_texto(self,texto):
        #usamos el diccionario para corregir el texto
        pass