import math

# Solicitar las longitudes de los catetos
cateto1 = int(input("Longitud del cateto 1? "))
cateto2 = int(input("Longitud del cateto 2? "))

# Verificar si alguno de los catetos es 0
if cateto1 == 0 or cateto2 == 0:
    print("!!Error: la medida de los catetos no puede ser 0!!")
else:
    # Calcular la hipotenusa usando la fórmula correcta
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    print("La hipotenusa del triángulo es:", hipotenusa)
