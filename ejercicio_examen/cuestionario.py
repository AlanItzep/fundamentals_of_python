import tkinter as tk
from quiz_screens import InicioScreen # Importa la pantalla de inicio

class MainApp:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.title("Mi Juego de Preguntas")

        self.inicio_screen = InicioScreen(master)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()