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

	def carton_salida(self, series, carton, salida_cierre, etiqueta_rango1, salida, precio, lista_Entry):
		numero_carton_siguiente1 = 0
		numero_carton_siguiente2 = 0
		numero_carton_siguiente3 = 0
		numero_carton_siguiente6 = 0

		dato_salida1=lista_Entry[0]
		salida1=dato_salida1.get()
		dato_salida2=lista_Entry[1]
		salida2=dato_salida2.get()
		dato_salida3=lista_Entry[2]
		salida3=dato_salida3.get()
		dato_salida6=lista_Entry[3]
		salida6=dato_salida6.get()
		lista_salidas = [salida1, salida2, salida3, salida6]

		serie_rango1 = etiqueta_rango1.cget("text")
		numero_carton1 = (int(serie_rango1)*6) + int(salida1)
		numero_carton2 = (int(serie_rango1)*6) + int(salida2)
		numero_carton3 = (int(serie_rango1)*6) + int(salida3)
		numero_carton6 = (int(serie_rango1)*6) + int(salida6)
		lista_numero_carton = [numero_carton1, numero_carton2, numero_carton3, numero_carton6]

		#-------------------- Carton salida del rango 2 ---------------------------------
		indices = 0
		for i in lista_numero_carton:
			if series[0].cget("text") == "0" or lista_salidas[indices] == "0":
				carton[indices].config(text="0")
			else:
				carton[indices].config(text=lista_numero_carton[indices])
			indices += 1

		##--------------- Carton salida a 1.5€ ---------------------
		indice_origen1 = 1
		rango_con_serie1 = 1
		indice_destino1 = 4

		for i in series[:7]:
			if salida1 == "0":
				pass

			#--------------- Carton salida del 3 al 9 ----------------------
			else:
				if series[indice_origen1].cget("text") == "0":
					carton[indice_destino1].config(text="0")
					indice_origen1 += 1
					indice_destino1 += 4
					rango_con_serie1 +=1
				else:
					numero_series1 = series[indice_origen1 - rango_con_serie1].cget("text")
					numero_carton_siguiente1 = int(numero_series1) * 6 + numero_carton1 
					carton[indice_destino1].config(text=numero_carton_siguiente1)
					numero_carton1 = numero_carton_siguiente1
					indice_origen1 += 1
					indice_destino1 += 4

					#------ Carton salida cierre
					ultima_serie1 = series[indice_origen1 - 1].cget("text")
					carton_salida_cierre1= (int(ultima_serie1) * 6) + numero_carton1
					salida_cierre[0].config(text=carton_salida_cierre1)

		##--------------- Carton salida 2€ ---------------------
		indice_origen2 = 1
		rango_con_serie2 = 1
		indice_destino2 = 5

		for i in series[:7]:
			if salida2 == "0":
				pass

			#--------------- Carton salida del 3 al 9 ----------------------
			else:
				if series[indice_origen2].cget("text") == "0":
					carton[indice_destino2].config(text="0")
					indice_origen2 += 1
					indice_destino2 += 4
					rango_con_serie2 +=1
				else:
					numero_series2 = series[indice_origen2 - rango_con_serie2].cget("text")
					numero_carton_siguiente2 = int(numero_series2) * 6 + numero_carton2 
					carton[indice_destino2].config(text=numero_carton_siguiente2)
					numero_carton2 = numero_carton_siguiente2
					indice_origen2 += 1
					indice_destino2 += 4

					#------ Carton salida cierre
					ultima_serie2 = series[indice_origen2 - 1].cget("text")
					carton_salida_cierre2= (int(ultima_serie2) * 6) + numero_carton_siguiente2
					salida_cierre[1].config(text=carton_salida_cierre2)

		##--------------- Carton salida a 3€ ---------------------
		indice_origen3 = 1
		rango_con_serie3 = 1
		indice_destino3 = 6

		for i in series[:7]:
			if salida3 == "0":
				pass

			#--------------- Carton salida del 3 al 9 ----------------------
			else:
				if series[indice_origen3].cget("text") == "0":
					carton[indice_destino3].config(text="0")
					indice_origen3 += 1
					indice_destino3 += 4
					rango_con_serie3 +=1
				else:
					numero_series3 = series[indice_origen3 - rango_con_serie3].cget("text")
					numero_carton_siguiente3 = int(numero_series3) * 6 + numero_carton3 
					carton[indice_destino3].config(text=numero_carton_siguiente3)
					numero_carton3 = numero_carton_siguiente3
					indice_origen3 += 1
					indice_destino3 += 4

					#------ Carton salida cierre
					ultima_serie3 = series[indice_origen3 - 1].cget("text")
					carton_salida_cierre3= (int(ultima_serie3) * 6) + numero_carton_siguiente3
					salida_cierre[2].config(text=carton_salida_cierre3)

		##--------------- Carton salida del rango 3 al 9 a 6€ ---------------------
		indice_origen6 = 1
		rango_con_serie6 = 1
		indice_destino6 = 7

		for i in series[:7]:
			if salida6 == "0":
				pass

			#--------------- Carton salida del 3 al 9 ----------------------
			else:
				if series[indice_origen6].cget("text") == "0":
					carton[indice_destino6].config(text="0")
					indice_origen6 += 1
					indice_destino6 += 4
					rango_con_serie6 +=1
				else:
					numero_series6 = series[indice_origen6 - rango_con_serie6].cget("text")
					numero_carton_siguiente6 = int(numero_series6) * 6 + numero_carton6 
					carton[indice_destino6].config(text=numero_carton_siguiente6)
					numero_carton6 = numero_carton_siguiente6
					indice_origen6 += 1
					indice_destino6 += 4

					#------ Carton salida cierre
					ultima_serie6 = series[indice_origen6 - 1].cget("text")
					carton_salida_cierre6= (int(ultima_serie6) * 6) + numero_carton_siguiente6
					salida_cierre[3].config(text=carton_salida_cierre6)			

	def carton_salida_siguiente(self, lista_series, lista_carton_salida, lista_carton_salida_cierre, lista_Entry):
		dato_salida1=lista_Entry[0]
		salida1=dato_salida1.get()

		dato_salida2=lista_Entry[1]
		salida2=dato_salida2.get()

		dato_salida3=lista_Entry[2]
		salida3=dato_salida3.get()

		dato_salida6=lista_Entry[3]
		salida6=dato_salida6.get()

		numero_entry=0
		salida_segun_precio=0

		#-------------------- Carton salida del rango 2 ---------------------------------
		serie_rango1 = lista_series[0].cget("text")
		numero_carton1 = (int(serie_rango1)*6) + int(salida1)
		numero_carton2 = (int(serie_rango1)*6) + int(salida2)
		numero_carton3 = (int(serie_rango1)*6) + int(salida3)
		numero_carton6 = (int(serie_rango1)*6) + int(salida6)
		lista_carton_salida_rango2 = [numero_carton1, numero_carton2, numero_carton3, numero_carton6]
		numero_lista=0

		for i in lista_Entry:
			if lista_series[0].cget("text") == "0" or lista_series[0].cget("text") == "":
				lista_carton_salida[salida_segun_precio].config(text="0")
			else:
				lista_carton_salida[salida_segun_precio].config(text=lista_carton_salida_rango2[numero_lista])

			numero_entry += 1
			salida_segun_precio += 1
			numero_lista +=1

			#indice_destino = 4
		#---------------------Carton salida del rango 3 al 9 -------------------------

		# indice_origen = 1
		# rango_con_serie = 1
		# for i in series[:7]:
		# 	if series[indice_origen].cget("text") == "0":
		# 		carton[indice_destino].config(text="0")
		# 		indice_origen += 1
		# 		indice_destino += 4
		# 		rango_con_serie +=1
		# 	else:
		# 		numero_series = series[indice_origen - rango_con_serie].cget("text")
		# 		numero_carton_siguiente = int(numero_series) * 6 + numero_carton 
		# 		carton[indice_destino].config(text=numero_carton_siguiente)
		# 		numero_carton = numero_carton_siguiente
		# 		indice_origen += 1
		# 		indice_destino += 4

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