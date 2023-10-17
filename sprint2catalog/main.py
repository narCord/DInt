from tkinter import Tk
from window import MainWindow
from loading_window import LoadingWindow

if __name__ == "__main__":
    root = Tk()
    # app = MainWindow(root)
    app = LoadingWindow(root)
    root.mainloop()
