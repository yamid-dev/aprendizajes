#Ejercicio 4 = Chatbot en Python que nos pida que le digamos algo, tome eso que le decimos, analice sentimiento, y responda cuál es el sentimiento
from textblob import TextBlob

class AnalizadorDeSentimiento:
    def analizar_sentimiento(self,texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutro"
        else:
            return "negativo"
analizador = AnalizadorDeSentimiento()
resultado = analizador.analizar_sentimiento("bad!")
print(resultado)