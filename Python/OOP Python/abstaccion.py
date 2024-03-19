class Auto():
    def __init__(self):
        self._estado = "apagado"
        
    def encender(self):
        self._estado ="encendido"
        print("El auto está encendido")
    
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
#Esto es abstracción porque solo estoy poniendo el método conducir sin necesidad de saber cómo se enciende, ni cómo está estructurado todo, etc. El auto se enciende solo y hace ese proceso. Todo lo que debe saber es que cuando llame al método conducir el auto va a arrancar a conducir     
mi_auto = Auto()
mi_auto.conducir()