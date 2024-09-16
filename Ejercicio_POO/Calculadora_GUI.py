import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self):
        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora Gráfica NEO")

        # Campos de entrada para los valores
        self.label_v1 = tk.Label(self.ventana, text="Primer valor:")
        self.label_v1.grid(row=0, column=0)
        self.v1 = tk.Entry(self.ventana)
        self.v1.grid(row=0, column=1)

        self.label_v2 = tk.Label(self.ventana, text="Segundo valor:")
        self.label_v2.grid(row=1, column=0)
        self.v2 = tk.Entry(self.ventana)
        self.v2.grid(row=1, column=1)

        # Botones de operaciones
        self.boton_suma = tk.Button(self.ventana, text="+", command=self.sumar)
        self.boton_suma.grid(row=2, column=0)

        self.boton_resta = tk.Button(self.ventana, text="-", command=self.restar)
        self.boton_resta.grid(row=2, column=1)

        self.boton_multi = tk.Button(self.ventana, text="*", command=self.multi)
        self.boton_multi.grid(row=3, column=0)

        self.boton_divi = tk.Button(self.ventana, text="/", command=self.div)
        self.boton_divi.grid(row=3, column=1)

        # Resultado
        self.label_resultado = tk.Label(self.ventana, text="Resultado:")
        self.label_resultado.grid(row=4, column=0)

        self.resultado = tk.Label(self.ventana, text="")
        self.resultado.grid(row=4, column=1)

        # Iniciar la ventana
        self.ventana.mainloop()

    def obtener_valores(self):
        try:
            v1 = float(self.v1.get())
            v2 = float(self.v2.get())
            return v1, v2
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce números válidos.")
            return None, None

    def sumar(self):
        v1, v2 = self.obtener_valores()
        if v1 is not None and v2 is not None:
            suma = v1 + v2
            self.resultado.config(text=f"El resultado de la suma es: {suma}")

    def restar(self):
        v1, v2 = self.obtener_valores()
        if v1 is not None and v2 is not None:
            resta = v1 - v2
            self.resultado.config(text=f"El resultado de la resta es: {resta}")

    def multi(self):
        v1, v2 = self.obtener_valores()
        if v1 is not None and v2 is not None:
            multi = v1 * v2
            self.resultado.config(text=f"El resultado de la multiplicación es: {multi}")

    def div(self):
        v1, v2 = self.obtener_valores()
        if v1 is not None and v2 is not None:
            if v2 != 0:
                div = v1 / v2
                self.resultado.config(text=f"El resultado de la división es: {div}")
            else:
                messagebox.showerror("Error", "No se puede dividir por 0.")

# Crear una instancia de la calculadora
Calculadora()
