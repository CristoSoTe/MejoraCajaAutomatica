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
	def sube_todas_las_series_a_venta(origen, destino, etiqueta_rango1):
		contenido_rango1 = origen[0].cget("text")
		etiqueta_rango1.config(text=contenido_rango1)
		for label_origen, label_destino in zip(origen[1:], destino):
			contenido_actual = label_origen.cget("text")
			label_destino.config(text=contenido_actual)

	def sube_a_venta_un_rango_2_9(self,origen, destino, etiqueta_rango1, indice):
		if indice == 0:
			contenido_rango1 = origen[0].cget("text")
			etiqueta_rango1.config(text=contenido_rango1)
		else:
			contenido_actual=origen[indice].cget("text")
			destino[indice-1].config(text=contenido_actual)

	#@staticmethod
	def subir_series_a_liquidacion(self, origen, destino, etiqueta_rango1):
		self.pico = self.pico_sal
		contenido_rango1 = etiqueta_rango1.cget("text")
		#texto_etiqueta = f"{contenido_rango1} + {self.pico}"
		destino[0].config(text=f"{contenido_rango1} + {self.pico}")

		for label_origen, label_destino in zip(origen, destino[1:9]):
			contenido_actual = label_origen.cget("text")
			label_destino.config(text=contenido_actual)

	def calcula_liquidacion(self, origen, destino, etiqueta_rango1, precio):
		contenido_rango1 = origen[0].cget("text")
		primer_elemento = contenido_rango1.split()[0].strip()
		liquidacion_rango1 = ((int(primer_elemento) * 6) + self.pico) * float(precio)
		destino[0].config(text=f"{liquidacion_rango1}€")
		indice = 1
		for elemento in origen[1:]:
			dato= round(int(elemento.cget("text")) * 6, 2)
			resultado = dato * float(precio)
			destino[indice].config(text=f"{resultado}€")
			indice += 1

	def cartones_en_liquidacion(self,origen, destino, salida):
		primero = origen[0].cget("text")
		numeros = [int(n) for n in primero.split() if n.isdigit()]
		resultado = ((numeros[0] * 6) + numeros[1]) + int(salida)
		if resultado > 1800:
			diferencia = resultado - 1800			
			destino[0].config(text=f"{salida} - {diferencia}")
		else:
			diferencia=resultado - 1
			destino[0].config(text=f"{salida} - {diferencia}")
		indice_destino = 1
		indice_origen = 1
		carton_inicial = diferencia + 1

		for i in destino[1:]:
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

	def pico_salida(self, salida):
		if salida == 0 or salida == "":
			pass
		else:
			self.pico_sal = 7 - (int(salida) % 6)
			if self.pico_sal == 7:
				self.pico_sal = 1
			elif self.pico_sal == 6:
				self.pico_sal = 0
			# else:
			# 	return self.pico_sal

	def salir(self, root):
		root.destroy()
		exit()