from tkinter import ttk, messagebox, Canvas, Scrollbar, Frame
import tkinter as tk
from cell import Cell
from detail_window import open_detail_window


def about_menu_clicked():
    messagebox.showinfo(title="Acerca de", message="Texto de prueba")


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

        # Crea un nuevo canvas
        self.canvas = Canvas(root)
        # Se indica que el scrollbar se movera en el eje y del canvas
        self.scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        # El frame es el widget desplazable
        self.scrollable_frame = Frame(self.canvas)

        # Esta funcion lambda hace la region desplazable del canvas se actualize cada vez que se actualiza el Frame
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Situa el frame en las coordenadas 0, 0 del canvas y lo ancla al noroeste
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        # Vincula el scrollbar al canvas para que se actualize cuando se desplaza en canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Este loop iterara la lista creada a partir del json
        for element in json_data:
            # Aqui se almacenan los datos del primer elemento del json, tal y como si fuese un diccionario
            self.title = element.get("name")
            self.description = element.get("description")
            self.image_url = element.get("image_url")

            # Instancia una nueva cell con los datos obtenidos del json
            cell = Cell(self.title, self.image_url, self.description)

            self.add_item(cell)

        # Posiciona el canvas en la ventana principal y permite que se expanda en todas las direcciones
        self.canvas.grid(row=0, column=0, sticky="nsew")
        # Posiciona el scrollbar la ventana principal junto al canvas y permite su expansion vertical
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Configuran el grid para que se redimensione proporcionalmente cuando lo hace la ventana principal
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

    # Este metodo se encarga de añadir las celdas al frame
    def add_item(self, cell):
        frame = Frame(self.scrollable_frame)
        frame.pack(pady=10)

        # Se asigna a una label un titulo y una imagen. Se indica que la imagen debe estar debajo del titulo
        label = ttk.Label(frame, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)

        # Asigna una posicion a la label en la cuadricula
        label.grid(row=0, column=0)

        # Label.bind indica a la label que este pendiente de un evento, en este caso ser clicada
        # El lambda event es una funcion simple y corta que se usa localmente y se activa con el event
        # La ultima parte ejecuta la funcion open_detail window pasando como parametro la celda actual
        label.bind("<Button-1>", lambda event, celda=cell: open_detail_window(celda))
