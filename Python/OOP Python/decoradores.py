#Decoradores  = función especial que decora a otra. El decorador no agarra la función y la modifica, sino que le agrega funcionalidad antes y/o después de ejecutarla.

def decordador(function):
    def function_modificada():
        print("Antes de llamar a la función")
        function()
        print("Después de llamar a la función")
    return function_modificada

# def saludo():
#     print("Hola Yamid")
    
# saludo_modificado = decordador(saludo)

# saludo_modificado()

@decordador
def saludo():
    print("Hola Yamid")

saludo()

#Decoradores de clases: Son funciones que toman una clase como argumento y devuelven una clase modificada o extendida de alguna manera. Se utlizan para modificar el comportamiento de una clase sin camvbiar su implementación directamente. Proporciona una forma elegante y reutlizable de agregar funcionalidades adicionales a las  clases

#Decoradores multiples: Capacidad de aplicar más de un decorador a una función o método. Esto permite modulizar y organizar el código de manera más eficiente, ya que te permite aplicar múltiples transformaciones o funcionalidades a una función o método de forma transparente y ordenada.
