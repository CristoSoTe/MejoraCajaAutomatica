import tkinter as tk

class MiVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo de Cambio de Contenido")

        # Crear el Frame
        self.frame = tk.Frame(root, bg="blue")
        self.frame.pack(padx=10, pady=10)

        # Lista de etiquetas para premios
        self.etiquetas_premios = ["Precio:", "Desde:", "Impresos:", "Recaudado:", "Línea:",
                                  "Prima:", "Vendidos:", "Al:", "Informáticos:", "Caja Impresos:",
                                  "Bingo:", "Prima Extra:"]

        self.entradas = []

        # Configurar el diseño de la interfaz
        valor_fila = 0
        valor_columna = 0

        for etiqueta_premio in self.etiquetas_premios:
            tk.Label(self.frame, text=etiqueta_premio, bg="blue", fg="white", font=("Times New Roman", 13, "bold"),
                     anchor="e", justify="right").grid(row=valor_fila, column=valor_columna, sticky="ew", padx=10)
            valor_columna += 1

            entrada = tk.Entry(self.frame, font=("Times New Roman", 13, "bold"), justify="right", width=14)
            entrada.grid(row=valor_fila, column=valor_columna, sticky="ew")
            valor_columna += 1

            self.entradas.append(entrada)

        # Botón para cambiar contenido
        tk.Button(root, text="Cambiar Contenido", command=self.cambiar_contenido).pack(pady=10)

    def cambiar_contenido(self):
        # Obtener valores de los Entry
        precio = float(self.entradas[0].get())
        desde = int(self.entradas[1].get())
        impresos = int(self.entradas[2].get())

        # Calcular nuevos valores
        recaudado = round(impresos * precio, 2)
        linea = round(recaudado * 0.085, 2)
        prima = float(self.entradas[5].get())  # Asumiendo que es un número flotante
        vendidos = int(self.entradas[6].get())
        al = float(self.entradas[7].get())  # Asumiendo que es un número flotante
        informaticos = float(self.entradas[8].get())  # Asumiendo que es un número flotante
        caja_impresos = round((impresos * 1.5) * 0.37, 2)
        bingo = round(recaudado * 0.37, 2)
        prima_extra = float(self.entradas[11].get())  # Asumiendo que es un número flotante

        # Actualizar los Entry con los nuevos valores
        self.entradas[3].delete(0, tk.END)
        self.entradas[3].insert(0, recaudado)

        self.entradas[4].delete(0, tk.END)
        self.entradas[4].insert(0, linea)

        self.entradas[9].delete(0, tk.END)
        self.entradas[9].insert(0, caja_impresos)

        self.entradas[10].delete(0, tk.END)
        self.entradas[10].insert(0, bingo)

        # Puedes seguir actualizando los demás Entry de manera similar

if __name__ == "__main__":
    root = tk.Tk()
    app = MiVentana(root)
    root.mainloop()