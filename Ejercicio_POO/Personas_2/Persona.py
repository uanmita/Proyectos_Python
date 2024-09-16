#Crear una clase “Persona” que sea la clase padre de otra clase “Estudiante”.
# Por tanto:

#En la clase “Persona” su metodo __init__()
#debe de estar preparado para recibir nombre y apellido.
#Además, esta clase , debe tener un metodo para mostrar nombre_completo()
#el cual debe mostrar el nombre acompañado del apellido.

#La otra clase “Estudiante”, debe de poder heredar de “Persona”,
#y además recibir los argumentos nombre y edad.
# También la clase “Estudiante”, recibe el valor “carrera”,
# y además contar con un metodo mostrar_carrera(). Las dos clases son obligatorias.

#Definición de la clase Persona

class Persona:
    def __init__(self):
        self.nombre = str (input("¿Nombre? "))
        self.apellido = str (input("¿Apellido? "))
        self.edad = int(input("¿Edad? "))

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} {self.apellido}, Edad: {self.edad}")




