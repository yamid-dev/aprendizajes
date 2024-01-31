'''Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	                Tipo impositivo
Menos de 10000€	        5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	        45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.'''

ra=float(input("Renta anual: "))
if ra<10000:
    print(f"Tramo impositivo: {ra+(ra*0.05)}€")
elif ra>=10000 or ra<=20000:
    print(f"Tramo impositivo: {ra+(ra*0.15)}€")
elif ra>20000 or ra<35000:
    print(f"{ra*0.20}")
elif ra>=35000 or ra<=60000:
    print(f"Tramo impositivo: {ra+(ra*0.30)}€")
elif ra>60000:
    print(f"Tramo impositivo: {ra+(ra*0.45)}€")
else:
    print("ERROR")