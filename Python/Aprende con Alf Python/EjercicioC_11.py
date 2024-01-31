'''Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido 
de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.'''

producto=input("Nombre: ")
precio=float(input("Precio del producto: "))
cantidad=int(input("Número de unidades: "))
print(f"{producto}: {precio:9.2f}€ x {cantidad:3d} unidades= {(precio*cantidad):11.2f}€")