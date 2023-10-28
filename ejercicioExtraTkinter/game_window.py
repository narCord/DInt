import json
import threading
import requests
import tkinter


class GameWindow:
    def __init__(self, root, difficulty):

        self.root = root
        self.window_configuration()

        self.finished_images_thread = False
        self.finished_words_thread = False
        self.images_json_data = []
        self.words_json_data = []

        self.fetch_image_json_data()
        self.fetch_words_json_data()

        print(self.words_json_data.get('Facil')[2])

    def fetch_image_json_data(self):
        ima = 'https://raw.githubusercontent.com/narCord/DInt/main/ejercicioExtraTkinter/HangedMan/hangedManImages.json'
        response = requests.get(ima)
        if response.status_code == 200:
            self.images_json_data = response.json()
            self.finished_images_thread = True
            # print(self.images_json_data)

    def fetch_words_json_data(self):
        words = 'https://raw.githubusercontent.com/narCord/DInt/main/ejercicioExtraTkinter/palabras.json'
        response = requests.get(words)
        if response.status_code == 200:
            self.words_json_data = response.json()
            self.finished_words_thread = True
            # print(self.words_json_data)

    def check_finished_threads(self):
        if self.finished_words_thread and self.finished_images_thread:
            # abrir nueva ventana
            print('a')
        else:
            self.root.after(100, self.check_finished_threads())

    def window_configuration(self):
        self.root.title('Juego del ahorcado')
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 4
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 4
        self.root.geometry(f'+{int(x)}+{int(y)}')
        self.root.geometry('1000x600')
        self.root.resizable(False, False)
