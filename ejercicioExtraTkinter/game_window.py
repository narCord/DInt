import json
import threading
import tkinter as tk
from io import BytesIO
from tkinter import messagebox
from random import randrange
import requests
from PIL import Image, ImageTk
from difficulty_selection_window import DifficultyWindow


class GameWindow:
    def __init__(self, root, difficulty):
        self.root = root
        self.window_configuration()
        self.difficulty = difficulty

        self.images_json_data = []
        self.words_json_data = []
        self.word_underscores = []
        self.word = ''

        self.fetch_image_json_data()
        self.fetch_words_json_data()

        self.get_word_to_guess()
        self.fails = 0

        response = requests.get(self.images_json_data.get('0'))
        img_data = Image.open(BytesIO(response.content))
        self.hanged_man_image = ImageTk.PhotoImage(img_data)
        self.hanged_man_image_label = tk.Label(self.root, image=self.hanged_man_image)
        self.hanged_man_image_label.pack()

        self.label_word = tk.Label(self.root, text=' '.join(self.word_underscores[1]), font=50)
        self.label_word.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.guess_button = tk.Button(self.root, text='Enviar', command=self.guess_letter)
        self.guess_button.pack()

        self.label_fail_count = tk.Button(self.root, text=' '.join(str(self.fails)), font=50)
        self.label_fail_count.pack(side='right')

        self.failed_letters = []
        self.label_failed_letters = tk.Label(self.root, text=' '.join(self.failed_letters), font=25)
        self.label_failed_letters.pack()

    def fetch_image_json_data(self):
        ima = 'https://raw.githubusercontent.com/narCord/DInt/main/ejercicioExtraTkinter/HangedMan/hangedManImages.json'
        response = requests.get(ima)
        if response.status_code == 200:
            self.images_json_data = response.json()
            # print(self.images_json_data)

    def fetch_words_json_data(self):
        words = 'https://raw.githubusercontent.com/narCord/DInt/main/ejercicioExtraTkinter/palabras.json'
        response = requests.get(words)
        if response.status_code == 200:
            self.words_json_data = response.json()
            # print(self.words_json_data)

    def window_configuration(self):
        self.root.title('Juego del ahorcado')
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 4
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 4
        self.root.geometry(f'+{int(x)}+{int(y)}')
        self.root.geometry('325x300')
        self.root.resizable(False, False)

    def get_word_to_guess(self):
        self.word = self.words_json_data.get(self.difficulty)[randrange(0, 5)]
        word = [i for i in self.word]
        underscores = ['_' for letter in word]
        # print(word)
        # print(underscores)

        self.word_underscores = [word, underscores]

    def guess_letter(self):
        letter = self.entry.get()
        if letter in self.word_underscores[0]:
            for i in range(len(self.word_underscores[0])):
                if self.word_underscores[0][i] == letter:
                    self.word_underscores[1][i] = letter
                    self.label_word.config(text=' '.join(self.word_underscores[1]))
            if "_" not in self.word_underscores[1]:
                self.won_game()
        else:
            self.fails = self.fails + 1
            response = requests.get(self.images_json_data.get(str(self.fails)))
            img_data = Image.open(BytesIO(response.content))
            self.hanged_man_image = ImageTk.PhotoImage(img_data)
            self.hanged_man_image_label.config(image=self.hanged_man_image)
            self.hanged_man_image_label.image = self.hanged_man_image

            self.failed_letters.append(letter)
            self.label_fail_count.config(text=' '.join(str(self.fails)), font=50)
            self.label_failed_letters.config(text=', '.join(self.failed_letters))
            if self.fails == 6:
                self.lost_game()

        self.entry.delete(0, tk.END)

    def lost_game(self):
        messagebox.showinfo(title='Aviso', message='Has perdido... La palabra era ' + self.word)
        self.entry.destroy()
        self.guess_button.destroy()

    def won_game(self):
        messagebox.showinfo(title='Aviso', message='Has ganado!')
        self.entry.destroy()
        self.guess_button.destroy()
