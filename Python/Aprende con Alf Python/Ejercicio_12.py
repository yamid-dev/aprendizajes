'''Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras
 vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.'''

precio_barra=3.49
barras_nv=int(input("Barras vendidas que no son del dia: "))
precio=barras_nv*precio_barra
desc=(precio)*0.6

print(f"""Precio habitual de una barra de pan: {precio_barra}€

Total sin descueto: {round((precio),2)}€
Descuento: {desc}€ 

Coste final: {round((precio-desc),2)}€ """)