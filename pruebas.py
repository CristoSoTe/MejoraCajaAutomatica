import tkinter as tk

class TuClase:
    def __init__(self):
        self.root = tk.Tk()
        self.precio="3"
        self.desde=1000
        self.lista_Entry_carton_salida = []

        for h in range(4):
            self.Entry_carton_salida = tk.Entry(self.root, fg="blue", bg="white", font=("Times New Roman", 17, "bold"), width=6, justify="right")
            self.Entry_carton_salida.pack(pady=20)
            self.lista_Entry_carton_salida.append(self.Entry_carton_salida)

        if self.precio == "1.5":
            self.lista_Entry_carton_salida[0].insert(0, self.desde)
            dato_salida =self.lista_Entry_carton_salida[0]
            self.salida= dato_salida.get()
        elif self.precio == "2":
            self.lista_Entry_carton_salida[1].insert(0, self.desde)
            dato_salida = self.lista_Entry_carton_salida[1]
            self.salida = dato_salida.get()
        elif self.precio == "3":
            self.lista_Entry_carton_salida[2].insert(0, self.desde)
            dato_salida = self.lista_Entry_carton_salida[2]
            self.salida = dato_salida.get()
        elif self.precio == "6":
            self.lista_Entry_carton_salida[3].insert(0, self.desde)
            dato_salida = self.lista_Entry_carton_salida[3]
            self.salida = dato_salida.get()

        # Asignar "2" al primer Entry (índice 0)
        # if self.precio == "2":
        #     self.lista_Entry_carton_salida[0].insert(0, self.desde)
        #     dato_salida =self.lista_Entry_carton_salida[0]
        #     self.salida= dato_salida.get()

        # # Asignar "3" al cuarto Entry (índice 3)
        # elif self.precio == "3":
        #     self.lista_Entry_carton_salida[3].insert(0, self.desde)
        #     dato_salida =self.lista_Entry_carton_salida[3]
        #     self.salida= dato_salida.get()

        self.root.mainloop()

# Crear una instancia de TuClase
app = TuClase()