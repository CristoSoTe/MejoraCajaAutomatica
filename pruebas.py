import tkinter as tk

class VentanaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caja Automática")
        self.frames = {}
        self.subframes = {}

        for i in range(5):
            identificador = f"Frame{i+1}"
            frame = tk.Frame(self.root)
            frame.pack(side="top", fill="both", expand=True)
            self.frames[identificador] = frame

            if identificador == "Frame1":
                for j in range(11):
                    subidentificador = f"SubFrameLiquidacion{j+1}"
                    subframe = tk.Frame(frame, bg="white")
                    subframe.pack(side="left", fill="both", expand=True)
                    self.subframes[subidentificador] = subframe
                    frame.grid_columnconfigure(j, weight=1)

                    if subidentificador == "SubFrameLiquidacion11":
                    	etiqueta_total_liquidacion = tk.Label(subframe, text="TOTAL", font=("Times New Roman", 20, "bold"))
                    	etiqueta_total_liquidacion.pack()
                    elif subidentificador == "SubFrameLiquidacion10":
                    	subframe.configure(background="red")
                    	etiqueta_cierre_liquidacion = tk.Label(subframe, text="CIERRE", font=("Times New Roman", 20, "bold"))
                    	etiqueta_cierre_liquidacion.pack()
                    else:
                    	etiqueta_cierre_liquidacion = tk.Label(subframe, text="RANGO", font=("Times New Roman", 20, "bold"))
                    	etiqueta_cierre_liquidacion.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaApp(root)
    root.mainloop()