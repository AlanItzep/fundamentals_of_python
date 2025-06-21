import sqlite3
import os
from datetime import datetime

class QuizDatabase:
    def __init__(self, db_name="quiz_stats.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._connect()
        self._create_table()

    def _connect(self):
        """Establece la conexión con la base de datos."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"Conectado a la base de datos: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            # Puedes añadir un messagebox aquí si quieres notificar al usuario
            # import tkinter as tk
            # from tkinter import messagebox
            # messagebox.showerror("Error de Base de Datos", f"No se pudo conectar a la base de datos: {e}")

    def _create_table(self):
        """Crea la tabla 'attempts' si no existe."""
        if not self.conn:
            print("No hay conexión a la base de datos para crear la tabla.")
            return

        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS attempts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    quiz_filename TEXT NOT NULL,
                    correct_answers INTEGER NOT NULL,
                    total_questions INTEGER NOT NULL,
                    time_taken_seconds INTEGER, -- Null si no aplica (ej. con temporizador límite agotado)
                    timestamp TEXT NOT NULL
                )
            """)
            self.conn.commit()
            print("Tabla 'attempts' verificada/creada exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    def save_attempt(self, quiz_filename, correct_answers, total_questions, time_taken_seconds=None):
        """
        Guarda un nuevo intento de quiz en la base de datos.
        :param quiz_filename: Nombre del archivo del quiz jugado (ej. 'questions.txt').
        :param correct_answers: Número de respuestas correctas.
        :param total_questions: Número total de preguntas.
        :param time_taken_seconds: Tiempo que tardó el usuario en segundos (opcional, si se usó temporizador ascendente).
        """
        if not self.conn:
            print("No hay conexión a la base de datos para guardar el intento.")
            return False

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.cursor.execute(
                "INSERT INTO attempts (quiz_filename, correct_answers, total_questions, time_taken_seconds, timestamp) VALUES (?, ?, ?, ?, ?)",
                (quiz_filename, correct_answers, total_questions, time_taken_seconds, timestamp)
            )
            self.conn.commit()
            print(f"Intento guardado: {quiz_filename}, Correctas: {correct_answers}/{total_questions}, Tiempo: {time_taken_seconds}s")
            return True
        except sqlite3.Error as e:
            print(f"Error al guardar el intento: {e}")
            return False

    def get_all_attempts(self):
        """Recupera todos los intentos guardados."""
        if not self.conn:
            print("No hay conexión a la base de datos para recuperar los intentos.")
            return []
        try:
            self.cursor.execute("SELECT * FROM attempts ORDER BY timestamp DESC")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener intentos: {e}")
            return []

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
            print("Conexión a la base de datos cerrada.")

# Ejemplo de uso (opcional, puedes borrarlo después de probar)
if __name__ == "__main__":
    db = QuizDatabase()

    # Guardar algunos intentos de ejemplo
    db.save_attempt("quiz_matematicas.txt", 8, 10, 150)
    db.save_attempt("quiz_historia.txt", 6, 8, None) # Sin tiempo si se agotó el límite
    db.save_attempt("quiz_matematicas.txt", 9, 10, 120)

    # Obtener y mostrar todos los intentos
    print("\nTodos los intentos:")
    for attempt in db.get_all_attempts():
        print(attempt)

    db.close()

    # Puedes eliminar el archivo de base de datos para empezar de nuevo
    # if os.path.exists("quiz_stats.db"):
    #     os.remove("quiz_stats.db")
    #     print("Base de datos eliminada.")