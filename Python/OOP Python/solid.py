#SRC,OCP,LCP,ISP,DIP
#PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP) =  Las clases derivadas deben ser sustituidas por sus clases base

#ESTO NO CUMPLE EL PRINCIPIO DE SUSTITUCIÓN DE LISKOV PORQUE EL PINGUINO DEBERÍA VOLAR SI HEREDA DE LA CLASE AVE.
# class Ave:
#     def volar(self):
#         return "Estoy volando"
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"
    
# def hacer_volar(ave = Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))

#ESTO SERÍA APLICAR EL PRINCIPIO DE SUSTITUCIÓN DE LISKOV
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"

class AveNoVoladora(Ave):
    pass