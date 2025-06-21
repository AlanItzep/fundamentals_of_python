# Mi Juego de Preguntas (Quiz App)

## Tabla de Contenidos
* [Características Principales](#características-principales)
* [Cómo Utilizar y Crear tus Propios Cuestionarios](#cómo-utilizar-y-crear-tus-propios-cuestionarios)
    * [1. Formato del Archivo de Cuestionario (.txt)](#1-formato-del-archivo-de-cuestionario-txt)
    * [2. Preparación y Ejecución del Programa](#2-preparación-y-ejecución-del-programa)
    * [3. Funcionalidad de las Ventanas](#3-funcionalidad-de-las-ventanas)
        * [A. Pantalla de Inicio (InicioScreen)](#a-pantalla-de-inicio-inicioscreen)
        * [B. Pantalla del Quiz (QuizScreen)](#b-pantalla-del-quiz-quizscreen)
        * [C. Pantalla de Estadísticas (StatsScreen)](#c-pantalla-de-estadísticas-statsscreen)
* [Funcionamiento Interno (Detrás de Escena)](#funcionamiento-interno-detrás-de-escena)
    * [1. Estructura de la Aplicación](#1-estructura-de-la-aplicación)
    * [2. Carga y Mezcla de Preguntas/Respuestas](#2-carga-y-mezcla-de-preguntasrespuestas)
    * [3. Gestión de la Base de Datos](#3-gestión-de-la-base-de-datos)

---

Esta es una aplicación de escritorio simple pero funcional desarrollada en Python utilizando Tkinter para la interfaz gráfica. Permite a los usuarios realizar cuestionarios personalizados, guardar sus resultados y visualizar estadísticas de rendimiento.

## Características Principales

* **Cuestionarios Personalizables:** Crea tus propios archivos de preguntas en formato `.txt`.
* **Temporizador Flexible:** Elige si quieres un temporizador con cuenta atrás o un contador de tiempo ascendente.
* **Estadísticas Detalladas:** Visualiza tus intentos de quiz en una tabla y un gráfico de rendimiento.
* **Persistencia de Datos:** Los resultados de tus quizzes se guardan en una base de datos SQLite local.

## Cómo Utilizar y Crear tus Propios Cuestionarios

### 1. Formato del Archivo de Cuestionario (`.txt`)

La aplicación carga las preguntas de archivos de texto simple (`.txt`). Es crucial que el formato de estos archivos se siga estrictamente para que la aplicación pueda interpretar correctamente las preguntas y sus respuestas.

Cada pregunta debe seguir el siguiente patrón:

[Número de Pregunta] - [Texto de la Pregunta]

[Opción 1], [TRUE/FALSE]

[Opción 2], [TRUE/FALSE]

[Opción 3], [TRUE/FALSE]

[Opción 4], [TRUE/FALSE]



**Puntos Clave del Formato:**

* **Pregunta:**
    * Debe comenzar con un número, seguido de un espacio, un guion (`-`), otro espacio y luego el texto de la pregunta.
    * Ejemplo: `1 - ¿Cuál es la capital de España?`
* **Respuestas:**
    * Cada pregunta debe tener **exactamente cuatro opciones de respuesta**.
    * Cada opción debe estar en una nueva línea.
    * El texto de la opción y su indicador de corrección (`TRUE` o `FALSE`) deben estar separados por una coma `,`.
    * El indicador de corrección (`TRUE` o `FALSE`) no distingue entre mayúsculas y minúsculas (ej. `true`, `True`, `TRUE` son válidos).
    * Debe haber al menos una respuesta marcada como `TRUE` para que la pregunta sea válida.

**Ejemplo de un archivo `questions.txt` válido:**

    1 - ¿Cuál es la capital de Francia?

    París, TRUE

    Madrid, FALSE

    Londres, FALSE

    Roma, FALSE

    2 - ¿Qué planeta es conocido como el Planeta Rojo?

    Venus, FALSE

    Marte, TRUE

    Júpiter, FALSE

    Saturno, FALSE

    3 - ¿Qué lenguaje de programación se utiliza para desarrollar esta aplicación?

    Java, FALSE

    C++, FALSE

    Python, TRUE

    JavaScript, FALSE


### 2. Preparación y Ejecución del Programa

**IMPORTANTE: Ejecuta el programa desde la línea de comandos en el directorio correcto.**

Para un funcionamiento óptimo y para asegurar que la aplicación pueda encontrar tus archivos de cuestionario y crear su base de datos de estadísticas, es **fundamental** ejecutar el script `cuestionario.py` desde la línea de comandos, asegurándote de que tu terminal esté en el mismo directorio donde se encuentra `cuestionario.py` y tus archivos `.txt` de cuestionario.

**Pasos:**

1.  Abre tu terminal o línea de comandos (CMD, PowerShell, Git Bash, etc.).
2.  Navega hasta el directorio donde has guardado `cuestionario.py` y tus archivos de cuestionario (`.txt`).
    * Ejemplo (Windows): `cd C:\Users\TuUsuario\Documents\MiProyectoQuiz`
    * Ejemplo (Linux/macOS): `cd /home/TuUsuario/MiProyectoQuiz`
3.  Ejecuta el programa:
    ```bash
    python cuestionario.py
    ```

**Razones para esta recomendación:**

* **Reconocimiento de Archivos de Cuestionario:** Al ejecutar desde el directorio, la aplicación puede encontrar fácilmente el archivo `questions.txt` (por defecto) o cualquier otro archivo `.txt` que selecciones usando el explorador de archivos.
* **Creación de la Base de Datos:** La base de datos de estadísticas (`quiz_stats.db`) se creará automáticamente en el mismo directorio desde el que ejecutas el programa, manteniéndolo organizado.

### 3. Funcionalidad de las Ventanas

#### A. Pantalla de Inicio (`InicioScreen`)

* **Seleccionar Archivo de Quiz:** Haz clic en "Seleccionar Archivo de Quiz" para elegir un archivo `.txt` de tu sistema. Por defecto, si no seleccionas uno, la aplicación intentará cargar `questions.txt` del mismo directorio.
* **Usar Temporizador:** Marca esta casilla para habilitar un temporizador para el quiz.
    * Si está marcada, introduce la cantidad de minutos deseada en el campo de texto.
    * Si no está marcada, el quiz registrará el tiempo que tardas en completarlo (temporizador ascendente) en lugar de un límite.
* **Iniciar Quiz:** Comienza el cuestionario con las preguntas del archivo seleccionado y la configuración del temporizador.
* **Ver Estadísticas:** Accede a la pantalla de estadísticas para revisar tu rendimiento.

#### B. Pantalla del Quiz (`QuizScreen`)

* **Preguntas y Opciones:** Las preguntas se muestran una por una, con sus opciones de respuesta (aleatoriamente mezcladas).
* **Selección Múltiple (implícita):** Aunque se usan `Checkbutton`s, la lógica del programa asume que solo una opción es correcta por pregunta si el archivo `.txt` está bien formateado con un solo `TRUE`. Si múltiples `TRUE`s se marcaran en el `.txt`, la validación podría necesitar ajustes finos para ese caso.
* **Temporizador:**
    * Si configuraste un tiempo límite, el contador regresará. Al llegar a cero, el quiz terminará automáticamente.
    * Si no configuraste un tiempo límite, un contador ascendente mostrará cuánto tiempo llevas respondiendo.
* **Enviar Respuestas:** Haz clic en este botón para finalizar el quiz y ver tus resultados. Este botón se desactiva una vez que se procesan las respuestas o se agota el tiempo.
* **Volver al Inicio:** Este botón aparece una vez que el quiz ha finalizado, permitiéndote regresar a la pantalla principal.

#### C. Pantalla de Estadísticas (`StatsScreen`)

* **Tabla de Intentos:** Muestra un registro de todos los quizzes que has realizado, incluyendo:
    * ID de Intento
    * Nombre del Archivo del Quiz
    * Respuestas Correctas (X/Y)
    * Total de Preguntas
    * Tiempo Tomado (mm:ss o N/A si el tiempo se agotó o no aplicaba)
    * Fecha y Hora del Intento
* **Gráfico de Rendimiento:** Un gráfico de barras visualiza el porcentaje de respuestas correctas para cada intento de quiz, facilitando el seguimiento de tu progreso.
* **Botones de Navegación del Gráfico:** Matplotlib proporciona una barra de herramientas en el gráfico para hacer zoom, moverlo, guardarlo como imagen, etc.
* **Volver al Inicio:** Regresa a la pantalla principal de configuración del quiz.

## Funcionamiento Interno (Detrás de Escena)

### 1. Estructura de la Aplicación

La aplicación sigue un patrón Model-View-Controller (MVC) simplificado:

* **`cuestionario.py` (Controlador Principal):** Contiene la clase `MainApp` que actúa como el controlador principal. Gestiona la navegación entre las diferentes pantallas (`InicioScreen`, `QuizScreen`, `StatsScreen`) y las inicializa. También maneja el ciclo de vida de la aplicación y la conexión con la base de datos.
* **`quiz_screens.py` (Vistas):** Contiene las clases `InicioScreen`, `QuizScreen` y `StatsScreen`, que son subclases de `tk.Frame`. Estas clases son responsables de la interfaz de usuario de cada pantalla y de interactuar con el controlador principal (`MainApp`) y la base de datos.
* **`quiz_utils.py` (Modelo/Utilidades):** Contiene funciones auxiliares, como `cargar_preguntas`, que se encarga de leer y parsear los archivos `.txt` de cuestionarios.
* **`quiz_database.py` (Modelo/Base de Datos):** Contiene la clase `QuizDatabase` que se encarga de todas las operaciones relacionadas con la base de datos SQLite (conexión, creación de tabla, guardar intentos, recuperar intentos).

### 2. Carga y Mezcla de Preguntas/Respuestas

1.  Cuando seleccionas un archivo `.txt` y haces clic en "Iniciar Quiz", la función `cargar_preguntas` de `quiz_utils.py` lee el archivo línea por línea.
2.  Parsea cada pregunta y sus cuatro opciones, identificando cuál es la correcta basándose en el indicador `TRUE`/`FALSE`.
3.  Una vez cargadas todas las preguntas en una lista de diccionarios, la aplicación `random.shuffle()` la lista de preguntas para que aparezcan en un orden aleatorio en cada intento de quiz.
4.  Dentro de cada pregunta, las opciones de respuesta también se mezclan aleatoriamente (`random.shuffle()`) antes de ser mostradas al usuario, asegurando que el orden de las respuestas no sea siempre el mismo.

### 3. Gestión de la Base de Datos

* Al iniciar la aplicación, se crea una instancia de `QuizDatabase`, que establece una conexión con el archivo `quiz_stats.db` (o lo crea si no existe) y asegura que la tabla `attempts` esté configurada.
* Después de cada quiz completado (o si el tiempo se agota), la clase `QuizScreen` llama al método `save_attempt()` de la instancia de `QuizDatabase` para registrar el resultado (nombre del archivo del quiz, número de respuestas correctas, total de preguntas y tiempo tomado).
* La pantalla de estadísticas (`StatsScreen`) recupera todos los intentos guardados de la base de dat