
compra = float(input("¿Importe de la compra?"))
puntos = int (input("¿Puntos disponibles?"))
dto = 0.0
if puntos <= 100:
    print ("El importe final de su compra es: ", compra - compra*10.10)
elif puntos > 100 and puntos < 150:
    print ("El importe final de su compra es: ", compra - compra*0.12)
elif puntos >= 150:
    print ("El importe final de su compra es: ", compra - compra*0.20)