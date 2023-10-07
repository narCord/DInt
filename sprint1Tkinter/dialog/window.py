from tkinter import ttk, Button
from yes_window import openYesWindow
from no_window import openNoWindow


class MainWindow:
    def on_button_click(self):
        pass

    def __init__(self, root):
        self.root = root

        # Creacion del frame de la ventana
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        # Creacion del label
        self.label = ttk.Label(self.frame, text="¿Si o no?")
        self.label.pack()

        # Creacion de botones
        # El boton del Si invoca la funcion openYesWindow de yes_window.py
        self.button = ttk.Button(self.root, text="Si", command=openYesWindow)
        self.button.pack(side="left", fill="x", expand=True)
        # El boton del No invoca la funcion openNoWindow de no_window.py
        self.button = ttk.Button(self.root, text="No", command=openNoWindow)
        self.button.pack(side="right", fill="x", expand=True)
