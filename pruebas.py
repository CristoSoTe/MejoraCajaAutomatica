import tkinter as tk
from ttkthemes import ThemedTk

root = ThemedTk(theme="arc")  # Cambia el tema según tus preferencias

button = tk.Button(root, text="Botón bonito")
button.pack(pady=20, padx=40)

root.mainloop()