import tkinter as tk

class VentanaApp:
	def __init__(self, root):
		
		self.root = root
		self.root.title("Caja Automática")
		self.frames = {}

		for i in range(5):
			identificador = f"Frame{i+1}"
			frame = tk.Frame(self.root)
			frame.pack(side="top", fill="both", expand=True)
			self.frames[identificador] = frame

		# ---------------------- Frame de liquidación -----------------------------------------

			if identificador == "Frame1":
				for i in range(5):
					identificador = f"Frame{i+1}"
					frame = tk.Frame(self.root)
					frame.pack(side="top", fill="both", expand=True)
					self.frames[identificador] = frame

					if identificador == "Frame3": 
						def botones_frame_inferior():
							for i in range(3):
								identificador = f"boton{i+1}"
								boton = tk.Button(frame,cursor="hand2")
								boton.pack(padx=10, pady=5 )
								self.frames[identificador] = boton

								if identificador == "boton1":
									boton.config(text= "Aumente")
								elif identificador == "boton2":
									boton.config(text="SUBIR", bg="#8B0000", fg ="#F0F8FF" ,cursor="hand2")
								else:
									boton.config(text="Disminuye")

						etiqueta = tk.Label(frame, text="10", fg="blue", bg = "white", font=("Times New Roman",17,"bold"), width=2)
						etiqueta.pack()

						botones_frame_inferior()


if __name__ == "__main__":
	root = tk.Tk()
	app = VentanaApp(root)
	root.mainloop()