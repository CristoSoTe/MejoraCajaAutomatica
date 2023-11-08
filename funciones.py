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
		self.labels[0].config(text=self.valor1)
	elif num == 2:
		self.valor2 += 1
		self.labels[1].config(text=self.valor2)
	elif num == 3:
		self.valor3 += 1
		self.labels[2].config(text=self.valor3)
	elif num == 4:
		self.valor4 += 1
		self.labels[3].config(text=self.valor4)
	elif num == 5:
		self.valor5 += 1
		self.labels[4].config(text=self.valor5)
	elif num == 6:
		self.valor6 += 1
		self.labels[5].config(text=self.valor6)
	elif num == 7:
		self.valor7 += 1
		self.labels[6].config(text=self.valor7)
	elif num == 8:
		self.valor8 += 1
		self.labels[7].config(text=self.valor8)
	else:
		self.valor9 += 1
		self.labels[8].config(text=self.valor9)	

# def baja_serie(self, num):
# 	if num == 1:
# 		self.valor1 -= 1
# 		if self.valor1 < 0:
# 			self.valor1 = 0
# 			self.labels[0].config(text=self.valor1)
# 		else:
# 			self.labels[0].config(text=self.valor1)
# 	elif num == 2:
# 		self.valor2 -= 1
# 		if self.valor2 < 0:
# 			self.valor2 = 0
# 			self.labels[1].config(text=self.valor2)
# 		else:
# 			self.labels[1].config(text=self.valor2)
# 	elif num == 3:
# 		self.valor3 -= 1
# 		if self.valor3 < 0:
# 			self.valor3 = 0
# 			self.labels[2].config(text=self.valor3)
# 		else:
# 			self.labels[2].config(text=self.valor3)
# 	elif num == 4:
# 		self.valor4 -= 1
# 		if self.valor4 < 0:
# 			self.valor4 = 0
# 			self.labels[3].config(text=self.valor4)
# 		else:
# 			self.labels[3].config(text=self.valor4)
# 	elif num == 5:
# 		self.valor5 -= 1
# 		if self.valor5 < 0:
# 			self.valor5 = 0
# 			self.labels[4].config(text=self.valor5)
# 		else:
# 			self.labels[4].config(text=self.valor5)
# 	elif num == 6:
# 		self.valor6 -= 1
# 		if self.valor6 < 0:
# 			self.valor6 = 0
# 			self.labels[5].config(text=self.valor6)
# 		else:
# 			self.labels[5].config(text=self.valor6)
# 	elif num == 7:
# 		self.valor7 -= 1
# 		if self.valor7 < 0:
# 			self.valor7 = 0
# 			self.labels[6].config(text=self.valor7)
# 		else:
# 			self.labels[6].config(text=self.valor7)
# 	elif num == 8:
# 		self.valor8 -= 1
# 		if self.valor8 < 0:
# 			self.valor8 = 0
# 			self.labels[7].config(text=self.valor8)
# 		else:
# 			self.labels[7].config(text=self.valor8)
# 	elif num == 9:
# 		self.valor9 -= 1
# 		if self.valor9 < 0:
# 			self.valor9 = 0
# 			self.labels[8].config(text=self.valor9)
# 		else:
# 			self.labels[8].config(text=self.valor9)

# def baja_serie(self, num):
#     if 1 <= num <= 9:
#         index = num - 1
#         valores = [self.valor1, self.valor2, self.valor3, self.valor4, self.valor5, self.valor6, self.valor7, self.valor8, self.valor9]
#         if valores[index] > 0:
#             valores[index] -= 1
#             self.labels[index].config(text=valores[index])
