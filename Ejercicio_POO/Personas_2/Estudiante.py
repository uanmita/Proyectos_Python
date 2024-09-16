#Crear una clase “Persona” que sea la clase padre de otra clase “Estudiante”.
# Por tanto:
from Ejercicio_POO.Personas_2.Persona import Persona


#En la clase “Persona” su metodo __init__()
#debe de estar preparado para recibir nombre y apellido.
#Además, esta clase , debe tener un metodo para mostrar nombre_completo()
#el cual debe mostrar el nombre acompañado del apellido.

#La otra clase “Estudiante”, debe de poder heredar de “Persona”,
#y además recibir los argumentos nombre y edad.
# También la clase “Estudiante”, recibe el valor “carrera”,
# y además contar con un metodo mostrar_carrera(). Las dos clases son obligatorias.

# Definición de la clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self):
        super().__init__()  # Llamada al constructor de la clase base
        self.carrera = str(input("¿Carrera?"))

    def mostrarCarrera(self):
        print(f"El nombre del estudiante es: {self.nombre} {self.apellido}, tiene "
              f"{self.edad} años y estudia {self.carrera}.")



# Crear una instancia de Estudiante con los datos proporcionados
e1 = Estudiante()
e1.mostrarCarrera()

p1 = e1
p1.mostrar_info()



