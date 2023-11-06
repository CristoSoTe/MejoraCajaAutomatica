import tkinter as tk

class VentanaApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Caja Automática")
		self.root.attributes('-fullscreen', True)
		self.root.config(bg="#000099")

		rangos = ["RANGO 1", "RANGO 2", "RANGO 3", "RANGO 4", "RANGO 5", "RANGO 6", "RANGO 7", "RANGO 8", "RANGO 9", "CIERRE", "TOTAL"]

		nombre_etiquetas = []

		for i in range(11):
			self.root.grid_columnconfigure(i, weight=1)

		for i, rango in enumerate(rangos):
			label = tk.Label(root, text = rango,bg="#C0C0C0", font=("Times New Roman",20,"bold")).grid(row = 0, column = i, sticky = "ew")#, sticky = "ew"
			
			columna += 1




if __name__ == "__main__":
	root = tk.Tk()
	app = VentanaApp(root)
	root.mainloop()