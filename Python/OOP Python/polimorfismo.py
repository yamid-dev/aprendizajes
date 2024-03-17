def recorrer(elemento):
    for item in elemento:
        print(f'El elemento actual es: {item}')

lista=[1,2,3,[4,5,6]]
lista2=["Maria","Juan",["Maria","Cristina","Ocampo"]]
palabra="polimorfismo"

#Esto es polimorfismo pues implementamos el mismo método para diferentes objetos
recorrer(lista)
recorrer(lista2)
recorrer(palabra)