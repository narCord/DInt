from tkinter import Tk
from difficulty_selection_window import DifficultyWindow
from game_window import GameWindow

if __name__ == '__main__':
    root = Tk()
    app = DifficultyWindow(root)
    # app = GameWindow(root, 'a')
    root.mainloop()
