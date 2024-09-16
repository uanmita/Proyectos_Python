print("----CALCULE SU DESCUENTO EN LA TARIFA ANUAL----")
tarifa = int ( input ("Tarifa anual?"))
dto = 0

nombre = str (input("Introduzca su nombre: "))
edad = int (input("Introduzca su edad: "))
trabajo = str(input("Trabaja usted? Si o No: "))

if edad >= 18 and trabajo == "Si":
    print ("El precio de su abono es: ",tarifa, "Euros, no hay descuento disponible para usted.")
elif edad >= 18 and trabajo == "No":
    dto = 0.05
    print (f"El precio de su abono es: {tarifa-tarifa*dto:.2f} Euros")
elif edad < 18 and trabajo == "Si":
    dto = 0.25
    print (f"El precio de su abono es: {tarifa-tarifa*dto:.2f} Euros")
elif edad < 18 and trabajo == "No":
    dto = 0.50
    print (f"El precio de su abono es: {tarifa-tarifa*dto:.2f} Euros")

