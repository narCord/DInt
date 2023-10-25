import threading
import requests
import tkinter


class DifficultyWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Ahorcado')
        self.root.geometry('250x250')
        self.root.resizable(False, False)

        self.finished_images_thread = False
        self.finished_words_thread = False
        self.images_json_data = []
        self.words_json_data = []

        self.fetch_image_json_data()
        self.fetch_words_json_data()

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
