import tkinter as tk
from pruebas2 import Funciones

class Mejora:
    def __init__(self):
        self.ventana = tk.Tk()

        # Crear una lista de Label y Botones
        self.lista_labels = [tk.Label(self.ventana, text="0") for _ in range(5)]
        self.lista_botones = [tk.Button(self.ventana, text=f"Incrementar {i}", command=lambda i=i: self.incrementar_contenido(i)) for i in range(5)]

        # Colocar los Label y Botones en la ventana
        for i, (label, boton) in enumerate(zip(self.lista_labels, self.lista_botones)):
            label.grid(row=i, column=0)
            boton.grid(row=i, column=1)

        # Crear una instancia de la clase Funciones y pasar la lista de Label
        self.funciones = Funciones(self.lista_labels)

    def incrementar_contenido(self, index):
        # Llamar a la función en funciones.py
        self.funciones.incrementar_contenido(index)

    def iniciar_aplicacion(self):
        self.ventana.mainloop()

# Crear una instancia de Mejora y comenzar la aplicación
app = Mejora()
app.iniciar_aplicacion()