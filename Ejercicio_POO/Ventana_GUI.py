import tkinter as tk  # Importamos la biblioteca Tkinter

# Crear una ventana principal
ventana = tk.Tk()

# Título de la ventana
ventana.title("Ventana_Python")

# Establecer dimensiones de la ventana
ventana.geometry("400x600")

# Crear una etiqueta de texto
etiqueta = tk.Label(ventana, text="¡Hola, Eva!", font=("Helvetica", 14))
etiqueta.pack(pady=20)  # Colocamos la etiqueta en la ventana

# Crear un botón
def boton_click():
    etiqueta.config(text="¡Has hecho clic en el botón,felicidades guapa!")

boton = tk.Button(ventana, text="Haz clic aquí", command=boton_click)
boton.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
