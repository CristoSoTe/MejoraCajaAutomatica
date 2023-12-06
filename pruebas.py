import tkinter as tk

class TuClase:
    def __init__(self):
        self.root = tk.Tk()
        self.precio="2"
        self.lista_Entry_carton_salida = []

        for h in range(4):
            self.Entry_carton_salida = tk.Entry(self.root, fg="blue", bg="white", font=("Times New Roman", 17, "bold"), width=6, justify="right")
            self.Entry_carton_salida.pack(pady=20)
            self.lista_Entry_carton_salida.append(self.Entry_carton_salida)

        # Asignar "2" al primer Entry (índice 0)
        if self.precio == "2":
            self.lista_Entry_carton_salida[0].insert(0, "2")

        # Asignar "3" al cuarto Entry (índice 3)
        elif self.precio != "2":
            self.lista_Entry_carton_salida[3].insert(0, "3")

        self.root.mainloop()

# Crear una instancia de TuClase
app = TuClase()