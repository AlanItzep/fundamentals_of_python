import tkinter as tk
from tkinter import ttk, messagebox
import os
from quiz_database import QuizDatabase
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class StatsScreen(tk.Frame):
    def __init__(self, master, db_instance, app_instance):
        super().__init__(master)
        self.master = master
        self.db = db_instance
        self.app = app_instance

        # Configura las filas y columnas para que se expandan
        # Row 0: Título (no expandible, weight=0)
        # Row 1: Tabla (expandible, weight=3)
        # Row 2: Gráfico (expandible, weight=4)
        # Row 3: Controles/Botones (no expandible, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=3) 
        self.grid_rowconfigure(2, weight=4) 
        self.grid_rowconfigure(3, weight=0) 

        self.grid_columnconfigure(0, weight=1) # Columna única, se expande horizontalmente

        self.crear_widgets_grid() # Llama al nuevo método para grid

    def crear_widgets_grid(self):
        # Título (Fila 0)
        tk.Label(self, text="Estadísticas del Quiz", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=20, sticky="nsew")

        # --- Frame para la TABLA (Fila 1) ---
        self.table_section_frame = tk.Frame(self, bd=2, relief="groove")
        self.table_section_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10) # sticky="nsew" para llenar la celda

        # Configurar la expansión dentro de table_section_frame para el Treeview y el Scrollbar
        self.table_section_frame.grid_rowconfigure(0, weight=1)
        self.table_section_frame.grid_columnconfigure(0, weight=1)
        self.table_section_frame.grid_columnconfigure(1, weight=0) # Para el scrollbar

        # Crear un Treeview (tabla)
        self.stats_tree = ttk.Treeview(self.table_section_frame, columns=("ID", "Quiz", "Correctas", "Total", "Tiempo", "Fecha"), show="headings")
        self.stats_tree.grid(row=0, column=0, sticky="nsew") # sticky="nsew" para llenar la celda

        # Definir los encabezados de las columnas
        self.stats_tree.heading("ID", text="ID")
        self.stats_tree.heading("Quiz", text="Archivo Quiz")
        self.stats_tree.heading("Correctas", text="Correctas")
        self.stats_tree.heading("Total", text="Total Preguntas")
        self.stats_tree.heading("Tiempo", text="Tiempo (mm:ss)")
        self.stats_tree.heading("Fecha", text="Fecha y Hora")

        # Configurar el ancho de las columnas
        self.stats_tree.column("ID", width=30, anchor="center")
        self.stats_tree.column("Quiz", width=150, anchor="w")
        self.stats_tree.column("Correctas", width=80, anchor="center")
        self.stats_tree.column("Total", width=100, anchor="center")
        self.stats_tree.column("Tiempo", width=100, anchor="center")
        self.stats_tree.column("Fecha", width=150, anchor="w")

        # Añadir scrollbar vertical
        scrollbar = ttk.Scrollbar(self.table_section_frame, orient="vertical", command=self.stats_tree.yview)
        self.stats_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns") # Columna 1 del table_section_frame

       # --- Frame para el GRÁFICO (Fila 2) ---
        self.graph_section_frame = tk.Frame(self, bd=2, relief="groove")
        self.graph_section_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

        # Configurar la expansión dentro de graph_section_frame
        self.graph_section_frame.grid_rowconfigure(0, weight=1)
        self.graph_section_frame.grid_rowconfigure(1, weight=0)
        self.graph_section_frame.grid_columnconfigure(0, weight=1)

        # Crear una figura de Matplotlib
        self.figure = Figure(figsize=(10, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)

        # Crear el lienzo de Tkinter para la figura de Matplotlib
        self.canvas_matplotlib = FigureCanvasTkAgg(self.figure, master=self.graph_section_frame)
        self.canvas_matplotlib_widget = self.canvas_matplotlib.get_tk_widget()
        self.canvas_matplotlib_widget.grid(row=0, column=0, sticky="nsew")

        # Añadir una barra de herramientas de navegación (zoom, pan, guardar)
        # ¡CAMBIO CRÍTICO AQUÍ: Añade pack_toolbar=False!
        self.toolbar = NavigationToolbar2Tk(self.canvas_matplotlib, self.graph_section_frame, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=1, column=0, sticky="ew") # <-- Esto ya estaba bien
        
        # --- Frame para los CONTROLES (Botones) (Fila 3) ---
        self.controls_frame = tk.Frame(self)
        self.controls_frame.grid(row=3, column=0, sticky="ew", padx=20, pady=10) # sticky="ew" para llenar el ancho

        # Botón para volver al menú principal
        # Aquí puedes usar pack() dentro de controls_frame ya que solo hay un botón
        tk.Button(self.controls_frame, text="Volver al Inicio",
                  command=lambda: self.app.show_frame("InicioScreen"),
                  font=("Arial", 12)).pack(pady=10) 

    def cargar_estadisticas(self):
        # Limpiar Treeview antes de cargar nuevos datos
        for item in self.stats_tree.get_children():
            self.stats_tree.delete(item)

        attempts = self.db.get_all_attempts()

        for attempt in attempts:
            _id, quiz_filename, correct_answers, total_questions, time_taken_seconds, timestamp = attempt
            
            formatted_time = "N/A"
            if time_taken_seconds is not None:
                minutes = time_taken_seconds // 60
                seconds = time_taken_seconds % 60
                formatted_time = f"{minutes:02}:{seconds:02}"
            
            self.stats_tree.insert("", "end", values=(
                _id, 
                quiz_filename, 
                f"{correct_answers}/{total_questions}", 
                total_questions, 
                formatted_time, 
                timestamp
            ))
        self.mostrar_grafico_puntuaciones() # Llama a la función para actualizar el gráfico


    def mostrar_grafico_puntuaciones(self):
        attempts_raw = self.db.get_all_attempts()

        self.ax.clear() # Limpiar el eje actual antes de dibujar uno nuevo

        if not attempts_raw:
            self.ax.text(0.5, 0.5, 'No hay datos de quizzes para mostrar.', 
                         horizontalalignment='center', verticalalignment='center', 
                         transform=self.ax.transAxes, fontsize=12, color='gray')
            self.canvas_matplotlib.draw() 
            return

        df = pd.DataFrame(attempts_raw, columns=["id", "quiz_filename", "correct_answers", "total_questions", "time_taken_seconds", "timestamp"])
        df["percentage_correct"] = (df["correct_answers"] / df["total_questions"]) * 100
        
        labels = [f"ID {row['id']}\n{row['quiz_filename']} ({row['timestamp'][:10]})" for index, row in df.iterrows()]
        
        self.ax.bar(labels, df["percentage_correct"], color='skyblue') 
        
        self.ax.set_xlabel("Intento de Quiz")
        self.ax.set_ylabel("Porcentaje de Respuestas Correctas (%)")
        self.ax.set_title("Rendimiento en Quizzes por Intento")
        self.ax.tick_params(axis='x', rotation=45, ha="right") 
        
        self.figure.tight_layout() # Ajustar el diseño para evitar solapamientos

        self.canvas_matplotlib.draw() # Redibujar el lienzo de Matplotlib
    
    def volver_a_inicio(self):
        self.app.show_frame("InicioScreen")