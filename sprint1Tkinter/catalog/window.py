from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk


class MainWindow:
    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda: " + cell.title
        messagebox.showinfo("Informacion", message)

    def __init__(self, root):
        root.title("Ventana principal")
        default_path = "D:\\usuario\\Documentos\\Clase\\DInt\\sprint1Tkinter\\catalog\\data\\unedited\\"

        # Creo una lista de Cells y le paso a cada celda su titulo y ruta
        self.cells = [
            Cell("Ciudades de la llanura", default_path + "CiudadesDeLaLlanura.jpg"),
            Cell("El Aleph", default_path + "ElAleph.jpg"),
            Cell("El forastero misterioso", default_path + "ElForasteroMisterioso.jpg"),
            Cell("Esto es agua", default_path + "EstoEsAgua.jpg"),
            Cell("Hamlet", default_path + "Hamlet.jpg")
        ]

        # Este loop crea una label con un titulo e imagen por cada iteracion
        for i, cell in enumerate(self.cells):
            # Abro la imagen sin editar usando y la reescalo usando Image.open(ruta).resize
            # En lugar de Image.ANTIALIAS he usado Image.Resampling.LANCZOS,
            # ya que antialias fue eliminado en la version 10 de Pillow
            resized_image = Image.open(cell.path).resize((100, 100), Image.Resampling.LANCZOS)
            cell.image_tk = ImageTk.PhotoImage(resized_image)

            # Se asigna a una label un titulo y una imagen. Se indica que la imagen debe estar debajo del titulo
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)

            # Asigna una posicion a la label en la cuadricula
            label.grid(row=i, column=0)

            # Label.bind indica a la label que este pendiente de un evento, en este caso ser clicada
            # El lambda event es una funcion simple y corta que se usa localmente y se activa con el event
            # La ultima parte ejecuta la funcion on_button_clicked pasando como parametro la celda actual
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(celda))
