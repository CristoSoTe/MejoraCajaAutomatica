import tkinter as tk 
from tkinter import messagebox as MessageBox
import os
import random
import socket
import re
import time
import threading
from funciones import *

class VentanaApp:
	def __init__(self, root):
		
		self.root = root
		self.root.title("Caja Automática")
		self.root.attributes('-fullscreen', True)
		self.root.config(bg="#000099")
		self.bandera = True
		self.etiqueta_liquidacion = {}
		self.frames = {}
		self.photoSube=tk.PhotoImage(file=r"c:\CajaMesaControl\flechaSube.png")
		self.photoBaja=tk.PhotoImage(file=r"c:\CajaMesaControl\flechaBaja.png")
		self.valor1=1; self.valor2=2; self.valor3=3; self.valor4=4;
		self.valor5=5; self.valor6=6; self.valor7=7; self.valor8=8;
		self.valor9=9
		self.labels = []
		self.botones = {}
		self.numero_boton = 0



		self.rangos = ["RANGO 1", "RANGO 2", "RANGO 3", "RANGO 4", "RANGO 5", "RANGO 6", "RANGO 7", "RANGO 8", "RANGO 9", "CIERRE", "TOTAL"]

		self.numero_series = ["liquidacion_liqui1","liquidacion_liqui2", "liquidacion_liqui3","liquidacion_liqui4","liquidacion_liqui5",
		"liquidacion_liqui6", "liquidacion_liqui7","liquidacion_liqui8", "liquidacion_liqui9", "liquidacion_liqui_cierre", "liquidacion_liqui_total"]

		self.etiquetas_premios = ["PRECIO", "DEL", "IMPRESOS", "RECAUDADO", "PREMIO LINEA", "PRIMA", "VENDIDOS", "AL", "INFORMATICOS","CAJA IMPRESOS", "PREMIO BINGO", "PRIMA EXTRA"]
		self.valores = [self.valor1, self.valor2, self.valor3, self.valor4, self.valor5, self.valor6, self.valor7, self.valor8, self.valor9]
		for i in range(5):
			identificador = f"Frame{i+1}"
			frame = tk.Frame(self.root)
			frame.pack(side="top", fill="both", expand=True)
			self.frames[identificador] = frame

# ---------------------- Frame de liquidación -----------------------------------------

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

# ----------------------------- Frame de información CM70 ----------------------------------

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

# -------------------------------- Frame de venta -----------------------------------

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

# -------------------------------- Frame de boton cerrar partida ---------------------------

			if identificador == "Frame4":
				frame.config(bg = "yellow")
				tk.Label(frame, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2).grid(row = 0, column = i, sticky = "ew")
				tk.Label(frame, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2).grid(row = 1, column = i, sticky = "ew")
				tk.Label(frame, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2).grid(row = 2, column = i, sticky = "ew")
				tk.Label(frame, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2).grid(row = 3, column = i, sticky = "ew")

# ---------------------------------------- Frame botones sube/baja ----------------------------------------------

			if identificador == "Frame5":
				numero_rango = 0
				valor_actual = 0
				
				

				for i in range(11):
					identificador = f"Frame{i+1}"
					frame = tk.Frame(self.root)
					frame.pack(side="left", fill="both", expand=True)
					self.frames[identificador] = frame
 					
					if identificador == "Frame1":
						tk.Button(frame, text="Histórico", bg= "Green", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack(pady=10)#, command=poner_al_frente_root
						tk.Button(frame, text= "RESET", bg= "#8B0000", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack()#, command=reset
						tk.Button(frame, command=lambda: salir(root), text= "SALIR", bg= "red", fg="White", font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack(pady=10)#, command= cerrar

					elif identificador == "Frame11":
 						boton_prepara_rectifica=tk.Button(frame, text="  COMENZAR  ", bg="#8B0000", fg ="#F0F8FF", font=("Times New Roman", 15,"bold"),cursor="hand2" )#,command = PreparaRectifica
 						boton_prepara_rectifica.pack(pady=50)
 						tk.Label(frame,text="CARBI-93 S.A.").pack()
 						tk.Label(frame,text="(Grupo Automáticos Canarios)").pack()

					else:
						
						rango = self.rangos[numero_rango]
						etiqueta_numero_rango = tk.Label(frame, text = rango, font=("Times New Roman",15,"bold"))
						etiqueta_numero_rango.pack()
						numero_rango += 1

						etiqueta_series = tk.Label(frame, text = "SERIES",bg="gray59", font=("Arial",10,"bold"))
						etiqueta_series.pack()

						self.valor = self.valores[valor_actual]
						etiqueta_numero_series = tk.Label(frame, text=str(self.valor), fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=2)
						etiqueta_numero_series.pack()
						self.labels.append(etiqueta_numero_series)
						valor_actual += 1

						#botones_frame_inferior()
						
						for i in range(3):
							identificador = f"boton{self.numero_boton+1}"
							boton = tk.Button(frame,cursor="hand2")
							boton.pack(padx=10, pady=5)
							self.botones[identificador] = boton #frames
							self.numero_boton += 1

							if identificador == "boton1":
								boton.config(image=self.photoSube, command=lambda: sube_serie(self, 1))
							elif identificador == "boton2":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF" ,cursor="hand2")
							elif identificador == "boton3":
								boton.config(image=self.photoBaja, command=lambda: baja_serie(self, 1))
							elif identificador == "boton4":
								boton.config(image=self.photoSube, command=lambda: sube_serie(self, 2))
							elif identificador == "boton5":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF" ,cursor="hand2")
							elif identificador == "boton6":
								boton.config(image=self.photoBaja, command=lambda: baja_serie(self, 2))
							elif identificador == "boton7":
								boton.config(image=self.photoSube, command=lambda: sube_serie(self, 3))
							elif identificador == "boton8":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF" ,cursor="hand2")
							elif identificador == "boton9":
								boton.config(image=self.photoBaja, command=lambda: baja_serie(self, 3))					

						if self.bandera:
							frame.config(bg="#C0C0C0")
							etiqueta_numero_rango.config(bg="#C0C0C0")
							etiqueta_series.config(bg="#C0C0C0")
							self.bandera = False
						else:
							frame.config(bg="gray59")
							etiqueta_numero_rango.config(bg="gray59")
							etiqueta_series.config(bg="gray59")
							self.bandera = True

# def probar():
# 	app.etiqueta_liquidacion["liquidacion_liqui1"].config(text=100)


if __name__ == "__main__":
	root = tk.Tk()
	app = VentanaApp(root)
	root.mainloop()
