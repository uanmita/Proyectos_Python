seguirChat = True
while seguirChat:
    texto = input(">")
    if texto == "salir":
        seguirChat = False
    texto = texto.replace(":)","🤣")
    texto = texto.replace(":*","😉")
    texto = texto.replace(":-","😘")
    texto = texto.replace(":/","🤪")
    texto = texto.replace("mierda","💩")
    print(texto)
