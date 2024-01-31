'''Escribir un programa que lea un entero positivo, 
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
n. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma: ((n*(n+1))//2)'''

n=int(input("Número: "))
print(f"La suma de todos los números hasta {n} es ",((n*(n+1))//2))