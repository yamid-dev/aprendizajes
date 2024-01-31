'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
 Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y 
 todos los ingredientes que lleva.'''

tipo=input("¿Quieres pizza vegetariana? (SI O NO): ")
if tipo.upper()=="SI":
    print('''
    Menú: 
    1. Pimientos
    2. Tofu
    ''')
    tip=" Vegetariana"
    ing=int(input("Elige una opción: "))
    if ing==1:
        ing="Pimientos"
    else:
        ing="Tofu"
else:
    print('''
    Menú:
    1. Peperoni
    2. Jamón
    3. Salmón
    ''')
    tip=" No vegetariana"
    ing=int(input("Elige una opción: "))
    if ing==1:
        ing="Peperoni"
    elif ing==2:
        ing="Jamón"
    elif ing==3:
        ing="Salmón"
print(f'''
Pizza: {tip}
Ingredientes: 
1. {ing}
2. Mozzarela
3. Tomate'''
)