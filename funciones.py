class Funciones:
	def __init__(self, labels):
		self.labels = labels

	def incrementar_serie(self, index):
		contenido_actual = int(self.labels[index].cget("text"))
		nuevo_contenido = contenido_actual + 1
		self.labels[index].config(text=str(nuevo_contenido))

	def decrementar_serie(self, index):
		contenido_actual = int(self.labels[index].cget("text"))
		if contenido_actual > 0:
			nuevo_contenido = contenido_actual - 1
			self.labels[index].config(text=str(nuevo_contenido))

	@staticmethod
	def sube_todas_las_series_a_venta(origen, destino, etiqueta_rango1):
		print(len(origen))
		contenido_rango1 = origen[0].cget("text")
		etiqueta_rango1.config(text=contenido_rango1)
		for label_origen, label_destino in zip(origen[1:], destino):
			contenido_actual = label_origen.cget("text")
			label_destino.config(text=contenido_actual)

	@staticmethod
	def subir_series_a_liquidacion(origen, destino, etiqueta_rango1):
		contenido_rango1 = etiqueta_rango1.cget("text")
		destino[0].config(text=contenido_rango1)
		for label_origen, label_destino in zip(origen, destino[1:9]):
			contenido_actual = label_origen.cget("text")
			label_destino.config(text=contenido_actual)

	def sube_a_venta_un_rango_2_9(self,origen, destino, index):
		print("Hola")
		print(len(origen))
		contenido_actual=origen[index].cget("text")
		destino[index-1].config(text=contenido_actual)


	def salir(self, root):
		root.destroy()
		exit()

