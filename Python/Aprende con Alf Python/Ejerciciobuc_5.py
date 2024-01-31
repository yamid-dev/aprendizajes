'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión 
cada año que dura la inversión. '''

cantidad=float(input("Cantidad a invertir: "))
interes=float(input("Interes anual: "))
años=int(input("Número de años: "))
for i in range(años):
   porc=cantidad*(interes/100)
   x=cantidad
   cantidad=cantidad+porc
   print(f"Año {i+1}: "+str(cantidad))
