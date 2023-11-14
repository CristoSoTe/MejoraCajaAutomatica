class Funciones:
    def __init__(self, labels):
        self.labels = labels

    def incrementar_contenido(self, index):
        contenido_actual = int(self.labels[index].cget("text"))
        nuevo_contenido = contenido_actual + 1
        self.labels[index].config(text=str(nuevo_contenido))