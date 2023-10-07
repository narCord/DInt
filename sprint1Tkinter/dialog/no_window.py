from tkinter import Tk, ttk


# Defino una funcion que creara una nueva ventana
def openNoWindow():
    root = Tk()
    root.title("no_window")

    label = ttk.Label(root, text="No window")
    label.pack()
