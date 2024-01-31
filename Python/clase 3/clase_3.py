a=12
b=145
print(f'''
{12}         +        {14}
Operando  Operador Operando
resultado: {12+14}
{a}         +        {b}
Operando  Operador Operando
resultado: {a+b}
''')
print("________________________________________")
#creación de un dato estructurado llamado lista
obj=[] 
obj=[1,2,3,4,5] 
print(type(obj))
#creación de un dato estructurado llamado tupla
list="hola",1,"hol",3 
print(type(list),list[1])
print("________________________________________")
#Uso de datos especiales
a=[1,2,3,4,5]
b=1
c=1
print(b is c)
print( b is not c)
print(5 in a,"/",5 not in a)
print("________________________________________")
# llenar lista con 11 nombres de invitados
lista_invitados = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Julia', 'Kevin']
print("Antonio" in lista_invitados)
print("________________________________________")# Crear un dato estructurado llamado MiDiccionario e ingresar keys "Nombre" con value "Margarita" y "Edad" con 55 y "Genero" con femenino
MiDiccionario = {
    "Nombre": "Margarita", 
    "Edad": 55, 
    "Genero": "femenino"}
print(MiDiccionario["Edad"],MiDiccionario["Genero"],MiDiccionario["Nombre"])
print("________________________________________")
#Crear un diccionario que contenga como keys "Padres" con valor de una lista de nombres de los padres y "Mascota" con value de otra lista de nombres, luego llamar el diccionario padres posicion 0:2
MiDicc= {"Padres": ["Juan", "María","Pablo", "Pedro"], 
         "Mascota": ["Firulais", "Michi"]}
print(MiDicc["Padres"][1:4])

#Crear un input llamado nombre