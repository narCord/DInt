import tkinter as tk
from PIL import Image, ImageTk
from detail_window import open_detail_window


class Cell:
    def __init__(self, title, path, description):
        # En la clase Cell el constructor recibeun titulo y una ruta a una imagen
        self.title = title
        self.path = path
        self.description = description
        # Abro la imagen, la redimensiono y creo una referencia a ella (self.image_tk)
        self.resized_image = Image.open(self.path).resize((100, 100), Image.Resampling.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(self.resized_image)
