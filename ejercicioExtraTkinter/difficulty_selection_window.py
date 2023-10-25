import threading
import requests
import tkinter


class DifficultyWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Ahorcado')
        self.root.geometry('250x250')
        self.root.resizable(False, False)
