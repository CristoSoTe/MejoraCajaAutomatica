import tkinter as tk 
from tkinter import messagebox as MessageBox
import os
import random
import socket
import re
import time
import threading
from funciones import Funciones
from tkinter import font

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

		
		
		
		self.lista_liquidacion = []
		self.lista_numero_series_liquidacion = []
		self.lista_numero_series_por_rango_venta = []
		self.lista_cartones_liquidacion = []
		self.lista_carton_salida_2_9 = []
		self.lista_carton_salida_siguiente_2_9 = []
		# self.lista_carton_salida_2 = []
		# self.lista_carton_salida_siguiente_2 = []
		# self.lista_carton_salida_3 = []
		# self.lista_carton_salida_siguiente_3 = []
		# self.lista_carton_salida_6 = []
		# self.lista_carton_salida_siguiente_6 = []
		self.lista_Entry_carton_salida = []
		self.lista_carton_salida_cierre = []
		self.lista_series_frame_5 = []
		self.lista_carton_salida_siguiente_cierre = []


		self.numero_boton = 0

		self.rangos = ["RANGO 1", "RANGO 2", "RANGO 3", "RANGO 4", "RANGO 5", "RANGO 6", "RANGO 7", "RANGO 8", "RANGO 9", "CIERRE", "TOTAL"]

		self.numero_series = ["liquidacion_liqui1","liquidacion_liqui2", "liquidacion_liqui3","liquidacion_liqui4","liquidacion_liqui5",
		"liquidacion_liqui6", "liquidacion_liqui7","liquidacion_liqui8", "liquidacion_liqui9", "liquidacion_liqui_cierre", "liquidacion_liqui_total"]

		self.etiquetas_premios = ["PRECIO", "DEL", "IMPRESOS", "RECAUDADO", "PREMIO LINEA", "PRIMA", "VENDIDOS", "AL", "INFORMATICOS","CAJA IMPRESOS", "PREMIO BINGO", "PRIMA EXTRA"]

		#--------------------------------------------- Listas liquidacion -----------------------------

		

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

						self.etiqueta_liquidacion_rango1 = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
						self.etiqueta_liquidacion_rango1.pack()
						self.lista_liquidacion.append(self.etiqueta_liquidacion_rango1)

						self.series_liquidacion_rango1=tk.Label(subframe, text = "SERIES + Pico", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						self.series_liquidacion_rango1.pack()

						self.etiqueta_numero_series_liquidacion_rango1 = tk.Label(subframe, text="0", fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=4)
						self.etiqueta_numero_series_liquidacion_rango1.pack()
						self.lista_numero_series_liquidacion.append(self.etiqueta_numero_series_liquidacion_rango1)

						del_al_liquidacion_rango1=tk.Label(subframe, text = "DEL-AL", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						del_al_liquidacion_rango1.pack()

						self.etiqueta_cartones_liquidacion_rango1 = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=8)
						self.etiqueta_cartones_liquidacion_rango1.pack()
						self.lista_cartones_liquidacion.append(self.etiqueta_cartones_liquidacion_rango1)

					elif SubIdentificador == "SubFrameLiquidacion10":
						subframe.config(bg="#00FFFF")
						self.etiqueta_cierre_liquidacion = tk.Label(subframe, text = "CIERRE", font=("Times New Roman",20,"bold"), bg="#00FFFF", fg="#009900")
						self.etiqueta_cierre_liquidacion.pack()

						self.etiqueta_liquidacion_cierre = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
						self.etiqueta_liquidacion_cierre.pack()
						self.lista_liquidacion.append(self.etiqueta_liquidacion_cierre)

						series_liquidacion_cierre=tk.Label(subframe, text = "SERIES + Pico", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						series_liquidacion_cierre.pack()

						self.etiqueta_numero_series_liquidacion_cierre = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=4)
						self.etiqueta_numero_series_liquidacion_cierre.pack()
						self.lista_numero_series_liquidacion.append(self.etiqueta_numero_series_liquidacion_cierre)

						del_al_liquidacion_cierre=tk.Label(subframe, text = "DEL-AL", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						del_al_liquidacion_cierre.pack()

						self.etiqueta_cartones_liquidacion_cierre = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=8)
						self.etiqueta_cartones_liquidacion_cierre.pack()
						self.lista_cartones_liquidacion.append(self.etiqueta_cartones_liquidacion_rango1)

					elif SubIdentificador == "SubFrameLiquidacion11":
						subframe.config(bg="#0099ff")
						etiqueta_total_liquidacion = tk.Label(subframe, text = "TOTAL", font=("Times New Roman",20,"bold"), bg="#0099ff")
						etiqueta_total_liquidacion.pack()

						self.etiqueta_liquidacion_total = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
						self.etiqueta_liquidacion_total.pack()
						self.lista_liquidacion.append(self.etiqueta_liquidacion_total)

						series_liquidacion_total=tk.Label(subframe, text = "SERIES", font=("Times New Roman", 15,"bold"), bg="#0099ff")
						series_liquidacion_total.pack()

						self.etiqueta_numero_series_liquidacion_total = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=2)
						self.etiqueta_numero_series_liquidacion_total.pack()
						self.lista_numero_series_liquidacion.append(self.etiqueta_numero_series_liquidacion_total)

						del_al_liquidacion_total=tk.Label(subframe, text = "DEL-AL", font=("Times New Roman", 15,"bold"), bg="#0099ff")
						del_al_liquidacion_total.pack()

						self.etiqueta_cartones_liquidacion_total = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=8)
						self.etiqueta_cartones_liquidacion_total.pack()
						self.lista_cartones_liquidacion.append(self.etiqueta_cartones_liquidacion_total)

					else:

						rango = self.rangos[indice_rango]
						etiqueta_numero_rango_liquidacion = tk.Label(subframe, text = rango, font=("Times New Roman",20,"bold"))
						etiqueta_numero_rango_liquidacion.pack()
						indice_rango += 1

						#liquidacion_rango = self.liquidacion[indice_liquidacion]
						self.etiqueta_liquidacion = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
						self.etiqueta_liquidacion.pack()
						self.lista_liquidacion.append(self.etiqueta_liquidacion)
						indice_liquidacion += 1

						series_liquidacion=tk.Label(subframe, text = "SERIES", font=("Times New Roman", 15,"bold"))
						series_liquidacion.pack()

						#numero_series_por_rango_liquidacion = self.numero_series_liquidacion[indice_liquidacion]
						self.etiqueta_numero_series_liquidacion = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=2)
						self.etiqueta_numero_series_liquidacion.pack()
						self.lista_numero_series_liquidacion.append(self.etiqueta_numero_series_liquidacion)
						indice_liquidacion += 1

						del_al_liquidacion=tk.Label(subframe, text = "DEL-AL", font=("Times New Roman", 15,"bold"))
						del_al_liquidacion.pack()

						#cartones_rango_liquidacion = self.cartones_liquidacion[indice_liquidacion]
						self.etiqueta_cartones_liquidacion = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=8)
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
				self.entradas = []
				for etiqueta_premio in self.etiquetas_premios:
					tk.Label(frame, text = etiqueta_premio, bg="blue", fg= "white", font=("Times New Roman",13,"bold"), anchor="e", justify="right").grid(row = valor_fila, column = valor_columna, sticky = "ew", padx= 10)
					valor_columna += 1
					entrada = tk.Entry(frame, font=("Times New Roman",13,"bold"), justify="right", width=14)
					entrada.grid(row = valor_fila, column = valor_columna, sticky = "ew")
					valor_columna += 1

					self.entradas.append(entrada)

					if valor_columna > 11:
						valor_fila = 1
						valor_columna = 0

				self.entradas[0].insert(0, "1.5")
				dato_precio =self.entradas[0]
				self.precio= dato_precio.get()

				self.entradas[1].insert(0, "1790")
				dato_desde = self.entradas[1]
				self.desde = dato_desde.get()

				self.entradas[2].insert(0, "100")
				dato_impresos = self.entradas[2]
				self.impresos = dato_impresos.get()

				self.entradas[3].insert(0, round(int(self.impresos) * float(self.precio),2))
				dato_recaudado = self.entradas[3]
				self.recaudado = dato_recaudado.get()

				self.entradas[4].insert(0, round(float(self.recaudado) * 0.085, 2))
				dato_linea = self.entradas[4]
				self.linea = dato_linea.get()

				self.entradas[5].insert(0, "100")
				dato_prima = self.entradas[5]
				self.prima = dato_prima.get()

				self.entradas[6].insert(0, 100)
				dato_vendidos = self.entradas[6]				
				self.vendidos = dato_vendidos.get()

				self.entradas[7].insert(0, "100")
				dato_al = self.entradas[7]
				self.al = dato_al.get()

				self.entradas[8].insert(0, "0")
				dato_informaticos = self.entradas[8]
				self.informaticos = dato_informaticos.get()

				self.entradas[9].insert(0, round((int(self.impresos) * 1.5) * 0.37, 2))
				dato_caja_impresos = self.entradas[9]
				self.caja_impresos = dato_caja_impresos.get()

				self.entradas[10].insert(0, round(float(self.recaudado) * 0.37, 2))
				dato_bingo = self.entradas[10]
				self.bingo = dato_bingo.get()

				self.entradas[11].insert(0, "100")
				dato_prima_extra = self.entradas[11]
				self.prima_extra = dato_prima_extra.get()
 
				
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
						subframe.config( bg="gray59")
						lista_precios = ["1,5€", "2€", "3€", "6€"]
						tk.Label(subframe, text="Precios", font=("Times New Roman",20,"bold"), bg="gray59").pack(pady=40)
						for i in lista_precios:
							tk.Label(subframe, text= i, font=("Times New Roman",20,"bold"), bg="gray59", fg="blue").pack(pady=18)

					elif subIdentificador == "SubFrameVenta2":
						subframe.config(bg="#00FFFF")
						self.etiqueta_numero_rango1_venta = tk.Label(subframe, text = "RANGO1", font=("Times New Roman",20,"bold"), bg="#00FFFF", fg="#009900")
						self.etiqueta_numero_rango1_venta.pack()
						indice_carton_salida_inicial = 0

						etiquetas_series_venta=tk.Label(subframe, text = "SERIES", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						etiquetas_series_venta.pack()

						self.etiqueta_numero_series_por_rango1_venta = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
						self.etiqueta_numero_series_por_rango1_venta.pack()

						etiquetas_salidas_venta1=tk.Label(subframe, text = "SALIDAS", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						etiquetas_salidas_venta1.pack()

						for h in range(4):
							self.Entry_carton_salida = tk.Entry(subframe, text="", fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6, justify="right")
							self.Entry_carton_salida.pack(pady=16)
							self.lista_Entry_carton_salida.append(self.Entry_carton_salida)

						self.lista_Entry_carton_salida[0].insert(0, "1790")
						dato_salida1 =self.lista_Entry_carton_salida[0]
						self.salida1= dato_salida1.get()

						self.lista_Entry_carton_salida[1].insert(0, "200")
						dato_salida2 = self.lista_Entry_carton_salida[1]
						self.salida2 = dato_salida2.get()

						self.lista_Entry_carton_salida[2].insert(0, "300")
						dato_salida3 = self.lista_Entry_carton_salida[2]
						self.salida3 = dato_salida3.get()

						self.lista_Entry_carton_salida[3].insert(0, "600")
						dato_salida6 = self.lista_Entry_carton_salida[3]
						self.salida6 = dato_salida6.get()

						etiqueta_vacia = tk.Label(subframe, text="", font=("Times New Roman",4,"bold"), bg="#00FFFF")
						etiqueta_vacia.pack()

					elif subIdentificador == "SubFrameVenta11":
						subframe.config(bg="#00FFFF")
						self.etiqueta_cierre_venta = tk.Label(subframe, text = "CIERRE", font=("Times New Roman",20,"bold"), bg="#00FFFF", fg="#009900")
						self.etiqueta_cierre_venta.pack()
						indice_carton_salida_cierre = 0

						etiqueta_vacia2 = tk.Label(subframe, text="", font=("Times New Roman",4,"bold"), bg="#00FFFF")
						etiqueta_vacia2.pack(pady=38)

						for r in range(4):
							#carton_salida_cierre = self.etiqueta_numero_carton_salida_cierre[indice_carton_salida_cierre]
							self.etiqueta_carton_salida_cierre = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
							self.etiqueta_carton_salida_cierre.pack()
							self.lista_carton_salida_cierre.append(self.etiqueta_carton_salida_cierre)

							#carton_salida_siguiente_cierre = self.numero_carton_salida_siguiente_cierre[indice_carton_salida_cierre]
							self.etiqueta_carton_salida_siguiente_cierre = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",15,"bold"), width=4)
							self.etiqueta_carton_salida_siguiente_cierre.pack(pady=1)
							self.lista_carton_salida_siguiente_cierre.append(self.etiqueta_carton_salida_siguiente_cierre)

							etiqueta_vacia = tk.Label(subframe, text="", font=("Times New Roman",4,"bold"), bg="#00FFFF")
							etiqueta_vacia.pack()
							indice_carton_salida_cierre += 1

					else:
						rango = self.rangos[indice_rango_venta]
						etiqueta_numero_rango_venta = tk.Label(subframe, text = rango, font=("Times New Roman",20,"bold"))
						etiqueta_numero_rango_venta.pack()
						indice_rango_venta += 1

						etiquetas_series_venta=tk.Label(subframe, text = "SERIES", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						etiquetas_series_venta.pack()

						#numero_series_por_rango_venta = self.numero_series_venta[indice_series_venta]
						self.etiqueta_numero_series_por_rango_venta = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=3)
						self.etiqueta_numero_series_por_rango_venta.pack()
						self.lista_numero_series_por_rango_venta.append(self.etiqueta_numero_series_por_rango_venta)
						self.series_en_venta=Funciones(self.lista_numero_series_por_rango_venta)

						indice_series_venta += 1

						etiquetas_salidas_venta=tk.Label(subframe, text = "SALIDAS", font=("Times New Roman", 15,"bold"), bg="#00FFFF")
						etiquetas_salidas_venta.pack()

						#------------------------------- Etiquetas Carton Salida ---------------------------------------
						for h in range(4):
							#carton_salida = self.numero_carton_salida_2_9[indice_carton_salida]
							self.etiqueta_carton_salida_2_9 = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=6)
							self.etiqueta_carton_salida_2_9.pack()
							self.lista_carton_salida_2_9.append(self.etiqueta_carton_salida_2_9)

							#carton_salida_siguiente_2_9 = self.numero_carton_salida_siguiente_2_9[indice_carton_salida]
							self.etiqueta_carton_salida_siguiente_2_9 = tk.Label(subframe, text=0, fg="blue", bg = "white", font=("Times New Roman",15,"bold"), width=4)
							self.etiqueta_carton_salida_siguiente_2_9.pack(pady=1)
							self.lista_carton_salida_siguiente_2_9.append(self.etiqueta_carton_salida_siguiente_2_9)

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
				tk.Button(frame, text="CERRAR", command=self.liquidar_partida, bg= "Green", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack(pady=7)
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
						tk.Button(Subframe, command=self.salir, text= "SALIR", bg= "red", fg="White", font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack(pady=10)#, command= cerrar

					elif sub_identificador == "Frame11":
 						boton_prepara_rectifica=tk.Button(Subframe, text="  COMENZAR  ", bg="#8B0000", fg ="#F0F8FF", font=("Times New Roman", 15,"bold"),cursor="hand2", command=self.sube_todas_las_series_a_venta)#,command = PreparaRectifica
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

						self.etiqueta_numero_series = tk.Label(Subframe, text="0", fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=2)
						self.etiqueta_numero_series.pack()
						self.lista_series_frame_5.append(self.etiqueta_numero_series)
						valor_actual += 1
						self.series_frame_5=Funciones(self.lista_series_frame_5)

						#botones_frame_inferior()
						
						for i in range(3):
							identificador = f"boton{self.numero_boton+1}"
							boton = tk.Button(Subframe,cursor="hand2")
							boton.pack(padx=10, pady=5)
							self.botones[identificador] = boton #frames
							self.numero_boton += 1

							if identificador == "boton1":
								boton.config(image=self.photoSube, command=lambda i=i: self.incrementar_serie(i))
							elif identificador == "boton2":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2", command=lambda: self.sube_a_venta_un_rango_2_9(0))
							elif identificador == "boton3":
								boton.config(image=self.photoBaja, command=lambda i=i: self.decrementar_serie(i-2))
							elif identificador == "boton4":
								boton.config(image=self.photoSube, command=lambda i=i: self.incrementar_serie(i+1))
							elif identificador == "boton5":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2", command=lambda: self.sube_a_venta_un_rango_2_9(1))
							elif identificador == "boton6":
								boton.config(image=self.photoBaja, command=lambda i=i: self.decrementar_serie(i-1))
							elif identificador == "boton7":
								boton.config(image=self.photoSube, command=lambda i=i: self.incrementar_serie(i+2))
							elif identificador == "boton8":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2", command=lambda: self.sube_a_venta_un_rango_2_9(2))
							elif identificador == "boton9":
								boton.config(image=self.photoBaja, command=lambda i=i: self.decrementar_serie(i))
							elif identificador == "boton10":
								boton.config(image=self.photoSube, command=lambda i=i: self.incrementar_serie(i+3))
							elif identificador == "boton11":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2", command=lambda: self.sube_a_venta_un_rango_2_9(3))
							elif identificador == "boton12":
								boton.config(image=self.photoBaja, command=lambda i=i: self.decrementar_serie(i+1))
							elif identificador == "boton13":
								boton.config(image=self.photoSube, command=lambda i=i: self.incrementar_serie(i+4))
							elif identificador == "boton14":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2", command=lambda: self.sube_a_venta_un_rango_2_9(4))
							elif identificador == "boton15":
								boton.config(image=self.photoBaja, command=lambda i=i: self.decrementar_serie(i+2))
							elif identificador == "boton16":
								boton.config(image=self.photoSube, command=lambda i=i: self.incrementar_serie(i+5))
							elif identificador == "boton17":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2", command=lambda: self.sube_a_venta_un_rango_2_9(5))
							elif identificador == "boton18":
								boton.config(image=self.photoBaja, command=lambda i=i: self.decrementar_serie(i+3))
							elif identificador == "boton19":
								boton.config(image=self.photoSube, command=lambda i=i: self.incrementar_serie(i+6))
							elif identificador == "boton20":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2", command=lambda: self.sube_a_venta_un_rango_2_9(6))
							elif identificador == "boton21":
								boton.config(image=self.photoBaja, command=lambda i=i: self.decrementar_serie(i+4))
							elif identificador == "boton22":
								boton.config(image=self.photoSube, command=lambda i=i: self.incrementar_serie(i+7))
							elif identificador == "boton23":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2", command=lambda: self.sube_a_venta_un_rango_2_9(7))
							elif identificador == "boton24":
								boton.config(image=self.photoBaja, command=lambda i=i: self.decrementar_serie(i+5))
							elif identificador == "boton25":
								boton.config(image=self.photoSube, command=lambda i=i: self.incrementar_serie(i+8))
							elif identificador == "boton26":
								boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF", cursor="hand2", command=lambda: self.sube_a_venta_un_rango_2_9(8))
							elif identificador == "boton27":
								boton.config(image=self.photoBaja, command=lambda i=i: self.decrementar_serie(i+6))					

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

		self.funciones= Funciones(labels=[])

	def liquidar_partida(self):
		self.funciones.pico_salida(self.salida1)

		self.funciones.subir_series_a_liquidacion(self.lista_numero_series_por_rango_venta, self.lista_numero_series_liquidacion, self.etiqueta_numero_series_por_rango1_venta)#series_en_liquidacion

		self.funciones.calcula_liquidacion(self.lista_numero_series_liquidacion, self.lista_liquidacion, self.etiqueta_numero_series_por_rango1_venta, self.precio)#series_frame_5

		self.funciones.cartones_en_liquidacion(self.lista_numero_series_liquidacion, self.lista_cartones_liquidacion, self.salida1)

		self.funciones.sube_todas_las_series_a_venta(self.lista_series_frame_5, self.lista_numero_series_por_rango_venta, self.etiqueta_numero_series_por_rango1_venta)#series_frame_5
		

	def sube_todas_las_series_a_venta(self):
		self.funciones.sube_todas_las_series_a_venta(self.lista_series_frame_5, self.lista_numero_series_por_rango_venta, self.etiqueta_numero_series_por_rango1_venta)#series_frame_5
	def sube_a_venta_un_rango_2_9(self, indice):
		self.funciones.sube_a_venta_un_rango_2_9(self.lista_series_frame_5, self.lista_numero_series_por_rango_venta, self.etiqueta_numero_series_por_rango1_venta, indice)#series_frame_5

	def incrementar_serie(self, indice): # Funcion que aumenta una serie pulsando el boton subir del rango elegido
		self.series_frame_5.incrementar_serie(indice)

	def decrementar_serie(self, indice): # Funcion que disminuye una serie pulsando el boton bajar del rango elegido
		self.series_frame_5.decrementar_serie(indice)

	

	def salir(self):
		self.funciones.salir(self.root)
	
if __name__ == "__main__":
	root = tk.Tk()
	app = VentanaApp(root)
	root.mainloop()
