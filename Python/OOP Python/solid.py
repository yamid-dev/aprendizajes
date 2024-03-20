#SRC,OCP,LCP,ISP,DIP
#PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP) = Establece dos cosas:

#1- Los módulos de alto nivel no tienen que depender de los de bajo nivel, sino que los dos tienen que depender de las abstracciones.
#2- Las abstracciones no deben depender de los detalles, sino los detalles depender de las abstracciones.

# class Diccionario:
#     def verificar_palabra(self,palabra):
#         #Lógica para verificar palabras
#         pass

# #la clase más importante es corrector ortográfico y está dependiendo de la clase Diccionario que es una 'mini-interfaz'
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
#     def corregir_texto(self,texto):
#         #usamos el diccionario para corregir el texto
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        #logica para verificar palabras
        pass


class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self,palabra):
        #logica para verificar palabras si está en el diccionario
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self,palabra):
        #logica para verificar palabras desde el servicio web
        pass

#CorrectorOrtografico que es la clase principal ya no está dependiendo de Diccionario, ahora está dependiendo de la implementación de Verificador, una clase Abstracta o interfaz.
class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificador = verificador

    def corregir_texto(self,texto):
        #usamos el verificador para corregir texto
        pass

corrector_diccionario = CorrectorOrtografico(Diccionario())
corrector_online = CorrectorOrtografico(ServicioOnline())