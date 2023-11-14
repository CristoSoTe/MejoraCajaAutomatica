class Funciones:
	def __init__(self, labels):
		self.labels = labels

	def incrementar_contenido(self, index):
		contenido_actual = int(self.labels[index].cget("text"))
		nuevo_contenido = contenido_actual + 1
		self.labels[index].config(text=str(nuevo_contenido))

	def decrementar_contenido(self, index):
		contenido_actual = int(self.labels[index].cget("text"))
		if contenido_actual > 0:
			nuevo_contenido = contenido_actual - 1
			self.labels[index].config(text=str(nuevo_contenido))

	@staticmethod
	def copiar_contenido(origen, destino, etiqueta_rango1):
		contenido_rango1 = origen[0].cget("text")
		etiqueta_rango1.config(text=contenido_rango1)
		for label_origen, label_destino in zip(origen, destino):
			contenido_actual = label_origen.cget("text")
			label_destino.config(text=contenido_actual)




	# def sube_serie(self, num):
	# 	ventana.valores[num] += 1
	# 	ventana.lista_series_frame_5[num].config(text=ventana.valores[num])

	# def baja_serie(self, num):
	# 	dato=ventana.lista_series_frame_5[num].cget("text") 
	# 	if int(dato) > 0:
	# 		ventana.valores[num] -= 1
	# 		ventana.lista_series_frame_5[num].config(text=ventana.valores[num])

	# def sube_a_venta_un_rango(etiqueta_numero_series_por_rango1_venta, lista_series_frame_5, num):
	# 	etiqueta_numero_series_por_rango1_venta.config(text=lista_series_frame_5[num]["text"])

	# def sube_a_venta_un_rango_2_9(lista_numero_series_por_rango_venta, lista_series_frame_5, num):
	# 	print(num)
	# 	lista_numero_series_por_rango_venta[num].config(text=lista_series_frame_5[num]["text"])

	# def comenzar(etiqueta_numero_series_por_rango1_venta, lista_numero_series_por_rango_venta, lista_series_frame_5):
	# 	lista_botones = 0
	# 	lista_venta = 0
	# 	etiqueta_numero_series_por_rango1_venta.config(text=lista_series_frame_5[0]["text"])
	# 	for i in range (1,9):
	# 		lista_numero_series_por_rango_venta[lista_botones].config(text=lista_series_frame_5[lista_venta]["text"])
	# 		lista_botones += 1
	# 		lista_venta += 1
	# 	self.salida(self.lista_Entry_carton_salida[0], self.lista_carton_salida_2_9[0])

	# def salida(self, origen, destino):
	# 	contenido = origen.get()
	# 	destino.config(text=contenido)

