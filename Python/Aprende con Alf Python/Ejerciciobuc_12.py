'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.'''
frase=list(input("Frase: ").upper())
cont=0
letra=input("Letra: ").upper()
for i in range(len(frase)):
    if frase[i]==letra:
        cont+=1
print(f"La letra {letra} se repite {cont} veces")