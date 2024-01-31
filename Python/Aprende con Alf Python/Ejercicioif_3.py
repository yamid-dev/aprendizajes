'''Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.'''

dividendo=int(input("Dividendo: "))
divisor=int(input("Divisor: "))
if divisor==0:
    print("ERROR")
else:
    print(f'''
            {dividendo}
            ______=  {dividendo//divisor}
            {divisor} ''')