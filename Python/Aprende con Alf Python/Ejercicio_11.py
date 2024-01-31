'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año,
 se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
 introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
 Redondear cada cantidad a dos decimales.'''

dinero=float(input("Ahorro inicial: "))
a_1=dinero*(1+0.04)
a_2=a_1*(1+0.04)
a_3=a_2*(1+0.04)
print(f"""
Año 1: ${round(a_1,2)}
Año 2: ${round(a_2,2)}
Año 3: ${round(a_3,2)}""")