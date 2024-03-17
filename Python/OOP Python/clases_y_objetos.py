#EstoEsPascalCase
#estoEsCamelCase
#esto_es_snake_case

#Esto es una clase llamada Celular
class Celular():
    #metodo constructor = metodo especial que cada vez que instanciamos esta clase automaticamente se ejecuta el método constructor.
    def __init__(self,marca,modelo,camara): #self es una forma de hacer referencia a si mismo, al mismo objeto.
        self.marca = marca #esto es como decir celular 1|2|3.marca = marca
        self.modelo = modelo
        self.camara = camara
    #metodo = acciones o funciones que puede realizar nuestro objeto
    def llamar(self):
        return(f"Estas haciendo un llamado desde un: {self.modelo}")

    def cortar(self):
        return(f"Cortaste la llamada desde tu: {self.modelo}")


#Estas son instancias de la clase Celular
celular1= Celular("Samsung","S23","48MPX") #Aquí ingresamos atributos basandonos en el método constructor que nos permite reutilizar código.

celular2= Celular("Apple","Iphon 15","PRO")

print(celular2.llamar())
print(celular2.cortar())