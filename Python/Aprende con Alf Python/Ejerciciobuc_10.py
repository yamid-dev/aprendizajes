'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.'''
num=int(input("Numero: "))
cont=0
for i in range(9):
    div=num%(i+1)
    if div==0:
        cont+=1
    if cont<=2:
        x=("Es primo")
    else:
        if cont>2:
            x=("No es primo")
print(x)