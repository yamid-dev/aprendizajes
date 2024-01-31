#if y else (condicionales), ejemplo
x = 10
y = 5
if x > y:
    resultado = "x es mayor que y"
    print(resultado)
else:
    resultado = "y es menor o igual a x"
    print(resultado)
print("_________________________________________")
a=2+2
if a==4: #condicion si es exactamente cuatro, entonces:
    print("A es igual a 4")
print("_________________________________________")  
a=2+3
if a==4: #condicion si es exactamente cuatro, entonces:
    print("A es igual a 4") #imprimir
elif a==5: #condicion si es exactamente cinco, entonces:
    print("A es igual a 5")#imprimir
elif a==6: #condicion si es exactamente seis, entonces:
    print("A es igual a 6") #imprimir
else:
    print("No se cumple la condición") #imprimir
print("_________________________________________")
if a==4:
    print("A es igual a 4")
else:
    if a==5:
        print("A es igual a 5")
    else:
        if a==6:
            print("A es igual a 6")
        else:
            print("No se cumple la condición")
print("________________________________________")
#ejercicio compra de libros 1
libro=25
comprador=100
if comprador>=25:
    print("VENDER")
else:
    print("NO SE VENDE")
print("________________________________________")
#ejercicio compra de libros 2
libro=25
comprador=int(input("Cantidad de dinero del que dispone el comprador: "))
if comprador<25:
    print("Saldo insuficiente para esta compra")
else:
    cant=int(input("Cantidad de libros que desea comprar: "))
    x=libro*cant
    dif=comprador-x
    if dif<0:
        print(f"Deficit: ${abs(dif)}")
    else:
        print(f"Cambio: ${dif}")