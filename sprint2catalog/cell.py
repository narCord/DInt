import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO


class Cell:
    def __init__(self, title, url, description):
        # En la clase Cell el constructor recibeun titulo y una ruta a una imagen
        self.title = title
        self.url = url
        self.description = description

        # Esta funcion lee la url recibida, abre la imagen y la devuelve
        def load_image_from_url(self, img_url):
            response = requests.get(img_url)
            img_data = Image.open(BytesIO(response.content))
            return ImageTk.PhotoImage(img_data)

        # Almacena la imagen devuelta por la funcion load_image_from_url
        self.image_tk = load_image_from_url(self, self.url)
