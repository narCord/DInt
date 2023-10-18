import tkinter.messagebox
from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import open_detail_window


def about_menu_clicked():
    tkinter.messagebox.showinfo(title="Acerca de", message="Texto de prueba")


class MainWindow:
    def __init__(self, root, json_data):
        # Defino el titulo de la ventana
        root.title("Ventana principal")
        # Posiciona la ventana en el centro de la pantalla
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry(f"+{int(x)}+{int(y)}")
        # Define las dimensiones en pixeles de la ventana que dibujara
        root.geometry("135x250")
        
        # Crea una barra de menu
        menu_bar = tk.Menu()
        help_menu = tk.Menu(menu_bar, tearoff=False)
        # Añade la opcion "Acerca de" a la barra de menu y hace que invoque about_menu_clicked cuando sea clickada
        help_menu.add_command(label="Acerca de", command=about_menu_clicked)
        # Crea la cascada en la barra de menu con el titulo "Ayuda"
        menu_bar.add_cascade(menu=help_menu, label="Ayuda")
        # Asigna la barra de menu a la ventana
        root.config(menu=menu_bar)

        # Variable para posicionar el grid en el loop for
        pos = 0

        # Este loop iterara la lista creada a partir del json
        for element in json_data:
            # Aqui se almacenan los datos del primer elemento del json, tal y como si fuese un diccionario
            self.title = element.get("name")
            self.description = element.get("description")
            self.image_url = element.get("image_url")

            # Instancia una nueva cell con los datos obtenidos del json
            cell = Cell(self.title, self.image_url, self.description)

            # Se asigna a una label un titulo y una imagen. Se indica que la imagen debe estar debajo del titulo
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)

            # Asigna una posicion a la label en la cuadricula
            label.grid(row=pos, column=0)
            pos += 1

            # Label.bind indica a la label que este pendiente de un evento, en este caso ser clicada
            # El lambda event es una funcion simple y corta que se usa localmente y se activa con el event
            # La ultima parte ejecuta la funcion open_detail window pasando como parametro la celda actual
            label.bind("<Button-1>", lambda event, celda=cell: open_detail_window(celda))
