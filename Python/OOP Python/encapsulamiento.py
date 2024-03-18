class MiClase:
    def __init__(self):
        #Atributo muy privado
        self.__atributo_privado = "Valor"
    #Método muy privado
    def __hablar(self):
        print("Hola, estoy hablando")
        
objeto = MiClase()
print(objeto.__hablar()) 

#El atributo privado de python es el protedigo de otros lenguajes y el atributo mu privado es el privado de otros lenguajes

#Getters y Setters: Getters obtenedor y setters establecedor. 