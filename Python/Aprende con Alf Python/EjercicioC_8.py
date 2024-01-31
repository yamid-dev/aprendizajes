'''Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del
 precio introducido.'''
 
precio=input("Precio en euros: ")
vof="." in precio
if vof==True:
    print(precio[:precio.find(".")]+""+" euros y "+precio[precio.find(".")+1:]+" centavos")
else:
    print(precio+" euros y 0 centavos")