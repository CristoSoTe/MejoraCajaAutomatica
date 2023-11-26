from tkinter import font

class Funciones:
	def __init__(self, labels):
		self.labels = labels
		self.pico_sal = 0

	def incrementar_serie(self, indice):
		contenido_actual = int(self.labels[indice].cget("text"))
		nuevo_contenido = contenido_actual + 1
		self.labels[indice].config(text=str(nuevo_contenido))

	def decrementar_serie(self, indice):
		contenido_actual = int(self.labels[indice].cget("text"))
		if contenido_actual > 0:
			nuevo_contenido = contenido_actual - 1
			self.labels[indice].config(text=str(nuevo_contenido))

	#@staticmethod
	def sube_todas_las_series_a_venta(self, origen, destino, etiqueta_rango1):
		#------------- Sube a venta el rango 1 con el boton comenzar -------------------
		contenido_rango1 = origen[0].cget("text")
		etiqueta_rango1.config(text=contenido_rango1)

		#------------- imprime en venta desde el rango 2 hasta el cierre con el boton comenzar ----------------------
		for label_origen, label_destino in zip(origen[1:], destino):
			contenido_actual = label_origen.cget("text")
			label_destino.config(text=contenido_actual)

	def sube_a_venta_un_rango_2_9(self,origen, destino, etiqueta_rango1, indice):
		#------------- Imprime en venta el rango 1 con el boton individual -------------------
		if indice == 0:
			contenido_rango1 = origen[0].cget("text")
			etiqueta_rango1.config(text=contenido_rango1)

		#------------ Sube a venta desde el rango 2 al 9 con el boton individual ----------------
		else:
			contenido_actual=origen[indice].cget("text")
			destino[indice-1].config(text=contenido_actual)

	def subir_series_a_liquidacion(self, origen, destino, etiqueta_rango1, impresos):
		#---------------------- Calcula todas las series vendidas ------------------------
		self.series_vendidas = (int(impresos) - self.pico_sal - int(self.pico_cie)) // 6

		#---------------------- Imprime en liquidacion las series vendidas en el rango 1 mas el pico de salida ---------------
		contenido_rango1 = etiqueta_rango1.cget("text")
		destino[0].config(text=f"{contenido_rango1} + {self.pico_sal}")

		#--------------------- Imprime en liquidacion el total de las series vendidas --------------------------
		destino[10].config(text=f"{self.series_vendidas}")

		#--------------------- Imprime en liquidacion las series del rango 2 al 9 -----------------------
		for label_origen, label_destino in zip(origen, destino[1:9]):
			contenido_actual = label_origen.cget("text")
			label_destino.config(text=contenido_actual)

		#-------------------- Imprime en liquidacion las series del cierre ----------------
		contenido_rango1_liquidacion = destino[0].cget("text") 
		primer_elemento_rango1_liquidacion = contenido_rango1_liquidacion.split()[0].strip()
		total_series_cierre = 0
		for elemento in destino[1:9]:
			contenido = elemento.cget("text")
			total_series_cierre += int(contenido)
		series_cierre = self.series_vendidas - total_series_cierre - int(primer_elemento_rango1_liquidacion)
		destino[9].config(text=f"{series_cierre} - { self.pico_cie}")

	def calcula_liquidacion(self, origen, destino, etiqueta_rango1, precio):

		#----------------- Imprime la liquidacion del rango 1 ------------------------------
		contenido_rango1 = origen[0].cget("text")
		primer_elemento_rango1 = contenido_rango1.split()[0].strip()
		liquidacion_rango1 = ((int(primer_elemento_rango1) * 6) + self.pico_sal) * float(precio)
		destino[0].config(text=f"{liquidacion_rango1}€")

		#------------------ Imprime la liquidacion del rango de cierre --------------------------
		contenido_rango10 = origen[9].cget("text")
		primer_elemento_cierre = contenido_rango10.split()[0].strip()
		liquidacion_cierre = ((int(primer_elemento_cierre) * 6) + self.pico_cie) * float(precio)
		destino[9].config(text=f"{liquidacion_cierre}€")

		#------------------ Imprime la liquidacion total ---------------------------------
		liquidacion_total = ((self.series_vendidas * 6) + self.pico_cie + self.pico_sal) * float(precio)
		destino[10].config(text=f"{liquidacion_total}€")

		#------------------ Imprime la liquidacion del rango 2 al 9 ------------------------
		indice = 1
		for elemento in origen[1:9]:
			dato= round(int(elemento.cget("text")) * 6, 2)
			resultado = dato * float(precio)
			destino[indice].config(text=f"{resultado}€")
			indice += 1

	def cartones_en_liquidacion(self,origen, destino, salida, cierre):

		#------------- Imprime los cartones que lleva el rango 1 --------------------
		primero = origen[0].cget("text")
		numeros = [int(n) for n in primero.split() if n.isdigit()]
		resultado = ((numeros[0] * 6) + numeros[1]) + int(salida)
		if resultado > 1800:
			diferencia = resultado - 1800			
			destino[0].config(text=f"{salida} - {diferencia}")
		else:
			diferencia=resultado - 1
			destino[0].config(text=f"{salida} - {diferencia}")

		#--------------- Imprime los cartones que llevan desde el rango 2 al 9 -------------
		indice_destino = 1
		indice_origen = 1
		carton_inicial = diferencia + 1

		for i in destino[1:9]:
			if int(origen[indice_origen].cget("text")) > 0: 
				carton_final=(int(origen[indice_origen].cget("text")) * 6 + diferencia)
				if carton_final > 1800:
					if carton_inicial > 1800:
						carton_inicial = carton_inicial - 1800
					carton_final = carton_final - 1800
					destino[indice_destino].config(text=f"{carton_inicial} - {carton_final}")
				else:
					destino[indice_destino].config(text=f"{carton_inicial} - {carton_final}")
				carton_inicial = carton_final + 1
				diferencia = carton_final
			else:
				destino[indice_destino].config(text=0)
			indice_destino +=1
			indice_origen += 1

		#-------------- Imprime los cartones que lleva el cierre ------------------------------
		if carton_inicial > 1800:
			carton_inicial = carton_inicial - 1800
			destino[9].config(text=f"{carton_inicial-1800} - {cierre}")
		else:
			destino[9].config(text=f"{carton_inicial} - {cierre}")


	




	def carton_salida(self, series, carton, etiqueta_rango1, salida, precio):

		serie_rango1 = etiqueta_rango1.cget("text")
		numero_carton = (int(serie_rango1)*6) + int(salida)
		carton[0].config(text=numero_carton)

		indice_origen = 0
		indice_destino = 4


		for i in series:

			if series[indice_origen].cget("text") != "0":
				numero_series = series[indice_origen].cget("text")
				print(numero_series)
				numero_carton = int(numero_series) * 6
				carton[indice_destino].config(text=numero_carton)
				indice_origen += 1
				indice_destino += 4 



	






	def pico_salida(self, salida):
		try:
			if salida == 0 or salida == "":
				pass
			else:
				self.pico_sal = 7 - (int(salida) % 6)
				if self.pico_sal == 7:
					self.pico_sal = 1
				elif self.pico_sal == 6:
					self.pico_sal = 0
		except:
			pass

	def pico_cierre(self, cierre):
		try:
			if cierre == "0" or cierre == "":
				pass
			else:
				self.pico_cie = (int(cierre) % 6)
		except:
			pass

	def salir(self, root):
		root.destroy()
		exit()