'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.'''

cant=int(input("Cantidad a invertir: "))
int_anual=int(input("Interes anual: "))
años=int(input("Número de años: "))
capital=round(cant*(int_anual/100+1)**años,2)
print(f"Capital obtenido en la inversión: ${capital}, con una diferencia de ${capital-cant} con respecto a la inversión inicial ")