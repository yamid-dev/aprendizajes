class MiClase:
    def __init__(self):
        #Atributo muy privado
        self.__atributo_privado = "Valor"
        
objeto = MiClase()
print(objeto.__atributo_privado)