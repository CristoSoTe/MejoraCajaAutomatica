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
		self.subframesLiquidacion = {}
		self.subframesCierre = {}
		self.subframesVenta = {}
		self.subframesBotones = {}
		self.botones = {}
		self.photoSube=tk.PhotoImage(file=r"c:\CajaMesaControl\flechaSube.png")
		self.photoBaja=tk.PhotoImage(file=r"c:\CajaMesaControl\flechaBaja.png")

		self.pico_salida=0

		#------------------------------------------- Variables Liquidacion --------------------------

		self.liquidacion1=0; self.liquidacion2=0; self.liquidacion3=0; self.liquidacion4=0; self.liquidacion5=0;
		self.liquidacion6=0; self.liquidacion7=0; self.liquidacion8=0; self.liquidacion9=0; self.liquidacion_cierre=0; self.liquidacion_total=0;
		# Variables de lo que tiene que liquidar cada rango

		self.series_liquidacion_rango1="0 + 0"; self.series_liquidacion_rango2=0; self.series_liquidacion_rango3=0; self.series_liquidacion_rango4=0; self.series_liquidacion_rango5=0;
		self.series_liquidacion_rango6=0; self.series_liquidacion_rango7=0; self.series_liquidacion_rango8=0; self.series_liquidacion_rango9=0; self.series_liquidacion_cierre="0 + 0";
		self.series_liquidacion_total=0;
		# Variables del numero de series que tiene cada rango en el frame de liquidacion

		self.cartones_liquidacion1=0; self.cartones_liquidacion2=0;self.cartones_liquidacion3=0; self.cartones_liquidacion4=0; self.cartones_liquidacion5=0;
		self.cartones_liquidacion6=0; self.cartones_liquidacion7=0;self.cartones_liquidacion8=0; self.cartones_liquidacion9=0; self.cartones_liquidacion_cierre=0;
		self.cartones_liquidacion_total=0;
		# Variables de los cartones que tiene cada rango en el frame de liquidacion

		#------------------------------------------ Variables Venta -------------------------------------

		self.numero_series_por_rango_venta1=0; self.numero_series_por_rango_venta2=0; self.numero_series_por_rango_venta3=0; self.numero_series_por_rango_venta4=0;
		self.numero_series_por_rango_venta5=0; self.numero_series_por_rango_venta6=0; self.numero_series_por_rango_venta7=0; self.numero_series_por_rango_venta8=0;
		self.numero_series_por_rango_venta9=0;
		# Variables del numero de serie que tiene cada rango en el frame de venta

		self.carton_salida1_rango1=0; self.carton_salida1_rango2=0; self.carton_salida1_rango3=0; self.carton_salida1_rango4=0; self.carton_salida1_rango5=0; self.carton_salida1_rango6=0; self.carton_salida1_rango7=0; self.carton_salida1_rango8=0; self.carton_salida1_rango9=0;
		# Variables carton de salida en el frame de venta al precio de 1.5€

		self.carton_salida_siguiente1_rango1=0; self.carton_salida_siguiente1_rango2=0; self.carton_salida_siguiente1_rango3=0; self.carton_salida_siguiente1_rango4=0; self.carton_salida_siguiente1_rango5=0; self.carton_salida_siguiente1_rango6=0; self.carton_salida_siguiente1_rango7=0; self.carton_salida_siguiente1_rango8=0; self.carton_salida_siguiente1_rango9=0;
		# Variables carton de salida para la siguiente partida en el frame de venta al precio de 1.5€

		self.carton_salida2_rango1=0; self.carton_salida2_rango2=0; self.carton_salida2_rango3=0; self.carton_salida2_rango4=0; self.carton_salida2_rango5=0; self.carton_salida2_rango6=0; self.carton_salida2_rango7=0; self.carton_salida2_rango8=0; self.carton_salida2_rango9=0;
		# Variables carton de salida en el frame de venta al precio de 2€

		self.carton_salida_siguiente2_rango1=0; self.carton_salida_siguiente2_rango2=0; self.carton_salida_siguiente2_rango3=0; self.carton_salida_siguiente2_rango4=0; self.carton_salida_siguiente2_rango5=0; self.carton_salida_siguiente2_rango6=0; self.carton_salida_siguiente2_rango7=0; self.carton_salida_siguiente2_rango8=0; self.carton_salida_siguiente2_rango9=0;
		# Variables carton de salida para la siguiente partida en el frame de venta al precio de 2€

		self.carton_salida3_rango1=0; self.carton_salida3_rango2=0; self.carton_salida3_rango3=0; self.carton_salida3_rango4=0; self.carton_salida3_rango5=0; self.carton_salida3_rango6=0; self.carton_salida3_rango7=0; self.carton_salida3_rango8=0; self.carton_salida3_rango9=0;
		# Variables carton de salida en el frame de venta al precio de 3€

		self.carton_salida_siguiente3_rango1=0; self.carton_salida_siguiente3_rango2=0; self.carton_salida_siguiente3_rango3=0; self.carton_salida_siguiente3_rango4=0; self.carton_salida_siguiente3_rango5=0; self.carton_salida_siguiente3_rango6=0; self.carton_salida_siguiente3_rango7=0; self.carton_salida_siguiente3_rango8=0; self.carton_salida_siguiente3_rango9=0;
		# Variables carton de salida para la siguiente partida en el frame de venta al precio de 3€

		self.carton_salida6_rango1=0; self.carton_salida6_rango2=0; self.carton_salida6_rango3=0; self.carton_salida6_rango4=0; self.carton_salida6_rango5=0; self.carton_salida6_rango6=0; self.carton_salida6_rango7=0; self.carton_salida6_rango8=0; self.carton_salida6_rango9=0;
		# Variables carton de salida en el frame de venta al precio de 6€

		self.carton_salida_siguiente6_rango1=0; self.carton_salida_siguiente6_rango2=0; self.carton_salida_siguiente6_rango3=0; self.carton_salida_siguiente6_rango4=0; self.carton_salida_siguiente6_rango5=0; self.carton_salida_siguiente6_rango6=0; self.carton_salida_siguiente6_rango7=0; self.carton_salida_siguiente6_rango8=0; self.carton_salida_siguiente6_rango9=0;
		# Variables carton de salida para la siguiente partida en el frame de venta al precio de 6€

		#------------------------------------------- Variables Botones ----------------------------------

		self.valor1=0; self.valor2=0; self.valor3=0; self.valor4=0; self.valor5=0;
		self.valor6=0; self.valor7=0; self.valor8=0; self.valor9 = 0
		
		
		self.lista_liquidacion = []
		self.lista_numero_series_liquidacion = []
		self.lista_numero_series_por_rango_venta = []
		self.lista_cartones_liquidacion = []
		self.lista_carton_salida_1 = []
		self.lista_carton_salida_siguiente_1 = []
		self.lista_carton_salida_2 = []
		self.lista_carton_salida_siguiente_2 = []
		self.lista_carton_salida_3 = []
		self.lista_carton_salida_siguiente_3 = []
		self.lista_carton_salida_6 = []
		self.lista_carton_salida_siguiente_6 = []
		self.lista_series_frame_5 = []

		self.numero_boton = 0

		self.rangos = ["RANGO 1", "RANGO 2", "RANGO 3", "RANGO 4", "RANGO 5", "RANGO 6", "RANGO 7", "RANGO 8", "RANGO 9", "CIERRE", "TOTAL"]

		self.numero_series = ["liquidacion_liqui1","liquidacion_liqui2", "liquidacion_liqui3","liquidacion_liqui4","liquidacion_liqui5",
		"liquidacion_liqui6", "liquidacion_liqui7","liquidacion_liqui8", "liquidacion_liqui9", "liquidacion_liqui_cierre", "liquidacion_liqui_total"]

		self.etiquetas_premios = ["PRECIO", "DEL", "IMPRESOS", "RECAUDADO", "PREMIO LINEA", "PRIMA", "VENDIDOS", "AL", "INFORMATICOS","CAJA IMPRESOS", "PREMIO BINGO", "PRIMA EXTRA"]

		#--------------------------------------------- Listas liquidacion -----------------------------

		self.liquidacion = [self.liquidacion1, self.liquidacion2, self.liquidacion3, self.liquidacion4, self.liquidacion5, self.liquidacion6, self.liquidacion7, self.liquidacion8, self.liquidacion9, self.liquidacion_cierre, self.liquidacion_total]
		# Lista de todas la variables de lo que tiene que liquidar cada rango

		self.numero_series_liquidacion = [self.series_liquidacion_rango1, self.series_liquidacion_rango2, self.series_liquidacion_rango3, self.series_liquidacion_rango4, self.series_liquidacion_rango5, self.series_liquidacion_rango6, self.series_liquidacion_rango7, self.series_liquidacion_rango8, self.series_liquidacion_rango9, self.series_liquidacion_cierre, self.series_liquidacion_total]
		# Lista del numero de series que tiene cada rango en la liquidacion

		self.cartones_liquidacion = [self.cartones_liquidacion1, self.cartones_liquidacion2, self.cartones_liquidacion3, self.cartones_liquidacion4, self.cartones_liquidacion5, self.cartones_liquidacion6, self.cartones_liquidacion7, self.cartones_liquidacion8, self.cartones_liquidacion9, self.cartones_liquidacion_cierre, self.cartones_liquidacion_total]
		# Lista de los cartones que tiene cada rango en la liquidacion

		#---------------------------------------------- Listas Venta ---------------------------------

		self.numero_series_venta = [self.numero_series_por_rango_venta1, self.numero_series_por_rango_venta2, self.numero_series_por_rango_venta3, self.numero_series_por_rango_venta4, self.numero_series_por_rango_venta5, self.numero_series_por_rango_venta6, self.numero_series_por_rango_venta7, self.numero_series_por_rango_venta8, self.numero_series_por_rango_venta9] 
		#Esta es la lista donde se encuentra el numero de series asignadas a cada rango en la zona de venta

		self.numero_carton_salida_1 =[self.carton_salida1_rango1, self.carton_salida1_rango2, self.carton_salida1_rango3, self.carton_salida1_rango4, self.carton_salida1_rango5, self.carton_salida1_rango6, self.carton_salida1_rango7, self.carton_salida1_rango8, self.carton_salida1_rango9] 
		# Esta es la lista donde estan las variables del carton de salida de todos los rangos al precio de 1.5€

		self.numero_carton_salida_siguiente_1 =[self.carton_salida_siguiente1_rango1, self.carton_salida_siguiente1_rango2, self.carton_salida_siguiente1_rango3, self.carton_salida_siguiente1_rango4, self.carton_salida_siguiente1_rango5, self.carton_salida_siguiente1_rango6, self.carton_salida_siguiente1_rango7, self.carton_salida_siguiente1_rango8, self.carton_salida_siguiente1_rango9] 
		# Esta es la lista donde estan las variables del carton de salida de la partida siguiente de todos los rangos al precio de 1.5€

		self.numero_carton_salida_2 = [self.carton_salida2_rango1, self.carton_salida2_rango2, self.carton_salida2_rango3, self.carton_salida2_rango4, self.carton_salida2_rango5, self.carton_salida2_rango6, self.carton_salida2_rango7, self.carton_salida2_rango8, self.carton_salida2_rango9] 
		# Esta es la lista donde estan las variables del carton de salida de todos los rangos al precio de 2€

		self.numero_carton_salida_siguiente_2 = [self.carton_salida_siguiente2_rango1, self.carton_salida_siguiente2_rango2, self.carton_salida_siguiente2_rango3, self.carton_salida_siguiente2_rango4, self.carton_salida_siguiente2_rango5, self.carton_salida_siguiente2_rango6, self.carton_salida_siguiente2_rango7, self.carton_salida_siguiente2_rango8, self.carton_salida_siguiente2_rango9] 
		# Esta es la lista donde estan las variables del carton de salida de la partida siguiente de todos los rangos al precio de 2€

		self.numero_carton_salida_3 = [self.carton_salida3_rango1, self.carton_salida3_rango2, self.carton_salida3_rango3, self.carton_salida3_rango4, self.carton_salida3_rango5, self.carton_salida3_rango6, self.carton_salida3_rango7, self.carton_salida3_rango8, self.carton_salida3_rango9] 
		# Esta es la lista donde estan las variables del carton de salida de todos los rangos al precio de 3€

		self.numero_carton_salida_siguiente_3 = [self.carton_salida_siguiente3_rango1, self.carton_salida_siguiente3_rango2, self.carton_salida_siguiente3_rango3, self.carton_salida_siguiente3_rango4, self.carton_salida_siguiente3_rango5, self.carton_salida_siguiente3_rango6, self.carton_salida_siguiente3_rango7, self.carton_salida_siguiente3_rango8, self.carton_salida_siguiente3_rango9] 
		# Esta es la lista donde estan las variables del carton de salida de la partida siguiente de todos los rangos al precio de 3€

		self.numero_carton_salida_6 = [self.carton_salida6_rango1, self.carton_salida6_rango2, self.carton_salida6_rango3, self.carton_salida6_rango4, self.carton_salida6_rango5, self.carton_salida6_rango6, self.carton_salida6_rango7, self.carton_salida6_rango8, self.carton_salida6_rango9] 
		# Esta es la lista donde estan las variables del carton de salida de todos los rangos al precio de 6€

		self.numero_carton_salida_siguiente_6 = [self.carton_salida_siguiente6_rango1, self.carton_salida_siguiente6_rango2, self.carton_salida_siguiente6_rango3, self.carton_salida_siguiente6_rango4, self.carton_salida_siguiente6_rango5, self.carton_salida_siguiente6_rango6, self.carton_salida_siguiente6_rango7, self.carton_salida_siguiente6_rango8, self.carton_salida_siguiente6_rango9] 
		# Esta es la lista donde estan las variables del carton de salida de la partida siguiente de todos los rangos al precio de 6€
		#-----------------------------------------------------------------------------------------------

		self.valores = [self.valor1, self.valor2, self.valor3, self.valor4, self.valor5, self.valor6, self.valor7, self.valor8, self.valor9]

		for i in range(5):
			identificador = f"Frame{i+1}"
			frame = tk.Frame(self.root)
			frame.pack(side="top", fill="both", expand=True)
			self.frames[identificador] = frame

# ---------------------- Frame de liquidación -----------------------------------------

			if identificador == "Frame1":
				indice_rango = 1
				for j in range(11):
					indice_liquidacion = 1

					SubIdentificador = f"SubFrameLiquidacion{j+1}"
					subframe = tk.Frame(frame)
					subframe.pack(side="left", fill="both", expand=True)
					self.subframesLiquidacion[identificador] = subframe
					subframe.grid_columnconfigure(j, weight=1)

					if SubIdentificador == "SubFrameLiquidacion1":
						subframe.config(bg="#00FFFF")
						self.etiqueta_numero_rango1_liquidacion = tk.Label(subframe, text = "RANGO1", font=("Times New Roman",20,"bold"), bg="#00FFFF", fg="#009900")
						self.etiqueta_numero_rango1_liquidacion.pack()

						self.etiqueta_liquidacion_rango1 = tk.Label(subframe, text=self.liquidacion1, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
						self.etiqueta_liquidacion_rango1.pack()
						self.lista_liquidacion.append(self.etiqueta_liquidacion)

						series_liquidacion_rango1=tk.Label(subframe, text = "SERIES + Pico", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						series_liquidacion_rango1.pack()

						self.etiqueta_numero_series_liquidacion_rango1 = tk.Label(subframe, text=self.series_liquidacion_rango1, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=4)
						self.etiqueta_numero_series_liquidacion_rango1.pack()
						self.lista_numero_series_liquidacion.append(self.etiqueta_numero_series_liquidacion_rango1)

						del_al_liquidacion_rango1=tk.Label(subframe, text = "DEL-AL", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						del_al_liquidacion_rango1.pack()

						self.etiqueta_cartones_liquidacion_rango1 = tk.Label(subframe, text=self.cartones_liquidacion1, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=8)
						self.etiqueta_cartones_liquidacion_rango1.pack()
						self.lista_cartones_liquidacion.append(self.etiqueta_cartones_liquidacion_rango1)

					elif SubIdentificador == "SubFrameLiquidacion10":
						subframe.config(bg="#00FFFF")
						self.etiqueta_cierre_liquidacion = tk.Label(subframe, text = "CIERRE", font=("Times New Roman",20,"bold"), bg="#00FFFF", fg="#009900")
						self.etiqueta_cierre_liquidacion.pack()

						self.etiqueta_liquidacion_cierre = tk.Label(subframe, text=self.liquidacion_cierre, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
						self.etiqueta_liquidacion_cierre.pack()
						self.lista_liquidacion.append(self.etiqueta_liquidacion_cierre)

						series_liquidacion_cierre=tk.Label(subframe, text = "SERIES + Pico", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						series_liquidacion_cierre.pack()

						self.etiqueta_numero_series_liquidacion_cierre = tk.Label(subframe, text=self.series_liquidacion_cierre, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=4)
						self.etiqueta_numero_series_liquidacion_cierre.pack()
						self.lista_numero_series_liquidacion.append(self.etiqueta_numero_series_liquidacion_cierre)

						del_al_liquidacion_cierre=tk.Label(subframe, text = "DEL-AL", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						del_al_liquidacion_cierre.pack()

						self.etiqueta_cartones_liquidacion_cierre = tk.Label(subframe, text=self.cartones_liquidacion_cierre, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=8)
						self.etiqueta_cartones_liquidacion_cierre.pack()
						self.lista_cartones_liquidacion.append(self.etiqueta_cartones_liquidacion_rango1)

					elif SubIdentificador == "SubFrameLiquidacion11":
						subframe.config(bg="#0099ff")
						etiqueta_total_liquidacion = tk.Label(subframe, text = "TOTAL", font=("Times New Roman",20,"bold"), bg="#0099ff")
						etiqueta_total_liquidacion.pack()

						self.etiqueta_liquidacion_total = tk.Label(subframe, text=self.liquidacion_total, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
						self.etiqueta_liquidacion_total.pack()
						self.lista_liquidacion.append(self.etiqueta_liquidacion_total)

						series_liquidacion_total=tk.Label(subframe, text = "SERIES", font=("Times New Roman", 15,"bold"), bg="#0099ff")
						series_liquidacion_total.pack()

						self.etiqueta_numero_series_liquidacion_total = tk.Label(subframe, text=self.series_liquidacion_total, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=2)
						self.etiqueta_numero_series_liquidacion_total.pack()
						self.lista_numero_series_liquidacion.append(self.etiqueta_numero_series_liquidacion_total)

						del_al_liquidacion_total=tk.Label(subframe, text = "DEL-AL", font=("Times New Roman", 15,"bold"), bg="#0099ff")
						del_al_liquidacion_total.pack()

						self.etiqueta_cartones_liquidacion_total = tk.Label(subframe, text=self.cartones_liquidacion_total, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=8)
						self.etiqueta_cartones_liquidacion_total.pack()
						self.lista_cartones_liquidacion.append(self.etiqueta_cartones_liquidacion_total)

					else:

						rango = self.rangos[indice_rango]
						etiqueta_numero_rango_liquidacion = tk.Label(subframe, text = rango, font=("Times New Roman",20,"bold"))
						etiqueta_numero_rango_liquidacion.pack()
						indice_rango += 1

						liquidacion_rango = self.liquidacion[indice_liquidacion]
						self.etiqueta_liquidacion = tk.Label(subframe, text=liquidacion_rango, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
						self.etiqueta_liquidacion.pack()
						self.lista_liquidacion.append(self.etiqueta_liquidacion)
						indice_liquidacion += 1

						series_liquidacion=tk.Label(subframe, text = "SERIES", font=("Times New Roman", 15,"bold"))
						series_liquidacion.pack()

						numero_series_por_rango_liquidacion = self.numero_series_liquidacion[indice_liquidacion]
						self.etiqueta_numero_series_liquidacion = tk.Label(subframe, text=numero_series_por_rango_liquidacion, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=2)
						self.etiqueta_numero_series_liquidacion.pack()
						self.lista_numero_series_liquidacion.append(self.etiqueta_numero_series_liquidacion)
						indice_liquidacion += 1

						del_al_liquidacion=tk.Label(subframe, text = "DEL-AL", font=("Times New Roman", 15,"bold"))
						del_al_liquidacion.pack()

						cartones_rango_liquidacion = self.cartones_liquidacion[indice_liquidacion]
						self.etiqueta_cartones_liquidacion = tk.Label(subframe, text=cartones_rango_liquidacion, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=8)
						self.etiqueta_cartones_liquidacion.pack()
						self.lista_cartones_liquidacion.append(self.etiqueta_cartones_liquidacion)
						indice_liquidacion += 1

						if self.bandera:
							subframe.config(bg="#C0C0C0")
							etiqueta_numero_rango_liquidacion.config(bg="#C0C0C0")
							series_liquidacion.config(bg="#C0C0C0")
							del_al_liquidacion.config(bg="#C0C0C0")
							self.bandera = False
						else:
							subframe.config(bg="gray59")
							etiqueta_numero_rango_liquidacion.config(bg="gray59")
							series_liquidacion.config(bg="gray59")
							del_al_liquidacion.config(bg="gray59")
							self.bandera = True



# ----------------------------- Frame de información CM70 ----------------------------------

			if identificador == "Frame2":
				frame.config(bg = "blue")
				valor_fila = 0
				valor_columna = 0
				for etiqueta_premio in self.etiquetas_premios:
					tk.Label(frame, text = etiqueta_premio, bg="blue", fg= "white", font=("Times New Roman",13,"bold"), anchor="e", justify="right").grid(row = valor_fila, column = valor_columna, sticky = "ew", padx= 10)
					valor_columna += 1
					tk.Entry(frame).grid(row = valor_fila, column = valor_columna, sticky = "ew")
					valor_columna += 1
					if valor_columna > 11:
						valor_fila = 1
						valor_columna = 0

# -------------------------------- Frame de venta -----------------------------------

			if identificador == "Frame3":
				indice_rango_venta = 1
				indice_series_venta = 1
				indice_carton_salida = 1

				for j in range(11):
					subIdentificador = f"SubFrameVenta{j+1}"
					subframe = tk.Frame(frame, bg="white")
					subframe.pack(side="left", fill="both", expand=True)
					self.subframesVenta[subIdentificador] = subframe
					subframe.grid_columnconfigure(j, weight=1)

					if subIdentificador == "SubFrameVenta1":
						tk.Label(subframe, text="Precios").pack()

					elif subIdentificador == "SubFrameVenta2":
						subframe.config(bg="#00FFFF")
						self.etiqueta_numero_rango1_venta = tk.Label(subframe, text = "RANGO1", font=("Times New Roman",20,"bold"), bg="#00FFFF", fg="#009900")
						self.etiqueta_numero_rango1_venta.pack()

					elif subIdentificador == "SubFrameVenta11":
						subframe.config(bg="#00FFFF")
						self.etiqueta_cierre_venta = tk.Label(subframe, text = "CIERRE", font=("Times New Roman",20,"bold"), bg="#00FFFF", fg="#009900")
						self.etiqueta_cierre_venta.pack()

					else:
						rango = self.rangos[indice_rango_venta]
						etiqueta_numero_rango_venta = tk.Label(subframe, text = rango, font=("Times New Roman",20,"bold"))
						etiqueta_numero_rango_venta.pack()
						indice_rango_venta += 1

						etiquetas_series_venta=tk.Label(subframe, text = "SERIES", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						etiquetas_series_venta.pack()

						numero_series_por_rango_venta = self.numero_series_venta[indice_series_venta]
						self.etiqueta_numero_series_por_rango_venta = tk.Label(subframe, text=numero_series_por_rango_venta, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
						self.etiqueta_numero_series_por_rango_venta.pack()
						self.lista_numero_series_por_rango_venta.append(self.etiqueta_numero_series_por_rango_venta)
						indice_series_venta += 1

						etiquetas_salidas_venta=tk.Label(subframe, text = "SALIDAS", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						etiquetas_salidas_venta.pack()

						#------------------------------- Etiquetas Carton Salida ---------------------------------------
						for h in range(4):
							carton_salida_1 = self.numero_carton_salida_1[indice_carton_salida]
							self.etiqueta_carton_salida1 = tk.Label(subframe, text=carton_salida_1, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
							self.etiqueta_carton_salida1.pack()
							self.lista_carton_salida_1.append(self.etiqueta_carton_salida1)

							carton_salida_siguiente_1 = self.numero_carton_salida_siguiente_1[indice_carton_salida]
							self.etiqueta_carton_salida_siguiente1 = tk.Label(subframe, text=carton_salida_siguiente_1, fg="blue", bg = "white", font=("Times New Roman",15,"bold"), width=4)
							self.etiqueta_carton_salida_siguiente1.pack(pady=1)
							self.lista_carton_salida_siguiente_1.append(self.etiqueta_carton_salida_siguiente1)

							etiqueta_vacia = tk.Label(subframe, text="", font=("Times New Roman",4,"bold"))
							etiqueta_vacia.pack()

							if self.bandera:
								etiqueta_vacia.config(bg="#C0C0C0")
								self.bandera = True
							else:
								etiqueta_vacia.config(bg="gray59")
								self.bandera = False

						# # ----------------------------- Etiquetas Carton Salida 2€ ----------------------------------------

						# carton_salida_2 = self.numero_carton_salida_2[indice_carton_salida]
						# self.etiqueta_carton_salida2 = tk.Label(subframe, text=carton_salida_2, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
						# self.etiqueta_carton_salida2.pack(pady=1)
						# self.lista_carton_salida_2.append(self.etiqueta_carton_salida2)

						# carton_salida_siguiente_2 = self.numero_carton_salida_siguiente_2[indice_carton_salida]
						# self.etiqueta_carton_salida_siguiente2 = tk.Label(subframe, text=carton_salida_siguiente_2, fg="blue", bg = "white", font=("Times New Roman",15,"bold"), width=4)
						# self.etiqueta_carton_salida_siguiente2.pack()
						# self.lista_carton_salida_siguiente_2.append(self.etiqueta_carton_salida_siguiente2)


						# #------------------------------- Etiquetas Carton Salida 3€ -------------------------------------

						# carton_salida_3 = self.numero_carton_salida_3[indice_carton_salida]
						# self.etiqueta_carton_salida3 = tk.Label(subframe, text=carton_salida_3, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
						# self.etiqueta_carton_salida3.pack(pady=2)
						# self.lista_carton_salida_3.append(self.etiqueta_carton_salida3)

						# carton_salida_siguiente_3 = self.numero_carton_salida_siguiente_3[indice_carton_salida]
						# self.etiqueta_carton_salida_siguiente3 = tk.Label(subframe, text=carton_salida_siguiente_3, fg="blue", bg = "white", font=("Times New Roman",15,"bold"), width=4)
						# self.etiqueta_carton_salida_siguiente3.pack()
						# self.lista_carton_salida_siguiente_3.append(self.etiqueta_carton_salida_siguiente3)

						# #------------------------------- Etiquetas Carton Salida 6€ -------------------------------------

						# carton_salida_6 = self.numero_carton_salida_6[indice_carton_salida]
						# self.etiqueta_carton_salida6 = tk.Label(subframe, text=carton_salida_6, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
						# self.etiqueta_carton_salida6.pack(pady=2)
						# self.lista_carton_salida_6.append(self.etiqueta_carton_salida6)

						# carton_salida_siguiente_6 = self.numero_carton_salida_siguiente_6[indice_carton_salida]
						# self.etiqueta_carton_salida_siguiente6 = tk.Label(subframe, text=carton_salida_siguiente_6, fg="blue", bg = "white", font=("Times New Roman",15,"bold"), width=4)
						# self.etiqueta_carton_salida_siguiente6.pack()
						# self.lista_carton_salida_siguiente_6.append(self.etiqueta_carton_salida_siguiente6)

						#---------------------------------- Varios ------------------------------------

						indice_carton_salida += 1 # Variable para que suba un rango en cada bucle

						if self.bandera:
							subframe.config(bg="#C0C0C0")
							etiqueta_numero_rango_venta.config(bg="#C0C0C0")
							etiquetas_series_venta.config(bg="#C0C0C0")
							etiquetas_salidas_venta.config(bg="#C0C0C0")
							etiqueta_vacia.config(bg="#C0C0C0")
							self.bandera = False
						else:
							subframe.config(bg="gray59")
							etiqueta_numero_rango_venta.config(bg="gray59")
							etiquetas_series_venta.config(bg="gray59")
							etiquetas_salidas_venta.config(bg="gray59")
							etiqueta_vacia.config(bg="gray59")
							self.bandera = True

# -------------------------------- Frame de boton cerrar partida ---------------------------

			if identificador == "Frame4":
				# for j in range(2):
				# 	sub_identificador = f"SubFrameCerrar{j+1}"
				# 	SubFrame = tk.Frame(frame)
				# 	SubFrame.pack(side=lefht, fill="both", expand=True) 
				# 	self.subframesCierre[sub_identificador] = SubFrame
				# 	SubFrame.grid_columnconfigure(j, weight=1)

				#if sub_identificador == "SubFrameCerrar1":
				tk.Button(frame, text="CERRAR", bg= "Green", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack(pady=7)
				frame.config(bg="blue")
					# elif sub_identificador == "SubFrameCerrar2":
					# 	tk.Button(SubFrame, text="ATRAS", bg= "Green", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack(padx=10, side=tk.RIGHT)
					# 	SubFrame.config(bg="#AFEEEE")

# ---------------------------------------- Frame botones sube/baja--------------------------

			if identificador == "Frame5":
				numero_rango = 0
				valor_actual = 0
				
				

				for j in range(11):
					sub_identificador = f"Frame{j+1}"
					Subframe = tk.Frame(self.root)
					Subframe.pack(side="left", fill="both", expand=True)
					self.subframesBotones[sub_identificador] = Subframe
					#SubFrame.grid_columnconfigure(j, weight=1)
 					
					if sub_identificador == "Frame1":
						tk.Button(Subframe, text="Histórico", bg= "Green", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack(pady=10)#, command=poner_al_frente_root
						tk.Button(Subframe, text= "RESET", bg= "#8B0000", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack()#, command=reset
						tk.Button(Subframe, command=lambda: salir(root), text= "SALIR", bg= "red", fg="White", font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack(pady=10)#, command= cerrar

					elif sub_identificador == "Frame11":
 						boton_prepara_rectifica=tk.Button(Subframe, text="  COMENZAR  ", bg="#8B0000", fg ="#F0F8FF", font=("Times New Roman", 15,"bold"),cursor="hand2" )#,command = PreparaRectifica
 						boton_prepara_rectifica.pack()

 						boton_atras=tk.Button(Subframe, text="ATRAS", bg= "Green", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7)
 						boton_atras.pack()


 						tk.Label(Subframe,text="CARBI-93 S.A.").pack()
 						tk.Label(Subframe,text="(Grupo Automáticos Canarios)").pack()

						

					else:
						
						rango = self.rangos[numero_rango]
						etiqueta_numero_rango = tk.Label(Subframe, text = rango, font=("Times New Roman",15,"bold"))
						etiqueta_numero_rango.pack()
						numero_rango += 1

						etiqueta_series = tk.Label(Subframe, text = "SERIES",bg="gray59", font=("Arial",10,"bold"))
						etiqueta_series.pack()

						valor = self.valores[valor_actual]
						self.etiqueta_numero_series = tk.Label(Subframe, text=valor, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=2)
						self.etiqueta_numero_series.pack()
						self.lista_series_frame_5.append(self.etiqueta_numero_series)
						valor_actual += 1

						#botones_frame_inferior()
						
						for i in range(3):
							identificador = f"boton{self.numero_boton+1}"
							boton = tk.Button(Subframe,cursor="hand2")
							boton.pack(padx=10, pady=5)
							self.botones[identificador] = boton #frames
							self.numero_boton += 1

							if identificador == "boton1":
								boton.config(image=self.photoSube, command=lambda idx=i: sube_serie(self, idx))
							elif identificador == "boton2":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2")
							elif identificador == "boton3":
								boton.config(image=self.photoBaja, command=lambda idx=i: baja_serie(self, idx-2))
							elif identificador == "boton4":
								boton.config(image=self.photoSube, command=lambda idx=i: sube_serie(self, idx+1))
							elif identificador == "boton5":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2")
							elif identificador == "boton6":
								boton.config(image=self.photoBaja, command=lambda idx=i: baja_serie(self, idx-1))
							elif identificador == "boton7":
								boton.config(image=self.photoSube, command=lambda idx=i: sube_serie(self, idx+2))
							elif identificador == "boton8":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2")
							elif identificador == "boton9":
								boton.config(image=self.photoBaja, command=lambda idx=i: baja_serie(self, idx))
							elif identificador == "boton10":
								boton.config(image=self.photoSube, command=lambda idx=i: sube_serie(self, idx+3))
							elif identificador == "boton11":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2")
							elif identificador == "boton12":
								boton.config(image=self.photoBaja, command=lambda idx=i: baja_serie(self, idx+1))
							elif identificador == "boton13":
								boton.config(image=self.photoSube, command=lambda idx=i: sube_serie(self, idx+4))
							elif identificador == "boton14":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2")
							elif identificador == "boton15":
								boton.config(image=self.photoBaja, command=lambda idx=i: baja_serie(self, idx+2))
							elif identificador == "boton16":
								boton.config(image=self.photoSube, command=lambda idx=i: sube_serie(self, idx+5))
							elif identificador == "boton17":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2")
							elif identificador == "boton18":
								boton.config(image=self.photoBaja, command=lambda idx=i: baja_serie(self, idx+3))
							elif identificador == "boton19":
								boton.config(image=self.photoSube, command=lambda idx=i: sube_serie(self, idx+6))
							elif identificador == "boton20":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2")
							elif identificador == "boton21":
								boton.config(image=self.photoBaja, command=lambda idx=i: baja_serie(self, idx+4))
							elif identificador == "boton22":
								boton.config(image=self.photoSube, command=lambda idx=i: sube_serie(self, idx+7))
							elif identificador == "boton23":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2")
							elif identificador == "boton24":
								boton.config(image=self.photoBaja, command=lambda idx=i: baja_serie(self, idx+5))
							elif identificador == "boton25":
								boton.config(image=self.photoSube, command=lambda idx=i: sube_serie(self, idx+8))
							elif identificador == "boton26":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2")
							elif identificador == "boton27":
								boton.config(image=self.photoBaja, command=lambda idx=i: baja_serie(self, idx+6))					

						if self.bandera:
							Subframe.config(bg="#C0C0C0")
							etiqueta_numero_rango.config(bg="#C0C0C0")
							etiqueta_series.config(bg="#C0C0C0")
							self.bandera = False
						else:
							Subframe.config(bg="gray59")
							etiqueta_numero_rango.config(bg="gray59")
							etiqueta_series.config(bg="gray59")
							self.bandera = True

# def probar():
# 	app.etiqueta_liquidacion["liquidacion_liqui1"].config(text=100)
	
if __name__ == "__main__":
	root = tk.Tk()
	app = VentanaApp(root)
	root.mainloop()
