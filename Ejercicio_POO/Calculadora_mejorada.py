#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando
#el metodo __init__. Calcular después la suma, resta, multiplicación y división.
#Utilizar un metodo para cada una e imprimir los resultados obtenidos.
#Llamar a la clase Calculadora.



class Calculadora:
    def __init__(self):
        self.v1 = int (input("Primer valor?"))
        self.v2 = int (input("Segundo valor?"))

    def sumar(self):
        suma = self.v1+self.v2
        print ("El resultado de la suma es:", suma)

    def restar(self):
        resta = self.v1-self.v2
        print("El resultado de la suma es:", resta)

    def multi(self):
        multi = self.v1*self.v2
        print("El resultado de la multiplicación es:", multi)

    def div(self):
        divi = self.v1/self.v2
        print("El resultado de la división es: ", divi)

c1 = Calculadora()

print ("Elija operacion a efectuar: ** Todas, + Sumar, - Restar, * Multiplicar, / Dividir")

operacion = str(input("¿Operacion?"))
if operacion == "+":
    c1.sumar()
elif operacion == "-":
    c1.restar()
elif operacion == "*":
    c1.multi()
elif operacion == "/":
    c1.div()
elif operacion == "**":
    c1.sumar()
    c1.restar()
    c1.multi()
    c1.div()