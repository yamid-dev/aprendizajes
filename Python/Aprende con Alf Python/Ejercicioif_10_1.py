tipo = input("¿Quieres pizza vegetariana? (SI O NO): ").upper()

if tipo == "SI":
    menu = '''
    Menú: 
    1. Pimientos
    2. Tofu
    '''
    ing = "Pimientos" if int(input(f"{menu}\nElige una opción: ")) == 1 else "Tofu"
else:
    menu = '''
    Menú:
    1. Peperoni
    2. Jamón
    3. Salmón
    '''
    ing = ""
    opcion = int(input(f"{menu}\nElige una opción: "))
    if opcion == 1:
        ing = "Peperoni"
    elif opcion == 2:
        ing = "Jamón"
    elif opcion == 3:
        ing = "Salmón"

print(f'''
Pizza: {"Vegetariana" if tipo == "SI" else "No vegetariana"}
Ingredientes: 
1. {ing}
2. Mozzarela
3. Tomate'''
)