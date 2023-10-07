from tkinter import Tk, ttk


# Defino una funcion que creara una nueva ventana
def openYesWindow():
    root = Tk()
    root.title("yes_window")

    label = ttk.Label(root, text="Yes window")
    label.pack()
