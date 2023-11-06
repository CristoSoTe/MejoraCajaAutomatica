import tkinter as tk

class VentanaApp:
	def __init__(self, root):
		
		self.root = root
		self.root.title("Caja Automática")
		self.root.attributes('-fullscreen', True)
		self.root.config(bg="#000099")
		self.bandera = True 

		rangos = ["RANGO 1", "RANGO 2", "RANGO 3", "RANGO 4", "RANGO 5", "RANGO 6", "RANGO 7", "RANGO 8", "RANGO 9", "CIERRE", "TOTAL"]

		numero_series = ["liquidacion_liqui1","liquidacion_liqui2", "liquidacion_liqui3","liquidacion_liqui4","liquidacion_liqui5",
		"liquidacion_liqui6", "liquidacion_liqui7","liquidacion_liqui8", "liquidacion_liqui9", "liquidacion_liqui_cierre", "liquidacion_liqui_total"]

		for i in range(11):
			self.root.grid_columnconfigure(i, weight=1)

		# ---------------------- ZONA DE LIQUIDACIÓN-----------------------------------------

		for i, rango in enumerate(rangos): 
			etiqueta=tk.Label(root, text = rango, font=("Times New Roman",20,"bold"))
			etiqueta.grid(row = 0, column = i, sticky = "ew")
			if self.bandera:
				etiqueta.config(bg="#C0C0C0")
				self.bandera = False
			else:
				etiqueta.config(bg="gray59")
				self.bandera = True

		for i, numero_serie in enumerate(numero_series):
			label = tk.Label(root, text = "0€",bg="white",fg="#800080", font=("Times New Roman",22,"bold"),width=7).grid(row = 1, column = i)#, sticky = "ew"

		for i in range(11):
			etiqueta = tk.Label(root, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold"))
			etiqueta.grid(row = 3, column = i, sticky = "ew")
			if self.bandera:
				etiqueta.config(bg="gray59")
				self.bandera = False
			else:
				etiqueta.config(bg="#C0C0C0")
				self.bandera = True

		for i, rango in enumerate(numero_series):
			series_liquidacion_cierre = tk.Label(root, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2).grid(row = 4, column = i, sticky = "ew")

		for i in range(11):
			etiqueta = tk.Label(root, text = "DEL - AL",bg="#31BFE4", font=("Times New Roman",13,"bold"))
			etiqueta.grid(row = 5, column = i, sticky = "ew")
			if self.bandera:
				etiqueta.config(bg="#C0C0C0")
				self.bandera = False
			else:
				etiqueta.config(bg="gray59")
				self.bandera = True

		for i, rango in enumerate(numero_series):
			carton_salida_liqui1_cierre = tk.Label(root, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8).grid(row = 6, column = i, sticky = "ew")





if __name__ == "__main__":
	root = tk.Tk()
	app = VentanaApp(root)
	root.mainloop()