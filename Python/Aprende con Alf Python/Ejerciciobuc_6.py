'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.'''
num=int(input("Tamaño del triangulo rectangulo: "))
x=" *"
for i in range(num):
    print(x*i)