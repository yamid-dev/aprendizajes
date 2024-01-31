import random
import os

def Ahorcado_play():
    
    Anima_Ahorkdo = ['''
        x---------x
        |         ▓
                  ▓
                  ▓
                  ▓
                  ▓
                  ▓
                  ▓
     =============▓==''','''
        x---------x
        |         ▓
        |         ▓
        o         ▓
                  ▓
                  ▓
                  ▓
                  ▓
     =============▓==''','''
        x---------x
        |         ▓
        |         ▓
        o         ▓
        |         ▓
                  ▓
                  ▓
                  ▓
     =============▓==''','''
        
        x---------x
        |         ▓
        |         ▓
        o         ▓
       /|         ▓
                  ▓
                  ▓
                  ▓
     =============▓==''','''
        x---------x
        |         ▓
        |         ▓
        o         ▓
       /|\        ▓
                  ▓
                  ▓
                  ▓
     =============▓==''','''
        x---------x
        |         ▓
        |         ▓
        o         ▓
       /|\        ▓
       /          ▓
                  ▓
                  ▓
     =============▓==''','''
        x---------x
        |         ▓
        |         ▓
        o         ▓
       /|\        ▓
       / \        ▓
                  ▓
                  ▓
     =============▓==''']
    Lenguajes= [
        "RUBY",
        "PYTHON",
        "JAVASCRIPT",
        "MYSQL",
        "JAVA",
        "LARAVEL",
        "SWIFT",
        "PASCAL",
        "SQL"
    ]
    palabra = random.choice(Lenguajes)
    espacios = ["_"]*len(palabra)
    intentos = 6
    # print(palabra)
    print(espacios)
    while (True):
        #os.system("cls")
        for caracter in espacios:
            print(caracter, end=" ")
        print(Anima_Ahorkdo[intentos])
        letra=input("Elija una letra: ").upper()
        encontrar=False
        for indice,caracter in enumerate(palabra):
            if caracter == letra:
                espacios[indice] = letra
                encontrar = True
        if not encontrar:
            intentos -=1
        if "_" not in espacios:
            os.system("cls")
            print("GANASTE!!! \n")
            break
            input()
        if intentos == 0:
            os.system("cls")
            print("PERDISTE!!! :( \n")
            break
            input()
Ahorcado_play()
    
    
    