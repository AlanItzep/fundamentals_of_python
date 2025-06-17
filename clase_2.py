"""
Questions 
1. Which of the following are valid Python variable names?
"""
#my_var = 1 --> si
#3value = 5
#value3 = 8 --> si
#my-var = 9

"""
2. Which of the following expressions return the boolean value True?
"""
#x = bool("false") --> True
#bool(0.0)
#3 < 5 and 2 != 4 --> True
#not (5 == 5 and False) --> True
"""
3. Which expressions evaluate to True?
"""
# print( 3 != 5) --> True
# print( 4 < 4 )
# print( 7 <= 7 ) --> True
# print( 9 == 10 )
"""
4. Which of the following are Python keywords?
"""
# def >> Keyboard
# True >> Keyboard
# value
# return >> Keyboard
"""
5. Which statements are correct about the print() function?
"""
# It can print multiple values. (check)
# It returns the printed value. >> No, print() no devuelve nada útil, solo muestra en pantalla. Su valor de retorno es None.
# It can be called without arguments. (check) >> Sí, si llamas a print() sin nada dentro, solo imprime una línea en blanco.
# It creates variables.
"""
6. Which of the following function calls are valid?
"""
# len("abc") >> valid
# int("42.5")
# str(True) >> valid
# abs(-3.5) >> valid
"""
7. What are valid results of the expression round(2.756, 2)?
"""
# 2.75
# 2.76 >> correct
# 2.8
# 3.0
"""
8. Which operations are valid on two strings?
"""
# "hi" + "there" >> Valid
# "hi" * 3 >> Valid
# "hi" - "i" >> 
# "hi" / "i" >> 
"""
9. What are possible outputs of type(3)?
"""
# <class 'int'> >> correct
# <type 'int'>
# int
# <class 'float'>

"""
10. What can be true about floating-point comparisons?
"""
# 0.1 + 0.2 == 0.3 may be False >> correct
# abs(a - b) < epsilon is a safe test >> correct
# float values are always exact
# Equality with floats is reliable for all cases

"""
11. Which of the following are boolean expressions?
"""
# 4 < 5 >> boolean
# "a" == "b" >> boolean
# not True >> boolean
# 5 + 2

"""
12. Which statements about logical operators are correct?
"""
# and returns True if both parts are true >> correct: Solo es True si las dos condiciones son True.
# or returns False if both are false >> correct: Basta con que una sea True para que todo sea True.
# not inverts the truth value >> correct: Convierte True en False, y viceversa.
# and means “either this or that” >> 	Esa descripción corresponde a or, no a and.

"""
13. Which expressions evaluate to False?
"""
# 5 < 3 >> Falso
# not True >> Falso
# 4 == 4 
# True and False >> Falso

"""
14. What are valid uses of the if statement?
"""
# if x > 0: >> valid
# if x == y then:
# if (x < 10): >> valid
# if x >= 3: print(x) >> valid

"""
15. What blocks require indentation in Python?
"""
# if >> requires
# def >> requires
# for >> requires
# print

"""
16. Which of the following define functions correctly?
"""
# def greet(name): >> correct
# function greet(): >> function no se usa en Python.
# def add(x, y): return x + y >> correct
# def(x): return x * x >> Falta el nombre de la función.

"""
17. What are true about the return statement?
"""
# It sends a result back to the caller >> correcto
# It ends function execution >> correcto
# A function can return multiple values >> correcto
# It is optional in all functions >> Solo es opcional si no necesitas devolver nada.

"""
18. Which are examples of chained conditionals?
"""
# if x < 0: ... elif x == 0: ... else: ... >> correcto
# if x < 0 or x == 0 or x > 0: >> Es un solo if con operadores lógicos.
# if x < 10: >> Solo un if, sin elif o else.
# elif x > 10: >> No puede haber elif sin un if anterior.

"""
19. What are correct uses of pass?
"""
# As a placeholder when a block is required >> correcto: se usa como marcador de posición cuando el bloque de código es obligatorio pero no quieres escribir nada aún.
# To skip a line of code >> incorrecto: no salta líneas, simplemente no hace nada. Si quieres saltarte algo, puedes usar continue o return.
# To silence syntax errors >> incorrecto: no arregla errores de sintaxis. Solo evita errores cuando se necesita un bloque de código vacío válido.
# To leave an if or else body empty >> correcto: Puedes usar pass en el cuerpo de un if, else, for, etc., cuando no quieras ejecutar ninguna acción.

"""
20. Which of the following expressions use valid multiple comparison?
"""
# if 1 < x <= 10: >> correcta
# if x != 5 != y: >> incorrecta
# if 0 < x and x < 100: >> correcta: Aunque no es una comparación encadenada, es válida y hace lo mismo que 0 < x < 100.
# if x < (y < 10): >> incorrecta: Compara x con un booleano (True o False), lo que suele ser un error.

"""
21. What are correct ternary expressions?
"""
# a if cond else b>> corecto
# if cond then a else b >> incorrrecto: Sintaxis no válida en Python.
# "Yes" if x > 5 else "No" >> correcto
# x ? "yes" : "no" >> incorrecto: Sintaxis de otros lenguajes, no de Python.

"""
22. What can be used in a match-case block?
"""
# match value: >> correcto
# case "hello":>> correcto
# case _:>> correcto
# if case == ...  >> incorrecto: no se usa if de esa forma.

"""
23. What are true about the match-case structure?
"""
# It matches values like a switch >> correcto
# It requires Python 3.10 or newer >> correcto
# case _: acts as “default” >> correcto
# You must use parentheses after match >> incorrecto: La sintaxis no lleva paréntesis.

"""
24. Which values are considered falsy in Python?
"""
# [] (empty list) >> correct
# 0.0 >> correct
# "" >> correct
# "0" >> Cadena con contenido = verdadero

"""
25. What are valid ways to read and convert user input?
"""
# input("Enter: ") >> correct
# int(input("Enter a number: ")) >> correct
# input() >> correct
# float("3.14") >> no usa input

"""
26. What can be used to check the available names in a module?
"""
#dir(math) >> correcto: Lista los nombres definidos en el módulo.
#help(math) >> correcto: Muestra la documentación del módulo.
#list(math) >> incorrecto: no se puede convertir un módulo en lista así.
#math.contents() >> incorrecto: contents() no es una función válida del módulo.

"""
27. Which of the following are expression statements in Python?
"""
# print("Hi") >> correcto
# x + 3 >> correcto
# len("text") >> correcto
# "hello" + "world" >> correcto

"""
28. What are correct statements about local variables?
"""
# They only exist inside the function body >> correcto
# Their names can be the same as global variables >> correcto 
# They are shared across all functions >> incorrecto: Cada función tiene su propio conjunto de variables locales
# They are declared with var keyword >> incorrecto: En Python no existe var; solo se usa la asignación directa

"""
29. What can be used to convert between types?
"""
# int("5") >> correcto
# float("3.14") >> correcto
# str(5.5) >> correcto
# toString(5) >> incorrecto: No es válida en Python

"""
30. What does the following code print?
def example():
    pass

print(example())
"""
# None >> correcto
# 0
# '' >>  No hay retorno de cadena vacía.
# Error