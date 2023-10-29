import sys
from tkinter import ttk
import tkinter
from game_window import GameWindow


class DifficultyWindow:
    def __init__(self, root):
        self.root = root
        self.window_configuration()
        self.selected_difficulty = ''

        self.button_creation()

    def window_configuration(self):
        self.root.title('Selección de dificultad')
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2.3
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 3
        self.root.geometry(f'+{int(x)}+{int(y)}')
        self.root.geometry('300x150')
        self.root.resizable(False, False)

    def button_creation(self):
        ttk.Label(text='Elija la dificultad de la partida', font=30).pack()
        # Boton facil
        ttk.Button(text='Fácil', width=15, command=lambda: self.launch_game('Facil')).pack()
        # Boton normal
        ttk.Button(text='Normal',  width=15, command=lambda: self.launch_game('Normal')).pack()
        # Boton dificil
        ttk.Button(text='Difícil',  width=15, command=lambda: self.launch_game('Dificil')).pack()
        # Boton de salir
        ttk.Button(text='Salir', command=sys.exit).pack(side='bottom')

    def launch_game(self, difficulty):
        self.root.destroy()
        root = tkinter.Tk()
        app = GameWindow(root, difficulty)
        root.mainloop()
