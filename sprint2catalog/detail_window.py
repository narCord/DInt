import tkinter
from tkinter import Tk, ttk


# Esta funcion recibe una instancia de cell como parametro
def open_detail_window(cell):
    root = tkinter.Toplevel()
    root.title(cell.title)

    # Esta label escribe el titulo, recibido como parametro
    title_label = ttk.Label(root, text=cell.title)
    title_label.pack(side="top")

    # Esta label escribe la descripcion, recibida como parametro
    desc_label = ttk.Label(root, text=cell.description)
    desc_label.pack(side="bottom")

    # Esta label dibuja la imagen recibida como parametro
    image_label = ttk.Label(root, image=cell.image_tk)
    image_label.pack(side="bottom")
