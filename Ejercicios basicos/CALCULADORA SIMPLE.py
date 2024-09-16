x = int(input("Introduzca numero 1: "))
y = int(input("Introduzca numero 2: "))

def suma():
    sum = x+y
    print("El resultado de la suma de los números es: ",sum)

def resta():
    res = x-y
    print("El resultado de la resta de los números es: ",res)

def multi():
    mul = x*y
    print("El resultado de la multiplicación de los números es: ",mul)

def div():
    div = x/y
    print("El resultado de la división de los números es: ",div)


print ("Elija operacion a efectuar: 1 Sumar, 2 Restar, 3 Multiplicar, 4 Dividir")

operacion = int(input("¿Operacion?"))
if operacion == 1:
    suma()
elif operacion == 2:
    resta()
elif operacion == 3:
    multi()
else:
    div()