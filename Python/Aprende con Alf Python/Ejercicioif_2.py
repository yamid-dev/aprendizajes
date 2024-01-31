'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario 
coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.'''

contraseña="hola mundo"
password=""
while contraseña!=password:
    password=input("Escribe tu contraseña: ")
    if contraseña==password.lower():
        print("Contraseña válida, bienvenido :)")
    else:
        print("Contraseña invalida, intentalo de nuevo")