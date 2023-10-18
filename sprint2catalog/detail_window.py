import tkinter
from tkinter import Tk, ttk


# Esta funcion recibe una instancia de cell como parametro
def open_detail_window(cell):
    root = tkinter.Toplevel()
    root.title(cell.title)
    # Posiciona la ventana en el centro de la pantalla
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry(f"+{int(x)}+{int(y)}")
    # Define las dimensiones en pixeles de la ventana que dibujara
    root.geometry("135x140")

    # Esta label escribe el titulo, recibido como parametro
    title_label = ttk.Label(root, text=cell.title)
    title_label.pack(side="top")

    # Esta label escribe la descripcion, recibida como parametro
    desc_label = ttk.Label(root, text=cell.description)
    desc_label.pack(side="bottom")

    # Esta label dibuja la imagen recibida como parametro
    image_label = ttk.Label(root, image=cell.image_tk)
    image_label.pack(side="bottom")
