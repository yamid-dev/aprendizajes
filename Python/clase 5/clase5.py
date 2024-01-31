#Identificar el problema:
    #Calcular la potencia al cuadrado de un número

#Localizamos la formula:
    #X^2=Y

#Variables E/S:
x=int(input("Base de la potencia: "))

#Operamos con las variables:
if x<0:
    print("La potencia no puede ser negativa")
else:
    y=x**2
#Mostrar resultados:
    print("El cuadrado del número",x,"es",y)

#Banco de pruebas o testing:
