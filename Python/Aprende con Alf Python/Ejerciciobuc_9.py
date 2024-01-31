'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''
contraseña="nidian56"
password=input("Ingrese tu contraseña: ")
while password!=contraseña:
    password=input("Contraseña incorrecta. Ingrese una nueva contraseña: ")
print("¡Bienvenid@!")