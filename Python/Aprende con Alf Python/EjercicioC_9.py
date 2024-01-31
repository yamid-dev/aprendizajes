'''Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.'''

fecha=input("Fecha de nacimiento (dd/mm/aaaa): ")
print(f'''
dia: {fecha[:2]} 
mes: {fecha[5:6]}
''')