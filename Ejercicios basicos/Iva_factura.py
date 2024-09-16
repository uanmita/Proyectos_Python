importeFactura = int (input("Introduzca el importe dela factura por favor: "))
tipoFactura = str (input("Introduzca tipo de factura General 'G' o Restauracion 'R'"))

if tipoFactura == "G":
    print ("el importe de su Factura es: ", importeFactura *0.21 + importeFactura )
else:
    print("el importe de su Factura es: ", importeFactura * 0.10 + importeFactura)