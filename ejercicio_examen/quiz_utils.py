import tkinter as tk
from tkinter import messagebox

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
    except Exception as e: # Captura otros posibles errores durante la lectura del archivo
        messagebox.showerror("Error de Archivo", f"Ocurrió un error al leer el archivo '{nombre_archivo}': {e}")
    return preguntas