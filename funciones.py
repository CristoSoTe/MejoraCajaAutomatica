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

def sube_serie(self, num):
	if num == 1:
		self.valor1 += 1
		self.etiqueta_numero_series.config(text=str(self.valor1))
	if num == 2:
		self.valor2 += 1
		self.etiqueta_numero_series.config(text=str(self.valor2))

def baja_serie(self, num):
	if num == 1:
		self.valor1 -= 1
		self.etiqueta_numero_series.config(text=str(self.valor1))

