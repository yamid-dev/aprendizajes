def mensaje():
    print("ACCESO PERMITIDO")
print("__________________________________________")
invitados=[1010101010,2020202020,3030303030,4040404040,5050505050,1005060791]
inp=int(input("Documento: "))
if inp in invitados:
    print("PERMITIDO ENTRAR")
else:
    print("ACCESO DENEGADO: LLAME A LA POLICIA!")
print("__________________________________________")
if inp==invitados[0]:
    mensaje()
elif inp== invitados[1]:
    mensaje()
elif inp== invitados[2]:
    mensaje()
elif inp== invitados[3]:
    mensaje()
elif inp== invitados[4]:
    mensaje()
else:
    print("ACCESO DENEGADO: LLAME A LA POLICIA!")