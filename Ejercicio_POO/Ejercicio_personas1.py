#Crea una clase “Persona”. Con atributos nombre y edad.
# Además,hay que crear un método “cumpleaños”, que aumente en 1 la edad de la persona
# cuando se invoque sobre un objeto creado con “Persona”.


class Persona:

    def __init__(self):
        self.nombre = str(input("¿Nombre?"))
        self.edad = int (input("¿edad?"))

    def cumple(self):
        self.edad += 1

    def print(self):
        print(f"{self.nombre} tiene {self.edad - 1} y cumple {self.edad} años.")

p1 = Persona()
p2 = Persona()
p1.cumple()
p2.edad()
p1.print()
p2.print()




