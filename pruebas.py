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

        	if identificador == "Frame1":
	        	for i in range(11):
	        		sub_identificador = f"SubFrame{i+1}"
	        		sub_frame = tk.Frame(frame)
	        		sub_frame.pack(side="left", fill="both", expand=True)
	        		self.frames[sub_identificador] = sub_frame
	        		sub_frame.grid_columnconfigure(i, weight=1)
	        		if sub_identificador == "SubFrame1":
	        			sub_frame.configure(bg="blue")  # Configura el color de fondo del subframe
	        			tk.Label(sub_frame, text="Hola").pack()
	        		else:
	        			tk.Label(sub_frame, text="Adios").pack()
        	else:
        		pass
        		#tk.Label(frame, text="Adios")
        		

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaApp(root)
    root.mainloop()