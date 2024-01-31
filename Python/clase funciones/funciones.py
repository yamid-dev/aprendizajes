#print()
#len()
#join()
#split()
txt=open("Funciones.txt","w")
nombre=list(input('''
Ingrese su nombre completo: 
'''))
cadena=("".join(nombre))
txt.write(f'''
Nombre:{cadena}
Palabra por palabra: {((str((cadena).split(" ")).replace("[","")).replace("]",""))}
Letra por letra: {((str((" ".join(nombre)).split(" ")).replace("[","")).replace("]",""))}
Número de letras de su nombre: {len((" ".join(nombre).replace(" ","")))}
Su nombre en mayuscula: {(cadena).upper()}
Su nombre en minuscula: {(cadena).lower()}
Rango de la lista de letras de tu nombre: {list(range(len(cadena)))}
''')
d=[]
d={"a":1,"b":2,"c":3}
m=(max(d))
x=list(range(11))
txt.write(f"""
Lista de numeros:
{x}
""")
t=tuple(x)
txt.write(f"""Valor ASCII de la cadena {m}: {ord(m)}
""")
num=123.456
txt.write(f"""Valor redondeado de {num}: {round(num)}""")
print('LA INFORMACIÓN HA SIDO REGISTRADA EN EL ARCHIVO "Funciones.txt"')
txt.close()
y=open("Funciones.txt","r")
u=y.read()
print(u)
y.close()

with open("Fuunciones.py","w") as variables:
    variables.writelines("""
a=1
b=2
c="hola","mundo","hermoso"
print(a+b)
print(" ".join(c))
d="Hola mundo"
print(d.split(" ",","))
""")
    
txt="Miguel es mi amigo"
print(txt.replace(" mi"," tu"))