import tkinter as tk

class VentanaApp:
    def __init__(self, root):
        self.root = root
        self.lista_labels = []  # Lista para almacenar los labels
        self.crear_labels()
        self.crear_boton()

    def crear_labels(self):
        for _ in range(5):
            label = tk.Label(self.root, text="0", font=("Arial", 12), width=10)
            label.pack()
            self.lista_labels.append(label)

    def crear_boton(self):
        boton = tk.Button(self.root, text="Actualizar", command=self.actualizar_label)
        boton.pack()

    def actualizar_label(self):
        from funciones import cambiar_texto_label
        cambiar_texto_label(self.lista_labels)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaApp(root)
    root.mainloop()