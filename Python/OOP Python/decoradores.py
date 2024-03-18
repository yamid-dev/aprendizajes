#Decoradores  = función especial que decora a otra. El decorador no agarra la función y la modifica, sino que le agrega funcionalidad antes y/o después de ejecutarla.

#Decoradores de clases: Son funciones que toman una clase como argumento y devuelven una clase modificada o extendida de alguna manera. Se utlizan para modificar el comportamiento de una clase sin camvbiar su implementación directamente. Proporciona una forma elegante y reutlizable de agregar funcionalidades adicionales a las  clases
# def decorador_clase(cls):
#     class NuevaClase:
        #*args es un parametro especial que se utiliza en la definición de funciones para indicar que la función puede aceptar un número variable de argumentos posicionales. Los argumentos pasados se recopilan en nuestra tupla dentro de la función
        
        #**kwargs es un parámetro especial que se utiliza en la definición de funciones para indicar que la función puede aceptar un número variable de argumentos de palabra clave (con nombres). Los argumentos pasados se recopilan en un diccionario dentro de la función
'''
EJEMPLO DE ARGS
'''
def suma(*args):
    total = 0
    for num in args:
        total += num
    return total
print(suma(1,2,3,4,5))

'''
EJEMPLO DE  KWARGS
'''


        # def __init__(self,*args,**kwargs):
        #     self.objeto_original = cls(*args,**kwargs)
        #     self.atributo_nuevo = "Atributo añadido por el decorador"
        
        #getarr es una función integrada de Python que se utiliza para obtener el valor de un atributo de un objeto dado su nombre. Toma tres argumentos: objeto del que se quiere obtener el atributo, el nombre del atributo y opcionalmente un valor por defecto que se volverá si el atributo no existe
    #     def __getattr__(self,nombre):
    #         return getattr(self.objeto_original,nombre)
    # return NuevaClase

# @decorador_clase
# class MiClase:
#     def __init__(self,valor):
#         self.valor = valor
    
#     def metodo(self):
#         print("Método original")
        
# objeto = MiClase(10)

# print(objeto.valor)
# objeto.metodo()

# print(objeto.atributo_nuevo)
#Decoradores multiples: Capacidad de aplicar más de un decorador a una función o método. Esto permite modulizar y organizar el código de manera más eficiente, ya que te permite aplicar múltiples transformaciones o funcionalidades a una función o método de forma transparente y ordenada.
