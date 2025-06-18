# para saber desde que ruta se esta ejecutando
"""
import os
print("Directorio actual:", os.getcwd())
"""
import tkinter as tk
from tkinter import messagebox
import random

# --- 1. Lógica para cargar las preguntas (SIN CAMBIOS) ---
def cargar_preguntas(nombre_archivo="questions.txt"):
    preguntas = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            i = 0
            while i < len(lineas):
                linea = lineas[i].strip()
                if " -" in linea:
                    partes = linea.split(" -", 1)
                    if partes[0].isdigit():
                        texto_pregunta = partes[1].strip()

                        respuestas = []
                        for j in range(1, 5):
                            if (i + j) < len(lineas):
                                try:
                                    texto_resp, valor = lineas[i + j].rsplit(",", 1)
                                    respuestas.append((texto_resp.strip(), valor.strip().upper() == "TRUE"))
                                except ValueError:
                                    print(f"Advertencia: Formato de respuesta incorrecto en linea {i+j+1}. Omitiendo pregunta.") 
                                    respuestas = []
                                    break
                            else:
                                print(f"Advertencia: El formato del archivo es incorrecto cerca de la pregunta en la linea {i + 1}. Faltan respuestas.")
                                respuestas = []
                                break
                        
                        if len(respuestas) == 4:
                            preguntas.append({
                                "pregunta": texto_pregunta,
                                "respuesta": respuestas
                            })
                        else:
                            print(f"Pregunta omitida por formato incorrecto o respuestas insuficientes: {texto_pregunta}")
                        
                        i += 5 
                else:
                    i += 1
    except FileNotFoundError:
        messagebox.showerror("Error de Archivo", f"El archivo '{nombre_archivo}' no fue encontrado")
    return preguntas

# --- 2. Lógica de la GUI con Tkinter (ADAPTADA PARA CHECKBUTTONS) ---
class QuizApp:
    def __init__(self, master):
        self.master = master
        master.title("Mi Juego de Preguntas (Múltiples Opciones)")
        master.geometry("800x600")

        self.preguntas = cargar_preguntas()
        if not self.preguntas:
            messagebox.showerror("Error","No se pudieron cargar preguntas. Revisa el fichero .txt.")
            master.destroy() 
            return
        
        random.shuffle(self.preguntas) 
        
        # Almacenará {id_pregunta: {texto_opcion: tk.BooleanVar}}
        # Esto nos permite saber el estado de cada Checkbutton
        self.opciones_seleccionadas_vars = {} 

        self.crear_widgets()
        self.cargar_todas_las_preguntas()


    def crear_widgets(self):
        self.canvas = tk.Canvas(self.master, borderwidth=0, background="#f0f0f0")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.vsb = tk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        self.vsb.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.scrollable_frame = tk.Frame(self.canvas, bg="#f0f0f0")

        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
        
        self.boton_enviar = tk.Button(self.master, text="Enviar Respuestas", command=self.procesar_respuestas, font=("Arial", 12))
        self.boton_enviar.pack(pady=10)

    def _on_mouse_wheel(self, event):
        if event.num == 5 or event.delta == -120: # Windows
            self.canvas.yview_scroll(1,"units")
        elif event.num == 4 or event.delta == 120: # Linux/macOS
            self.canvas.yview_scroll(-1,"units")

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
            
            # Inicializamos un diccionario para las variables de los Checkbuttons de esta pregunta
            # Esto es clave para las múltiples selecciones
            opciones_vars_de_esta_pregunta = {} 
            
            opciones = preg["respuesta"][:]
            random.shuffle(opciones)

            for j, (texto_opcion, _) in enumerate(opciones):
                letra = chr(65 + j) # A, B, C, D
                
                # CADA CHECKBUTTON TIENE SU PROPIA tk.BooleanVar
                var_check = tk.BooleanVar() 
                var_check.set(False) # Inicia desmarcado (vacío)
                
                # Almacenamos la variable booleana, usando el texto de la opción como clave
                opciones_vars_de_esta_pregunta[texto_opcion] = var_check

                cb = tk.Checkbutton(pregunta_container,
                                     text=f"{letra}. {texto_opcion}",
                                     variable=var_check, # Conectamos el Checkbutton a su BooleanVar
                                     font=("Arial", 10),
                                     anchor="w",
                                     justify="left",
                                     wraplength=550,
                                     bg="white"
                                     )
                cb.pack(fill="x", pady=2, padx=10)
            
            # Guardamos el diccionario de variables de esta pregunta por su índice
            self.opciones_seleccionadas_vars[idx] = opciones_vars_de_esta_pregunta
    
    def procesar_respuestas(self):
        resultados_finales = {} # Para almacenar el resumen final
        correctas_count = 0

        # Iterar sobre cada pregunta en el orden original de self.preguntas (idx-1)
        # o en el orden que se mostraron (idx de self.opciones_seleccionadas_vars)
        for idx_pregunta_mostrada, opciones_vars_de_esta_pregunta in self.opciones_seleccionadas_vars.items():
            pregunta_original_data = self.preguntas[idx_pregunta_mostrada - 1] # Asume que el idx de la pregunta en la GUI coincide con idx-1 en self.preguntas
            pregunta_texto = pregunta_original_data["pregunta"]
            
            respuestas_usuario_para_esta_pregunta = []
            for opcion_texto, var_check in opciones_vars_de_esta_pregunta.items():
                if var_check.get(): # Si el Checkbutton está marcado
                    respuestas_usuario_para_esta_pregunta.append(opcion_texto)
            
            respuestas_correctas_reales = []
            for opcion_texto_original, es_correcta in pregunta_original_data["respuesta"]:
                if es_correcta:
                    respuestas_correctas_reales.append(opcion_texto_original)

            # Para verificar si es correcta, comparamos las listas de respuestas
            # Importa el orden para la comparación? Si no, se pueden ordenar las listas
            # para una comparación consistente. Aquí asumimos que el orden no importa para la verificación.
            es_correcta_total = sorted(respuestas_usuario_para_esta_pregunta) == sorted(respuestas_correctas_reales)
            
            resultados_finales[pregunta_texto] = {
                "seleccionado": ", ".join(respuestas_usuario_para_esta_pregunta) if respuestas_usuario_para_esta_pregunta else "No respondida",
                "correctas": ", ".join(respuestas_correctas_reales),
                "resultado": "Correcta" if es_correcta_total else "Incorrecta"
            }
            if es_correcta_total:
                correctas_count += 1
        
        # Mostrar resumen
        resumen_texto = "Resultados del Quiz:\n\n"
        for preg_txt, res in resultados_finales.items():
            resumen_texto += f"Pregunta: {preg_txt}\n"
            resumen_texto += f"Tu(s) respuesta(s): {res['seleccionado']}\n"
            resumen_texto += f"Respuesta(s) correcta(s): {res['correctas']}\n"
            resumen_texto += f"Resultado: {res['resultado']}\n\n"
        
        resumen_texto += f"¡Has respondido {correctas_count} de {len(self.preguntas)} preguntas correctamente!"

        messagebox.showinfo("Resultados del Quiz", resumen_texto)

# --- Ejecutar la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

"""
pregunta = random.choice(preguntas)
respuestas = pregunta["respuesta"][:]
random.shuffle(respuestas)
print(pregunta["pregunta"])
for i, (texto, _) in enumerate(respuestas, 1):
    print(f"{i}. {texto}")
"""