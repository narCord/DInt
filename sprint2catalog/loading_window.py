import threading
import tkinter
from tkinter import ttk, Tk

class LoadingWindow:
    def __init__(self, root):
        self.root = root
        self.root.title()
        # Define las dimensiones en pixeles de la ventana que dibujara
        self.root.geometry("170x120")
        # Define si la ventana sera redimensionable. Primer parametro altura, segundo anchura
        self.root.resizable(False, False)

        # Crea una etiqueta y la coloca la parte superior de la ventana con un relleno de 10 pixeles en el eje y
        self.label = tkinter.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tkinter.TOP, pady=10)

        # Almacena en una variable el color de la etiqueta anterior
        label_bg_color = self.label.cget("bg")

        # Crea un lienzo de 60x60 usando de color de fondo la variable anterior
        self.canvas = tkinter.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        # Inicializa el valor del progresso de carga a 0
        self.progress = 0

        self.draw_progress_circle(self.progress)

        self.update_progress_circle()

    # Esta funcion se encarga de dibujar el circulo de carga en el lienzo
    def draw_progress_circle(self, progress):
        # Calcula el angulo que dibujara
        angle = int(360 * (progress / 100))

        # Dibuja el angulo en el lienzo. Los 4 primeros parametros son las coordenadas donde se dibuja
        # El primer par seran las coordenadas de la esquina superior izquierda y el segundo la esquina inferior derecha
        self.canvas.create_arc(10, 10, 35, 35,
                               start=0, extent=angle, tags="progress", outline='green', width=4, style=tkinter.ARC)

    # Esta funcion actualiza el progreso del circulo de carga
    def update_progress_circle(self):
        # Suma a la variable que se utiliza para calcular el angulo
        self.progress += 9
        # Llama a la funcion que dibuja el circulo
        self.draw_progress_circle(self.progress)
        # Esta funcion se llama a si misma de nuevo cada 100 milisegundos
        self.root.after(100, self.update_progress_circle)
