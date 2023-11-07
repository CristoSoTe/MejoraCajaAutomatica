import tkinter as tk

class VentanaApp:
	def __init__(self, root):
		
		self.root = root
		self.root.title("Caja Automática")
		self.root.attributes('-fullscreen', True)
		self.root.config(bg="#000099")
		self.bandera = True
		self.etiqueta_liquidacion = {}
		self.frames = {}


		self.rangos = ["RANGO 1", "RANGO 2", "RANGO 3", "RANGO 4", "RANGO 5", "RANGO 6", "RANGO 7", "RANGO 8", "RANGO 9", "CIERRE", "TOTAL"]

		self.numero_series = ["liquidacion_liqui1","liquidacion_liqui2", "liquidacion_liqui3","liquidacion_liqui4","liquidacion_liqui5",
		"liquidacion_liqui6", "liquidacion_liqui7","liquidacion_liqui8", "liquidacion_liqui9", "liquidacion_liqui_cierre", "liquidacion_liqui_total"]

		self.etiquetas_premios = ["PRECIO", "DEL", "IMPRESOS", "RECAUDADO", "PREMIO LINEA", "PRIMA", "VENDIDOS", "AL", "INFORMATICOS","CAJA IMPRESOS", "PREMIO BINGO", "PRIMA EXTRA"]

		for i in range(5):
			identificador = f"Frame{i+1}"
			frame = tk.Frame(self.root)
			frame.pack(side="top", fill="both", expand=True)
			self.frames[identificador] = frame

			# ---------------------- ZONA DE LIQUIDACIÓN-----------------------------------------

			if identificador == "Frame1":
				for i in range(11):

					frame.grid_columnconfigure(i, weight=1)
				for i, rango in enumerate(self.rangos): 
					etiqueta=tk.Label(frame, text = rango, font=("Times New Roman",20,"bold"))
					etiqueta.grid(row = 0, column = i, sticky = "ew")
					if self.bandera:
						etiqueta.config(bg="#C0C0C0")
						self.bandera = False
					else:
						etiqueta.config(bg="gray59")
						self.bandera = True

				for i, numero_serie in enumerate(self.numero_series):
					label = tk.Label(frame, text = "100€",bg="white",fg="#800080", font=("Times New Roman",22,"bold"),width=7)
					label.grid(row = 1, column = i, sticky = "ew")
					self.etiqueta_liquidacion[numero_serie] = label

				for i in range(11):
					etiqueta = tk.Label(frame, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold"))
					etiqueta.grid(row = 3, column = i, sticky = "ew")
					if self.bandera:
						etiqueta.config(bg="gray59")
						self.bandera = False
					else:
						etiqueta.config(bg="#C0C0C0")
						self.bandera = True

				for i, rango in enumerate(self.numero_series):
					series_liquidacion_cierre = tk.Label(frame, text = "50",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2).grid(row = 4, column = i, sticky = "ew")

				for i in range(11):
					etiqueta = tk.Label(frame, text = "DEL - AL",bg="#31BFE4", font=("Times New Roman",13,"bold"))
					etiqueta.grid(row = 5, column = i, sticky = "ew")
					if self.bandera:
						etiqueta.config(bg="#C0C0C0")
						self.bandera = False
					else:
						etiqueta.config(bg="gray59")
						self.bandera = True

				for i, rango in enumerate(self.numero_series):
					carton_salida_liqui1_cierre = tk.Label(frame, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8).grid(row = 6, column = i, sticky = "ew")

			if identificador == "Frame2":
				frame.config(bg = "blue")
				valor_fila = 0
				valor_columna = 0
				for etiqueta_premio in self.etiquetas_premios:
					tk.Label(frame, text = etiqueta_premio, bg="blue", fg= "white", font=("Times New Roman",13,"bold")).grid(row = valor_fila, column = valor_columna, sticky = "ew", padx= 10)
					valor_columna += 1
					tk.Entry(frame).grid(row = valor_fila, column = valor_columna, sticky = "ew")
					valor_columna += 1
					if valor_columna > 11:
						valor_fila = 1
						valor_columna = 0

			if identificador == "Frame3":
				for i in range(11):
					frame.grid_columnconfigure(i, weight=1)
				frame.config(bg = "red")
				for i, rango in enumerate(self.rangos): 
					etiqueta=tk.Label(frame, text = rango, font=("Times New Roman",20,"bold"))
					etiqueta.grid(row = 0, column = i, sticky = "ew")
					if self.bandera:
						etiqueta.config(bg="#C0C0C0")
						self.bandera = False
					else:
						etiqueta.config(bg="gray59")
						self.bandera = True
			if identificador == "Frame4":
				frame.config(bg = "yellow")
				tk.Label(frame, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2).grid(row = 0, column = i, sticky = "ew")
				tk.Label(frame, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2).grid(row = 1, column = i, sticky = "ew")
				tk.Label(frame, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2).grid(row = 2, column = i, sticky = "ew")
				tk.Label(frame, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2).grid(row = 3, column = i, sticky = "ew")

			if identificador == "Frame5":
				for i in range(10):
					identificador = f"Frame{i+1}"
					frame = tk.Frame(self.root)
					frame.pack(side="left", fill="both", expand=True)
					self.frames[identificador] = frame
					tk.Button(frame, text=self.frames[identificador]).pack()
					if self.bandera:
						frame.config(bg="#C0C0C0")
						self.bandera = False
					else:
						frame.config(bg="gray59")
						self.bandera = True


# def probar():
# 	app.etiqueta_liquidacion["liquidacion_liqui1"].config(text=100)

if __name__ == "__main__":
	root = tk.Tk()
	app = VentanaApp(root)
	root.mainloop()