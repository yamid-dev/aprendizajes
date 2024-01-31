'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
 como el número introducido.'''

nom=input("¿Cuál es tu nombre? ")
rep=int(input("Número de veces a repetir: "))
print(f"{nom}\n"*rep)