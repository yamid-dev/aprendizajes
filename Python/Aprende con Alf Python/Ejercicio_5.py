'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
 Después debe mostrar por pantalla la paga que le corresponde.'''

horas=int(input("Horas trabajadas: "))
coste=int(input("Coste por hora: "))
print(f"Paga:  ${horas*coste}")