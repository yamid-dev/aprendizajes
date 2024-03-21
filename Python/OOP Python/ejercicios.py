#Ejercicio 4 = Chatbot en Python que nos pida que le digamos algo, tome eso que le decimos, analice sentimiento, y responda cuál es el sentimiento

#Este código si cumple los principios SOLID
import openai

openai.api_key = "sk-"

system_rol = "Haz de cuenta que eres un analizador de sentimiento. Yo te doy sentimientos y tu analizas el sentimiento de los mensajes y das una respuesta con al menos 1 caracter y como máximo 4 caracteres. SOLO RESPUESTAS NUMÉRICAS. Donde 1 es negatividad máxima, 0 es neutral y 1 es positividad máxima (puedes responder con ints o floats)"

mensajes = [{"role":"system",'content':system_rol}]

#Creamos la clase sentimiento que tiene la responsabilidad única de representar un sentimiento y su color
class Sentimientos:
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.nombre)

#Creamos la clase AnalizadorDeSentimientos que tiene la responsabilidad de mapear polaridades a sentimiento, se encarga de definirnos cuál será en sentimiento
    
#AnalizadorDeSentimiento depende de Sentimientos Y de Rangos, y no dependemos de una biblioteca externa, sino dependemos de las implementaciones de los métodos de la clase Sentimientos y de los rangos.
class AnalizadorDeSentimientos:
    def __init__(self,rangos):
        self.rangos = rangos
    def analizar_sentimiento(self,polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        #si no está en el rango es muy negativo
        return Sentimientos("Muy Negativo","31")
    
#Cumplimos con el principio abierto/cerrado pues está abierto para extensiones ya que podemos agregar más rangos sin necesidad de modificar el código
rangos = [
    (-0.6,-0.3),Sentimientos("negativo","31"),
    (-0.3,-0.1),Sentimientos("algo negativo","31"),
    (-0.1,0.1),Sentimientos("neutral","31"),
    (0.1,0.4),Sentimientos("algo positivo","31"),
    (0.4,0.9),Sentimientos("positivo","31"),
    (0.9,1.0),Sentimientos("muy positivo","31"),
]

analizador = AnalizadorDeSentimientos(rangos)

while True:
    user_prompt = input("\x1b[1;33m"+" \nDime algo: " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensajes,
        max_tokens=8
    )
    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role": "assistant", "content": respuesta})

    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)
