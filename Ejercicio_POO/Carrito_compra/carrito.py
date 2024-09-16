# carrito.py
from productos import Producto

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            for producto in self.productos:
                print(producto)

    def total(self):
        return sum(producto.precio for producto in self.productos)
