# main.py
from productos import Producto
from carrito import Carrito

def main():
    carrito = Carrito()

    # Crear productos
    producto1 = Producto("Camisa", 20.0)
    producto2 = Producto("Pantalones", 35.0)
    producto3 = Producto("Zapatos", 50.0)

    # Agregar productos al carrito
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)

    # Mostrar productos en el carrito
    print("Productos en el carrito:")
    carrito.mostrar_carrito()

    # Mostrar el total
    print(f"Total a pagar: ${carrito.total()}")

if __name__ == "__main__":
    main()
