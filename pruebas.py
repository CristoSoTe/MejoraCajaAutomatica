import tkinter as tk

class VentanaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caja Automática")
        self.valor1=0
        self.valor2=0
        self.valores = [self.valor1, self.valor2]

        self.etiqueta1 = tk.Label(root, text=0)
        self.etiqueta1.pack()

        self.etiqueta2 = tk.Label(root, text=0)
        self.etiqueta2.pack()

        self.labels = [self.etiqueta1, self.etiqueta2]

        # Creamos botones con funciones asociadas a cada uno
        for i in range(len(self.labels)):
            boton = tk.Button(root, text=f"Subir Serie {i+1}", command=lambda idx=i: self.sube_serie(idx))
            boton.pack()

    def sube_serie(self, num):
        self.valores[num] += 1
        self.labels[num].config(text=self.valores[num])

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaApp(root)
    root.mainloop()