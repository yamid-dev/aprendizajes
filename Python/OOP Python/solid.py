#SRC,OCP,LCP,ISP,DIP
#PRINCIPIO ABIERTO/CERRADO (OCP) = LAS CLASES, LOS MODULOS, LAS FUNCIONES TIENEN QUE ESTAR ABIERTAS PARA LA EXTENSION PERO CERRADAS PARA LA MODIFICACIÓN. NO ES BUENO MODIFICAR EL CÓDIGO DE UNA CLASE

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError
    
class Notificador_Email(Notificador):
    def notificar (self):
        print(f"Enviando mensaje a {self.usuario.email}")

class Notificador_SMS(Notificador):
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.sms}")

class Notificador_Whatsapp(Notificador):
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.whatsapp }")

#Puedo agregar más implementaciones de la clase Notificador, pero no estoy modificando la misma cumpliendo de esta manera el principio de abierto/cerrado
class Notificador_Twitter(Notificador):
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.twitter}")
