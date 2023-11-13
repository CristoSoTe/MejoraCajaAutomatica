def salir(ventana):
	# global hilo_actualizacion, cliente
	# if MessageBox.askquestion("Salir", "¿Deseas salir de la aplicación?") == "yes":
	# 	detener_hilo.set()
	# 	if cliente:
	# 		cliente.close()
	# try:
	# 	ruta_ejecutable = r"C:\CajaMesaControl\Menu\Menu.exe"
	# 	os.startfile(ruta_ejecutable)
	# except:
	# 	pass
	# if raiz:
	# 	raiz.destroy()
	
	ventana.destroy()

def sube_serie(ventana, num):
	ventana.valores[num] += 1
	ventana.lista_series_frame_5[num].config(text=ventana.valores[num])

def baja_serie(ventana, num):
	dato=ventana.lista_series_frame_5[num].cget("text") 
	if int(dato) > 0:
		ventana.valores[num] -= 1
		ventana.lista_series_frame_5[num].config(text=ventana.valores[num])

def sube_a_venta_un_rango(etiqueta_numero_series_por_rango1_venta, lista_series_frame_5, num):
	etiqueta_numero_series_por_rango1_venta.config(text=lista_series_frame_5[num]["text"])

def sube_a_venta_un_rango_2_9(lista_numero_series_por_rango_venta, lista_series_frame_5, num):
	print(num)
	lista_numero_series_por_rango_venta[num].config(text=lista_series_frame_5[num]["text"])

def comenzar(etiqueta_numero_series_por_rango1_venta, lista_numero_series_por_rango_venta, lista_series_frame_5):
	lista_botones = 0
	lista_venta = 0
	etiqueta_numero_series_por_rango1_venta.config(text=lista_series_frame_5[0]["text"])
	for i in range (1,9):
		lista_numero_series_por_rango_venta[lista_botones].config(text=lista_series_frame_5[lista_venta]["text"])
		lista_botones += 1
		lista_venta += 1

