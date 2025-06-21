import tkinter as tk
from quiz_screens import InicioScreen, QuizScreen # Asegúrate de que QuizScreen exista en quiz_screens.py
from stats_screen import StatsScreen
from quiz_database import QuizDatabase

class MainApp:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.title("Mi Juego de Preguntas")
        self.db = QuizDatabase()  # Instancia la base de datos aquí

        self.screens = {}
        self.current_screen_name = None # Para rastrear la pantalla actual

        # Crea instancias de todas las pantallas.
        # Las pantallas se instancian UNA SOLA VEZ.
        # No les pases datos dinámicos del quiz aquí, esos se pasan a sus métodos de "inicio_quiz".
        self.screens["InicioScreen"] = InicioScreen(master, self.db, self)
        
        # Importante: QuizScreen ahora se inicializa sin preguntas ni tiempo.
        # Esos datos se le pasan a un método posterior (iniciar_quiz_data).
        # También se le pasa la instancia de la app.
        self.screens["QuizScreen"] = QuizScreen(master, self.db, self) # Pasa la DB y la app
        
        self.screens["StatsScreen"] = StatsScreen(master, self.db, self)
        # Si tienes EndScreen, instánciala aquí también:
        # self.screens["EndScreen"] = EndScreen(master, self.db, self) 

        # Inicialmente, muestra la pantalla de inicio
        self.show_frame("InicioScreen")

    # MODIFICADO: Acepta **kwargs para pasar datos a la pantalla que se muestra
    def show_frame(self, page_name, **kwargs):
        """
        Muestra un frame para el nombre de página dado y pasa kwargs si los hay.
        """
        frame = self.screens[page_name]
        
        # Oculta todos los demás frames
        for name, f in self.screens.items():
            if f != frame:
                f.pack_forget()

        # Muestra el frame solicitado
        frame.pack(fill="both", expand=True)
        self.current_screen_name = page_name # Actualiza la pantalla actual
        
        # Llama a un método específico en el frame si existe y si se pasaron kwargs
        if page_name == "QuizScreen" and "preguntas" in kwargs:
            # Llama al método de QuizScreen para inicializar los datos del quiz
            frame.iniciar_quiz_data(kwargs["preguntas"], kwargs["tiempo_limite"], kwargs["quiz_filename"])
        elif page_name == "StatsScreen":
            # Recarga los datos de estadísticas cada vez que se visita
            frame.cargar_estadisticas()
            # frame.mostrar_grafico_puntuaciones() # Ya se llama dentro de cargar_estadisticas

        self.master.deiconify() 
        self.master.lift() 

    # MODIFICADO: Implementa la lógica de "volver al inicio" con la "X"
    def on_closing(self):
        """
        Método para manejar el cierre de la ventana principal.
        Si no estamos en InicioScreen, vuelve a ella. De lo contrario, cierra la app.
        """
        if self.current_screen_name != "InicioScreen":
            # Si no estamos en InicioScreen, vamos a InicioScreen
            self.show_frame("InicioScreen")
        else:
            # Si ya estamos en InicioScreen, cierra la aplicación
            if self.db:
                self.db.close()
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing) # Asocia la función on_closing con la "X"
    root.mainloop()