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
		self.photoSube=tk.PhotoImage(file=r"c:\CajaMesaControl\flechaSube.png")
		self.photoBaja=tk.PhotoImage(file=r"c:\CajaMesaControl\flechaBaja.png")

		self.pico_salida=0

		self.liquidacion1=0; self.liquidacion2=0; self.liquidacion3=0; self.liquidacion4=0; self.liquidacion5=0;
		self.liquidacion6=0; self.liquidacion7=0; self.liquidacion8=0; self.liquidacion9=0; self.liquidacion_cierre=0; self.liquidacion_total=0;

		self.series_liquidacion_rango1="0 - 0"; self.series_liquidacion_rango2=0; self.series_liquidacion_rango3=0; self.series_liquidacion_rango4=0; self.series_liquidacion_rango5=0;
		self.series_liquidacion_rango6=0; self.series_liquidacion_rango7=0; self.series_liquidacion_rango8=0; self.series_liquidacion_rango9=0; self.series_liquidacion_cierre="0 - 0";
		self.series_liquidacion_total=0;

		self.cartones_liquidacion1=0; self.cartones_liquidacion2=0;self.cartones_liquidacion3=0; self.cartones_liquidacion4=0; self.cartones_liquidacion5=0;
		self.cartones_liquidacion6=0; self.cartones_liquidacion7=0;self.cartones_liquidacion8=0; self.cartones_liquidacion9=0; self.cartones_liquidacion_cierre=0;
		self.cartones_liquidacion_total=0; 


		self.valor1=0; self.valor2=0; self.valor3=0; self.valor4=0; self.valor5=0;
		self.valor6=0; self.valor7=0; self.valor8=0; self.valor9 = 0
		
		self.labels = []
		self.lista_liquidacion = []
		self.lista_numero_series_liquidacion = []
		self.lista_cartones_liquidacion = []
		self.botones = {}
		self.numero_boton = 0

		self.rangos = ["RANGO 1", "RANGO 2", "RANGO 3", "RANGO 4", "RANGO 5", "RANGO 6", "RANGO 7", "RANGO 8", "RANGO 9", "CIERRE", "TOTAL"]

		self.numero_series = ["liquidacion_liqui1","liquidacion_liqui2", "liquidacion_liqui3","liquidacion_liqui4","liquidacion_liqui5",
		"liquidacion_liqui6", "liquidacion_liqui7","liquidacion_liqui8", "liquidacion_liqui9", "liquidacion_liqui_cierre", "liquidacion_liqui_total"]

		self.etiquetas_premios = ["PRECIO", "DEL", "IMPRESOS", "RECAUDADO", "PREMIO LINEA", "PRIMA", "VENDIDOS", "AL", "INFORMATICOS","CAJA IMPRESOS", "PREMIO BINGO", "PRIMA EXTRA"]

		self.liquidacion = [self.liquidacion1, self.liquidacion2, self.liquidacion3, self.liquidacion4, self.liquidacion5, self.liquidacion6, self.liquidacion7, self.liquidacion8, self.liquidacion9, self.liquidacion_cierre, self.liquidacion_total]

		self.numero_series_liquidacion = [self.series_liquidacion_rango1, self.series_liquidacion_rango2, self.series_liquidacion_rango3, self.series_liquidacion_rango4, self.series_liquidacion_rango5, self.series_liquidacion_rango6, self.series_liquidacion_rango7, self.series_liquidacion_rango8, self.series_liquidacion_rango9, self.series_liquidacion_cierre, self.series_liquidacion_total]

		self.cartones_liquidacion = [self.cartones_liquidacion1, self.cartones_liquidacion2, self.cartones_liquidacion3, self.cartones_liquidacion4, self.cartones_liquidacion5, self.cartones_liquidacion6, self.cartones_liquidacion7, self.cartones_liquidacion8, self.cartones_liquidacion9, self.cartones_liquidacion_cierre, self.cartones_liquidacion_total]

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
					tk.Label(frame, text = etiqueta_premio, bg="blue", fg= "white", font=("Times New Roman",13,"bold")).grid(row = valor_fila, column = valor_columna, sticky = "ew", padx= 10)
					valor_columna += 1
					tk.Entry(frame).grid(row = valor_fila, column = valor_columna, sticky = "ew")
					valor_columna += 1
					if valor_columna > 11:
						valor_fila = 1
						valor_columna = 0

# -------------------------------- Frame de venta -----------------------------------

			if identificador == "Frame3":
				indice_rango_venta = 1
				for j in range(11):
					indice_rango_venta = 1
					
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

						if self.bandera:
							subframe.config(bg="#C0C0C0")
							etiqueta_numero_rango_venta.config(bg="#C0C0C0")
							# series_liquidacion.config(bg="#C0C0C0")
							# del_al_liquidacion.config(bg="#C0C0C0")
							self.bandera = False
						else:
							subframe.config(bg="gray59")
							etiqueta_numero_rango_venta.config(bg="gray59")
							# series_liquidacion.config(bg="gray59")
							# del_al_liquidacion.config(bg="gray59")
							self.bandera = True

# -------------------------------- Frame de boton cerrar partida ---------------------------

			if identificador == "Frame4":
				for j in range(2):
					sub_identificador = f"SubFrameCerrar{j+1}"
					SubFrame = tk.Frame(frame)
					SubFrame.pack(side="left", fill="both", expand=True) 
					self.subframesCierre[sub_identificador] = SubFrame
					SubFrame.grid_columnconfigure(j, weight=1)

					if sub_identificador == "SubFrameCerrar1":
						tk.Button(SubFrame, text="CERRAR", bg= "Green", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack(side=tk.RIGHT)
						SubFrame.config(bg="red")
					elif sub_identificador == "SubFrameCerrar2":
						tk.Button(SubFrame, text="ATRAS", bg= "Green", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7).pack()
						SubFrame.config(bg="blue")

# ---------------------------------------- Frame botones sube/baja--------------------------

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

						valor = self.valores[valor_actual]
						self.etiqueta_numero_series = tk.Label(frame, text=valor, fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=2)
						self.etiqueta_numero_series.pack()
						self.labels.append(self.etiqueta_numero_series)
						valor_actual += 1

						#botones_frame_inferior()
						
						for i in range(3):
							identificador = f"boton{self.numero_boton+1}"
							boton = tk.Button(frame,cursor="hand2")
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
