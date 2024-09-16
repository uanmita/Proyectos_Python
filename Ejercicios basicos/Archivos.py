"""def encriptarArchivo():
    archivo = open("file.txt","w")
    archivo.write("Texto a encriptar del fichero")
    texto = archivo.read("file.txt")
    archivo.close()
    textoEncriptado = encriptar(texto)"""




##archivo = open("file.txt")
##print (archivo.read())

def encriptar(texto):
    print ("Encriptar este texto "+texto)
    textofinal = ""
    for x in texto:
        textofinal += x + ""
        archivo = open("file.txt","w")
        print(textofinal)





encriptar("Juanma Parada")