#Ejercicio 4 = Chatbot en Python que nos pida que le digamos algo, tome eso que le decimos, analice sentimiento, y responda cuál es el sentimiento

#Este código no cumple los principios SOLID
import openai

openai.api_key = "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"

system_rol = "Haz de cuenta que eres un analizador de sentimiento. Yo te doy sentimientos y tu analizas el sentimiento de los mensajes y das una respuesta con al menos 1 caracter y como máximo 4 caracteres. SOLO RESPUESTAS NUMÉRICAS. Donde 1 es negatividad máxima, 0 es neutral y 1 es positividad máxima (puedes responder con ints o floats)"

mensajes = [{"role":"system",'content':system_rol}]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.8 and polaridad <= -0.3:
            return "1"  # Muy negativo
        elif polaridad > -0.3 and polaridad < -0.1:
            return "2"  # Algo negativo
        elif polaridad > -0.1 and polaridad <= 0.1:
            return "0"  # Neutral
        elif polaridad > 0.1 and polaridad <= 0.4:
            return "3"  # Algo positivo
        elif polaridad > 0.4 and polaridad <= 0.9:
            return "4"  # Positivo
        elif polaridad > 0.9:
            return "5"  # Muy positivo
        else:
            return "1"  # Muy negativo

analizador = AnalizadorDeSentimientos()

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
