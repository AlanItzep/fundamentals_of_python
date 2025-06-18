import tkinter as tk
from tkinter import messagebox, filedialog # Importa filedialog
import random
import time
from quiz_utils import cargar_preguntas # Importa la función de utilidad

class InicioScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)

        # Nuevo: tk.StringVar para guardar y mostrar la ruta del archivo seleccionado
        self.selected_file_path = tk.StringVar(value="No se ha seleccionado archivo") 
        self.quiz_filename = "questions.txt" # Nombre de archivo por defecto

        self.crear_widgets()

    # ... (el resto del código de InicioScreen, incluyendo toggle_tiempo_input y iniciar_quiz)
    def crear_widgets(self):
        tk.Label(self, text="Configuración del Quiz", font=("Arial", 16, "bold")).pack(pady=20)

        # Sección de selección de archivo
        tk.Label(self, text="Archivo del Quiz:", font=("Arial", 12)).pack(pady=(10, 0))
        # Etiqueta para mostrar la ruta del archivo seleccionado
        tk.Label(self, textvariable=self.selected_file_path, font=("Arial", 10), fg="blue").pack(pady=(0, 10))
        tk.Button(self, text="Seleccionar Archivo de Quiz", command=self.seleccionar_archivo_quiz, font=("Arial", 10)).pack(pady=5)
        
        # Texto por defecto para la ruta del archivo si no se selecciona explícitamente ninguno
        self.selected_file_path.set(f"Usando por defecto: {self.quiz_filename}")

        # Separador para mayor claridad
        tk.Frame(self, height=2, bd=1, relief=tk.SUNKEN).pack(fill="x", padx=20, pady=10)

        # Opciones de temporizador existentes
        self.usar_temporizador_var = tk.BooleanVar(value=False)
        tk.Checkbutton(self, text="Usar Temporizador", variable=self.usar_temporizador_var, 
                       command=self.toggle_tiempo_input, font=("Arial", 12)).pack(pady=5)
        tk.Label(self, text="Tiempo límite (minutos):", font=("Arial", 12)).pack(pady=5)
        self.tiempo_entrada = tk.Entry(self, width=10, font=("Arial", 12))
        self.tiempo_entrada.insert(0, "2") # Valor por defecto: 2 minutos (antes era 120 segundos)
        self.tiempo_entrada.pack(pady=5)

        tk.Button(self, text="Iniciar Quiz", command=self.iniciar_quiz, font=("Arial", 14, "bold")).pack(pady=20)

        self.toggle_tiempo_input()
    
    def seleccionar_archivo_quiz(self):
        # Abre un cuadro de diálogo de selección de archivo para que el usuario elija un archivo .txt
        file_path = filedialog.askopenfilename(
            title="Selecciona un archivo de preguntas",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if file_path: # Si se seleccionó un archivo
            self.quiz_filename = file_path
            # Actualiza la ruta de archivo mostrada (solo muestra el nombre del archivo para abreviar)
            self.selected_file_path.set(f"Archivo seleccionado: {self.quiz_filename.split('/')[-1]}") 
        else:
            # Si no se selecciona ningún archivo, vuelve al por defecto o informa al usuario
            self.selected_file_path.set(f"Usando por defecto: {self.quiz_filename.split('/')[-1]}") # Sigue mostrando el por defecto si el usuario cancela
            self.quiz_filename = "questions.txt" # Asegúrate de que el por defecto esté activo si se cancela el diálogo

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
                tiempo_limite = tiempo_en_minutos * 60 # Convertir a segundos para el temporizador
            except ValueError:
                messagebox.showerror("Error de Tiempo", "Por favor, introduce un número válido para los minutos del tiempo límite.")
                return
        
        # Pasa el nombre del archivo seleccionado a cargar_preguntas
        preguntas_cargadas = cargar_preguntas(self.quiz_filename) 
        if not preguntas_cargadas:
            return

        self.destroy() 
        # Aquí pasamos la referencia al objeto 'master' (la ventana principal)
        # para que QuizScreen pueda llamarla al querer volver.
        QuizScreen(self.master, preguntas_cargadas, tiempo_limite)


class QuizScreen(tk.Frame):
    def __init__(self, master, preguntas, tiempo_limite=None):
        super().__init__(master)
        self.master = master
        self.preguntas = preguntas
        self.tiempo_limite = tiempo_limite
        self.tiempo_restante = tiempo_limite
        self.timer_id = None
        self.has_finished = False # Nuevo: banderín para saber si el quiz ha terminado


        self.opciones_seleccionadas_vars = {} 
        self.checkbuttons_referencia = {}

        self.pack(fill="both", expand=True)
        self.crear_widgets()
        self.cargar_todas_las_preguntas()

        if self.tiempo_limite is not None:
            self.iniciar_temporizador()

    # ... (el resto del código de QuizScreen, incluyendo crear_widgets, _on_mouse_wheel, 
    #      iniciar_temporizador, actualizar_temporizador, cargar_todas_las_preguntas, 
    #      y procesar_respuestas)
    def crear_widgets(self):
        self.top_frame = tk.Frame(self, bg="#e0e0e0", padx=10, pady=5)
        self.top_frame.pack(side="top", fill="x")
        self.timer_label = tk.Label(self.top_frame, text="", font=("Arial", 14, "bold"), bg="#e0e0e0")
        self.timer_label.pack(side="left", padx=10)
        self.boton_enviar = tk.Button(self.top_frame, text="Enviar Respuestas", command=self.procesar_respuestas, font=("Arial", 12))
        self.boton_enviar.pack(side="right", padx=10)

        # ¡NUEVO! Botón para volver a la pantalla inicial (inicialmente oculto o deshabilitado)
        self.boton_volver_inicio = tk.Button(self.top_frame, text="Volver al Inicio", command=self.volver_a_inicio, font=("Arial", 12))
        # No lo empaquetamos aquí; lo haremos visible después de procesar_respuestas

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

    def iniciar_temporizador(self):
        if self.tiempo_restante is not None:
            self.actualizar_temporizador()

    def actualizar_temporizador(self):
        if self.tiempo_restante is not None and self.tiempo_restante >= 0:
            minutos = self.tiempo_restante // 60
            segundos = self.tiempo_restante % 60
            self.timer_label.config(text=f"Tiempo restante: {minutos:02}:{segundos:02}")
            self.tiempo_restante -= 1
            self.timer_id = self.after(1000, self.actualizar_temporizador)
        else:
            self.timer_label.config(text="¡Tiempo agotado!", fg="red")
            self.procesar_respuestas(tiempo_agotado=True)

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
        if self.has_finished: # Evita procesar dos veces si ya se terminó el quiz
            return
        
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None

        self.boton_enviar.config(state=tk.DISABLED) # Deshabilita el botón de enviar
        self.has_finished = True # Marca el quiz como terminado

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
        mensaje_final += f"Has respondido {correctas_count} de {len(self.preguntas)} preguntas correctamente."

        messagebox.showinfo("Quiz Finalizado", mensaje_final)

        # ¡NUEVO! Mostrar el botón "Volver al Inicio" una vez que el quiz ha terminado
        self.boton_volver_inicio.pack(side="right", padx=10)

    def volver_a_inicio(self):
        """Destruye la QuizScreen actual y vuelve a crear la InicioScreen."""
        self.destroy() # Destruye este frame (QuizScreen)
        # Recrea la pantalla de inicio usando la ventana principal (master)
        # La referencia a master se pasa desde MainApp a InicioScreen, y de InicioScreen a QuizScreen
        from quiz_screens import InicioScreen # Importa de nuevo para asegurar
        InicioScreen(self.master) # Recrea la pantalla inicial