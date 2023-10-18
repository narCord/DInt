import threading
import tkinter
import requests
from window import MainWindow


def launch_main_window(json_data):
    root = tkinter.Tk()
    app = MainWindow(root, json_data)
    root.mainloop()


class LoadingWindow:
    def __init__(self, root):
        self.root = root
        self.root.title()
        # Define las dimensiones en pixeles de la ventana que dibujara
        self.root.geometry("170x120")
        # Define si la ventana sera redimensionable. Primer parametro altura, segundo anchura
        self.root.resizable(False, False)

        self.finished = False
        self.json_data = []

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

        self.check_thread()

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()

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
        self.progress += 10
        # Llama a la funcion que dibuja el circulo
        self.draw_progress_circle(self.progress)
        # Esta funcion se llama a si misma de nuevo cada 100 milisegundos
        self.root.after(100, self.update_progress_circle)

    # Esta funcion recoge los datos del json alojado en el link
    # Si el codigo de respuesta es igual 200, es decir, exitoso, almacenara los datos del json leido en un array
    # y pondra self.finished a True
    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/narCord/DAM/main/recursos/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished = True
            # print(self.json_data)

    # Esta funcion detecta si el thread que lee el json ha terminado, si lo ha hecho destruye la ventana actual y lanza
    # launch_main_window pasando el array json_data como parametro, si no lo ha hecho se repite a si misma cada 100ms
    def check_thread(self):
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)
