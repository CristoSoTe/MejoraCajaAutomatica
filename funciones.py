class Funciones:
	def __init__(self, labels):
		self.labels = labels

	def incrementar_serie(self, indice):
		contenido_actual = int(self.labels[indice].cget("text"))
		nuevo_contenido = contenido_actual + 1
		self.labels[indice].config(text=str(nuevo_contenido))

	def decrementar_serie(self, indice):
		contenido_actual = int(self.labels[indice].cget("text"))
		if contenido_actual > 0:
			nuevo_contenido = contenido_actual - 1
			self.labels[indice].config(text=str(nuevo_contenido))

	@staticmethod
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

	@staticmethod
	def subir_series_a_liquidacion(origen, destino, etiqueta_rango1):
		contenido_rango1 = etiqueta_rango1.cget("text")
		destino[0].config(text=contenido_rango1)
		for label_origen, label_destino in zip(origen, destino[1:9]):
			contenido_actual = label_origen.cget("text")
			label_destino.config(text=contenido_actual)

	def calcula_liquidacion(self, origen, destino, etiqueta_rango1, precio):
		contenido_rango1 = etiqueta_rango1.cget("text")
		destino[0].config(text=int(contenido_rango1) * 6 * float(precio))
		indice = 1
		for elemento in origen[1:]:
			dato= round(int(elemento.cget("text")) * 6, 2)
			resultado = dato * float(precio)
			destino[indice].config(text=resultado)
			indice += 1

	def salir(self, root):
		root.destroy()
		exit()

