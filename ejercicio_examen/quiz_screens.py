import os
import tkinter as tk
from tkinter import messagebox, filedialog
import random
import time
from quiz_utils import cargar_preguntas
from quiz_database import QuizDatabase

class InicioScreen(tk.Frame):
    def __init__(self, master, db_instance, app_instance):
        super().__init__(master)
        self.master = master
        self.db = db_instance
        self.app = app_instance

        self.selected_file_path = tk.StringVar(value="No se ha seleccionado archivo") 
        self.quiz_filename = "questions.txt" # Nombre de archivo por defecto

        self.crear_widgets()
        self.selected_file_path.set(f"Usando por defecto: {os.path.basename(self.quiz_filename)}")

    def crear_widgets(self):
        tk.Label(self, text="Configuración del Quiz", font=("Arial", 16, "bold")).pack(pady=20)

        # Sección de selección de archivo
        tk.Label(self, text="Archivo del Quiz:", font=("Arial", 12)).pack(pady=(10, 0))
        tk.Label(self, textvariable=self.selected_file_path, font=("Arial", 10), fg="blue").pack(pady=(0, 10))
        tk.Button(self, text="Seleccionar Archivo de Quiz", command=self.seleccionar_archivo_quiz, font=("Arial", 10)).pack(pady=5)
        
        # El valor por defecto ya se establece en __init__

        tk.Frame(self, height=2, bd=1, relief=tk.SUNKEN).pack(fill="x", padx=20, pady=10)

        # Opciones de temporizador
        self.usar_temporizador_var = tk.BooleanVar(value=False)
        tk.Checkbutton(self, text="Usar Temporizador", variable=self.usar_temporizador_var, 
                       command=self.toggle_tiempo_input, font=("Arial", 12)).pack(pady=5)
        tk.Label(self, text="Tiempo límite (minutos):", font=("Arial", 12)).pack(pady=5)
        self.tiempo_entrada = tk.Entry(self, width=10, font=("Arial", 12))
        self.tiempo_entrada.insert(0, "2")
        self.tiempo_entrada.pack(pady=5)

        tk.Button(self, text="Iniciar Quiz", command=self.iniciar_quiz, font=("Arial", 14, "bold")).pack(pady=20)
        tk.Button(self, text="Ver Estadísticas", command=self.ver_estadisticas, font=("Arial", 12)).pack(pady=10)

        self.toggle_tiempo_input()
    
    def seleccionar_archivo_quiz(self):
        file_path = filedialog.askopenfilename(
            title="Selecciona un archivo de preguntas",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if file_path:
            self.quiz_filename = file_path
            self.selected_file_path.set(f"Archivo seleccionado: {os.path.basename(self.quiz_filename)}") 
        else:
            self.quiz_filename = "questions.txt" 
            self.selected_file_path.set(f"Usando por defecto: {os.path.basename(self.quiz_filename)}") 

    def toggle_tiempo_input(self):
        if self.usar_temporizador_var.get():
            self.tiempo_entrada.config(state=tk.NORMAL)
        else:
            self.tiempo_entrada.config(state=tk.DISABLED)

    def iniciar_quiz(self):
        tiempo_limite = None
        if self.usar_temporizador_var.get():
            try:
                tiempo_en_minutos = int(self.tiempo_entrada.get())
                if tiempo_en_minutos <= 0:
                    messagebox.showerror("Error de Tiempo", "El tiempo debe ser un número positivo de minutos.")
                    return
                tiempo_limite = tiempo_en_minutos * 60
            except ValueError:
                messagebox.showerror("Error de Tiempo", "Por favor, introduce un número válido para los minutos del tiempo límite.")
                return
        
        preguntas_cargadas = cargar_preguntas(self.quiz_filename) 
        if not preguntas_cargadas:
            return

        # Ahora show_frame acepta los kwargs y los pasa a QuizScreen.iniciar_quiz_data
        self.app.show_frame("QuizScreen", 
                            preguntas=preguntas_cargadas, 
                            tiempo_limite=tiempo_limite, 
                            quiz_filename=self.quiz_filename)

    def ver_estadisticas(self):
        self.app.show_frame("StatsScreen")

    def salir_app(self):
        self.app.on_closing()


class QuizScreen(tk.Frame):
    # MODIFICADO: No espera las preguntas/tiempo en __init__.
    # Se le pasa la instancia de la app y la DB, pero los datos del quiz se pasan después.
    def __init__(self, master, db_instance, app_instance):
        super().__init__(master)
        self.master = master
        self.db = db_instance
        self.app = app_instance # Guarda la referencia a MainApp

        # Inicializa variables que serán establecidas por iniciar_quiz_data
        self.preguntas = []
        self.tiempo_limite = None
        self.tiempo_restante = None
        self.quiz_filename = "unknown"

        self.timer_id = None
        self.has_finished = False 
        self.start_time = None 

        self.opciones_seleccionadas_vars = {} 
        self.checkbuttons_referencia = {}

        # Una sola llamada a crear_widgets
        self.crear_widgets()
        # No se llama a cargar_todas_las_preguntas ni iniciar_temporizador aquí,
        # lo hará iniciar_quiz_data cuando MainApp lo muestre.

    def iniciar_quiz_data(self, preguntas, tiempo_limite, quiz_filename):
        """
        Método para inicializar los datos del quiz y empezar el temporizador.
        Llamado por MainApp cuando se muestra QuizScreen.
        """
        self.preguntas = preguntas[:] 
        random.shuffle(self.preguntas)

        self.tiempo_limite = tiempo_limite
        self.tiempo_restante = tiempo_limite
        self.quiz_filename = quiz_filename

        self.has_finished = False 
        self.boton_enviar.config(state=tk.NORMAL) 

        # Limpiar preguntas anteriores y crear nuevas
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.opciones_seleccionadas_vars = {} 
        self.checkbuttons_referencia = {}

        self.cargar_todas_las_preguntas()

        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        
        self.start_time = None 
        self.timer_label.config(fg="black") 

        if self.tiempo_limite is not None:
            self.iniciar_temporizador_descendente()
        else:
            self.iniciar_temporizador_ascendente()
        
        # Asegúrate de ocultar el botón de volver al inicio al empezar un nuevo quiz
        self.boton_volver_inicio.pack_forget()


    def crear_widgets(self):
        self.top_frame = tk.Frame(self, bg="#e0e0e0", padx=10, pady=5)
        self.top_frame.pack(side="top", fill="x")
        self.timer_label = tk.Label(self.top_frame, text="", font=("Arial", 14, "bold"), bg="#e0e0e0")
        self.timer_label.pack(side="left", padx=10)
        self.boton_enviar = tk.Button(self.top_frame, text="Enviar Respuestas", command=self.procesar_respuestas, font=("Arial", 12))
        self.boton_enviar.pack(side="right", padx=10)

        self.boton_volver_inicio = tk.Button(self.top_frame, text="Volver al Inicio", command=self.volver_a_inicio, font=("Arial", 12))
        # No lo empaquetamos aquí; se empaqueta después de procesar_respuestas

        self.canvas = tk.Canvas(self, borderwidth=0, background="#f0f0f0")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.vsb.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f0f0f0")
        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

    def _on_mouse_wheel(self, event):
        if event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1,"units")
        elif event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1,"units")

    def iniciar_temporizador_descendente(self):
        if self.tiempo_restante is not None:
            self.actualizar_temporizador_descendente()

    def actualizar_temporizador_descendente(self):
        if self.tiempo_restante is not None and self.tiempo_restante >= 0:
            minutos = self.tiempo_restante // 60
            segundos = self.tiempo_restante % 60
            self.timer_label.config(text=f"Tiempo restante: {minutos:02}:{segundos:02}")
            self.tiempo_restante -= 1
            self.timer_id = self.after(1000, self.actualizar_temporizador_descendente) 
        else:
            self.timer_label.config(text="¡Tiempo agotado!", fg="red")
            self.procesar_respuestas(tiempo_agotado=True)

    def iniciar_temporizador_ascendente(self):
        self.start_time = time.time() 
        self.actualizar_temporizador_ascendente()

    def actualizar_temporizador_ascendente(self):
        if not self.has_finished: 
            elapsed_time = int(time.time() - self.start_time)
            minutos = elapsed_time // 60
            segundos = elapsed_time % 60
            self.timer_label.config(text=f"Tiempo transcurrido: {minutos:02}:{segundos:02}")
            self.timer_id = self.after(1000, self.actualizar_temporizador_ascendente)

    def cargar_todas_las_preguntas(self):
        for idx, preg in enumerate(self.preguntas, 1):
            pregunta_container = tk.LabelFrame(self.scrollable_frame,
                                               text=f"Pregunta {idx}",
                                               font=("Arial", 12, "bold"),
                                               padx=15, pady=10,
                                               bg="white", bd=2, relief="groove")
            pregunta_container.pack(fill="x", padx=10, pady=10, expand=True)

            tk.Label(pregunta_container, text=preg["pregunta"],
                     wraplength=600, font=("Arial", 11), anchor="w", justify="left", bg="white").pack(pady=5)

            opciones_vars_de_esta_pregunta = {} 
            opciones_checkbuttons_de_esta_pregunta = {} 

            opciones = preg["respuesta"][:]
            random.shuffle(opciones)

            for j, (texto_opcion, _) in enumerate(opciones):
                letra = chr(65 + j) 

                var_check = tk.BooleanVar() 
                var_check.set(False) 

                opciones_vars_de_esta_pregunta[texto_opcion] = var_check

                cb = tk.Checkbutton(pregunta_container,
                                     text=f"{letra}. {texto_opcion}",
                                     variable=var_check, 
                                     font=("Arial", 10),
                                     anchor="w",
                                     justify="left",
                                     wraplength=550,
                                     bg="white", 
                                     selectcolor="lightgray" 
                                     )
                cb.pack(fill="x", pady=2, padx=10)
                opciones_checkbuttons_de_esta_pregunta[texto_opcion] = cb 

            self.opciones_seleccionadas_vars[idx] = opciones_vars_de_esta_pregunta
            self.checkbuttons_referencia[idx] = opciones_checkbuttons_de_esta_pregunta 

    def procesar_respuestas(self, tiempo_agotado=False):
        if self.has_finished: 
            return
        
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None

        self.boton_enviar.config(state=tk.DISABLED) 
        self.has_finished = True 

        final_time_for_db = None 

        if tiempo_agotado:
            final_time_message = "" 
        else: 
            if self.tiempo_limite is None and self.start_time is not None:
                final_elapsed_time = int(time.time() - self.start_time)
                min_final = final_elapsed_time // 60
                seg_final = final_elapsed_time % 60
                final_time_message = f"Tu tiempo: {min_final:02}:{seg_final:02}\n"
                final_time_for_db = final_elapsed_time 
            else:
                final_time_message = "" 

        correctas_count = 0

        for idx_pregunta_mostrada, opciones_vars_de_esta_pregunta in self.opciones_seleccionadas_vars.items():
            pregunta_original_data = self.preguntas[idx_pregunta_mostrada - 1]

            respuestas_correctas_reales = []
            for opcion_texto_original, es_correcta in pregunta_original_data["respuesta"]:
                if es_correcta:
                    respuestas_correctas_reales.append(opcion_texto_original)

            checkbuttons_de_esta_pregunta = self.checkbuttons_referencia[idx_pregunta_mostrada]

            todas_las_correctas_marcadas = True
            incorrectas_marcadas_por_usuario = 0
            correctas_marcadas_por_usuario = 0

            for opcion_texto_mostrada in opciones_vars_de_esta_pregunta.keys():

                checkbutton = checkbuttons_de_esta_pregunta[opcion_texto_mostrada]
                checkbutton.config(state=tk.DISABLED)

                es_correcta_real = (opcion_texto_mostrada in respuestas_correctas_reales)
                fue_marcada_por_usuario = opciones_vars_de_esta_pregunta[opcion_texto_mostrada].get()

                if es_correcta_real and fue_marcada_por_usuario:
                    checkbutton.config(bg="lightgreen", fg="black") 
                    correctas_marcadas_por_usuario += 1
                elif es_correcta_real and not fue_marcada_por_usuario:
                    checkbutton.config(bg="lightgreen", fg="darkgreen") 
                    todas_las_correctas_marcadas = False
                elif not es_correcta_real and fue_marcada_por_usuario:
                    checkbutton.config(bg="red", fg="white")
                    incorrectas_marcadas_por_usuario += 1
                    todas_las_correctas_marcadas = False 
                else: 
                    checkbutton.config(bg="lightgray", fg="gray")

            if todas_las_correctas_marcadas and \
               (incorrectas_marcadas_por_usuario == 0) and \
               (correctas_marcadas_por_usuario == len(respuestas_correctas_reales)):
                correctas_count += 1

        mensaje_final = ""
        if tiempo_agotado:
            mensaje_final = "¡Tiempo agotado!\n"
        
        mensaje_final += final_time_message 
        mensaje_final += f"Has respondido {correctas_count} de {len(self.preguntas)} preguntas correctamente."
        
        messagebox.showinfo("Quiz Finalizado", mensaje_final)

        if self.db: 
            display_filename = os.path.basename(self.quiz_filename)
            self.db.save_attempt(
                quiz_filename=display_filename,
                correct_answers=correctas_count,
                total_questions=len(self.preguntas),
                time_taken_seconds=final_time_for_db 
            )

        self.boton_volver_inicio.pack(side="right", padx=10) 
        self.timer_label.config(fg="black") 

    def volver_a_inicio(self):
        self.app.show_frame("InicioScreen")