import tkinter as tk
from PIL import Image, ImageTk


class Cell:
    def __init__(self, title, path):
        # En la clase Cell el constructor recibeun titulo y una ruta a una imagen
        self.title = title
        self.path = path
        # Con la libreria Pillow podemos mostrar una imagen en pantalla indicandole su ruta
        self.image_tk = ImageTk.PhotoImage(file=self.path)
