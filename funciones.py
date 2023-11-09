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
	ventana.labels[num].config(text=ventana.valores[num])

def baja_serie(ventana, num):
	dato=ventana.labels[num].cget("text") 
	if int(dato) > 0:
		ventana.valores[num] -= 1
		ventana.labels[num].config(text=ventana.valores[num])

def sube_a_venta_un_rango(ventana, num):
	pass
