from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox


class MainWindow:
    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda: " + cell.title
        messagebox.showinfo("Informacion", message)

    def __init__(self, root):
        root.title("Ventana principal")
        default_path = "D:\\usuario\\Documentos\\Clase\\DInt\\sprint1Tkinter\\catalog\\data\\"

        # Creo una lista de Cells y le paso a cada celda su titulo y ruta
        self.cells = [
            Cell("Ciudades de la llanura", default_path + "edited\\CiudadesDeLaLlanura.jpg"),
            Cell("El Aleph", default_path + "edited\\ElAleph.jpg"),
            Cell("El forastero misterioso", default_path + "edited\\ElForasteroMisterioso.jpg"),
            Cell("Esto es agua", default_path + "edited\\EstoEsAgua.jpg"),
            Cell("Hamlet", default_path + "edited\\Hamlet.jpg")
        ]

        # Este loop crea una label con un titulo e imagen por cada iteracion
        for i, cell in enumerate(self.cells):
            # Se asigna a una label un titulo y una imagen. Se indica que la imagen debe estar debajo del titulo
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)

            # Asigna una posicion a la label en la cuadricula
            label.grid(row=i, column=0)

            # Label.bind indica a la label que este pendiente de un evento, en este caso ser clicada
            # El lambda event es una funcion simple y corta que se usa localmente y se activa con el event
            # La ultima parte ejecuta la funcion on_button_clicked pasando como parametro la celda actual
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(celda))
