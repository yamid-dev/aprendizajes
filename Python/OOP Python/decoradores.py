#Decoradores  = función especial que decora a otra. El decorador no agarra la función y la modifica, sino que le agrega funcionalidad antes y/o después de ejecutarla.

#Decoradores multiples: Capacidad de aplicar más de un decorador a una función o método. Esto permite modulizar y organizar el código de manera más eficiente, ya que te permite aplicar múltiples transformaciones o funcionalidades a una función o método de forma transparente y ordenada.

def decorador1(function):
    def wrapper():
        print("Antes del primer decorador")
        function()
        print("Después del primer decorador")
    return wrapper

def decorador2(function):
    def wrapper():
        print("Antes del segundo decorador")
        function()
        print("Después del segundo decorador")
    return wrapper

@decorador1
@decorador2
def function_decorada():
    print("¡Función decorada!")
    
function_decorada()