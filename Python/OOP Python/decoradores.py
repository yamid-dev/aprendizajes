#Decoradores  = función especial que decora a otra

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