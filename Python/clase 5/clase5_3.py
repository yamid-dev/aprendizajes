from math import sqrt
cateto1=int(input("Cateto opuesto: "))
cateto2=int(input("Cateto adyacente: "))
if cateto1<=0 and cateto2<=0:
    print("No es un triangulo")
else:
    hipotenusa=((cateto1**2)+(cateto2**2))**0.5
    print(hipotenusa)
print("______________________________________")
cateto1=int(input("Cateto opuesto: "))
cateto2=int(input("Cateto adyacente: "))
if cateto1<=0 and cateto2<=0:
    print("No es un triangulo")
else:
    hipotenusa=sqrt((cateto1**2)+(cateto2**2))
    print(hipotenusa)