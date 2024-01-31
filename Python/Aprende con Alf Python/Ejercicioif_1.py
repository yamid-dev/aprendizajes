'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.'''
edad=int(input("¿Cuál es tu edad?: "))
if edad>=18 and edad<=115:
    print("MAYOR DE EDAD")
elif edad<18 and edad>=0:
    print("MENOR DE EDAD")
else:
    print("EDAD INVALIDA")