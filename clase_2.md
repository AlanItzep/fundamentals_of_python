## Questions

 1. Which of the following are valid Python variable names?

	 a. **my_var = 1**  --> si 
	 
	 b. si 3value = 5 
	 
	 c. **value3 = 8** --> si 
	 
	 d. my-var = 9
  
2. Which of the following expressions return the boolean value True?  
	  
	  a. **x = bool("false")** --> True
	  
	  b. bool(0.0)
	  
	  c. **3 < 5 and 2 != 4** --> True
	  
	  d. **not (5 == 5 and False)** --> True

3. Which expressions evaluate to True?

	a. **print( 3 != 5)** --> True

	b. print( 4 < 4 )

	c. **print( 7 <= 7 )** --> True

	d. print( 9 == 10 )

4. Which of the following are Python keywords?

	a. **def** >> Keyboard

	b. **True** >> Keyboard

	c. value

	d. **return** >> Keyboard

5. Which statements are correct about the print() function?

	a. **It can print multiple values.** (check)

	b. It returns the printed value. >> No, print() no devuelve nada útil, solo muestra en pantalla. Su valor de retorno es None.

	c. **It can be called without arguments.** (check) >> Sí, si llamas a print() sin nada dentro, solo imprime una línea en blanco.

	d. It creates variables.  

6. Which of the following function calls are valid?

    a. **len("abc")** >> valid

    b. int("42.5")

    c. **str(True)** >> valid

    d. **abs(-3.5)** >> valid

7. What are valid results of the expression round(2.756, 2)?

    a. 2.75

    b. **2.76** >> correct

    c. 2.8

    d. 3.0

8. Which operations are valid on two strings?

    a. **"hi" + "there"** >> Valid

    b. **"hi" * 3** >> Valid

    c. "hi" - "i" >>

    d. "hi" / "i" >>

9. What are possible outputs of type(3)?

    a. **<class 'int'>** >> correct

    b. <type 'int'>

    c. int

    d. <class 'float'>

10. What can be true about floating-point comparisons?

    a.** 0.1 + 0.2 == 0.3 may be False** >> correct

    b. **abs(a - b) < epsilon is a safe test** >> correct

    c. float values are always exact

    d. Equality with floats is reliable for all cases

11. Which of the following are boolean expressions?

    a. **4 < 5** >> boolean

    b. **"a" == "b"** >> boolean

    c. **not True** >> boolean

    d. 5 + 2  

12. Which statements about logical operators are correct?

    a. **and returns True if both parts are true** >> correct: Solo es True si las dos condiciones son True.

    b. **or returns False if both are false** >> correct: Basta con que una sea True para que todo sea True.

    c. **not inverts the truth value** >> correct: Convierte True en False, y viceversa.

    d. and means “either this or that” >> Esa descripción corresponde a or, no a and.

13. Which expressions evaluate to False?

    a. **5 < 3** >> Falso

    b. **not True** >> Falso

    c. 4 == 4

    d. **True and False** >> Falso

14. What are valid uses of the if statement?

    a. **if x > 0:** >> valid

    b. if x == y then:

    c. **if (x < 10):** >> valid

    d. **if x >= 3: print(x)** >> valid

15. What blocks require indentation in Python?

    a. **if** >> requires

    b. **def** >> requires

    c. **for** >> requires

    d. print

16. Which of the following define functions correctly?

    a. **def greet(name):** >> correct

    b. function greet(): >> function no se usa en Python.

    c. **def add(x, y): return x + y** >> correct

    d. def(x): return x * x >> Falta el nombre de la función.

17. What are true about the return statement?

    a. **It sends a result back to the caller** >> correcto

    b. **It ends function execution** >> correcto

    c. **A function can return multiple values** >> correcto

    d. It is optional in all functions >> Solo es opcional si no necesitas devolver nada.

18. Which are examples of chained conditionals?

    a. **if x < 0: ... elif x == 0: ... else: ...** >> correcto

    b. if x < 0 or x == 0 or x > 0: >> Es un solo if con operadores lógicos.

    c. if x < 10: >> Solo un if, sin elif o else.

    d. elif x > 10: >> No puede haber elif sin un if anterior.

19. What are correct uses of pass?

    a. **As a placeholder when a block is required** >> correcto: se usa como marcador de posición cuando el bloque de código es obligatorio pero no quieres escribir nada aún.

    b. To skip a line of code >> incorrecto: no salta líneas, simplemente no hace nada. Si quieres saltarte algo, puedes usar continue o return.

    c. To silence syntax errors >> incorrecto: no arregla errores de sintaxis. Solo evita errores cuando se necesita un bloque de código vacío válido.

    d. **To leave an if or else body empty** >> correcto: Puedes usar pass en el cuerpo de un if, else, for, etc., cuando no quieras ejecutar ninguna acción.

20. Which of the following expressions use valid multiple comparison?

    a. **if 1 < x <= 10:** >> correcta

    b. if x != 5 != y: >> incorrecta

    c. **if 0 < x and x < 100:** >> correcta: Aunque no es una comparación encadenada, es válida y hace lo mismo que 0 < x < 100.

    d. if x < (y < 10): >> incorrecta: Compara x con un booleano (True o False), lo que suele ser un error.

21. What are correct ternary expressions?

    a. **a if cond else b** >> corecto

    b. if cond then a else b >> incorrrecto: Sintaxis no válida en Python.

    c. **"Yes" if x > 5 else "No"** >> correcto

    d. x ? "yes" : "no" >> incorrecto: Sintaxis de otros lenguajes, no de Python.

22. What can be used in a match-case block?

    a. **match value:** >> correcto

    b. **case "hello":** >> correcto

    c. **case _:** >> correcto

    d. if case == ... >> incorrecto: no se usa if de esa forma.

23. What are true about the match-case structure?

    a. **It matches values like a switch** >> correcto

    b. **It requires Python 3.10 or newer** >> correcto

    c. **case _: acts as “default”** >> correcto

    d. You must use parentheses after match >> incorrecto: La sintaxis no lleva paréntesis.

24. Which values are considered falsy in Python?

    a. **[] (empty list)** >> correct

    b. **0.0** >> correct

    c. **""** >> correct

    d. "0" >> Cadena con contenido = verdadero

25. What are valid ways to read and convert user input?

    a. **input("Enter: ")** >> correct

    b. **int(input("Enter a number: "))** >> correct

    c. **input()** >> correct

    d. float("3.14") >> no usa input

26. What can be used to check the available names in a module?

    a. **#dir(math)** >> correcto: Lista los nombres definidos en el módulo.

    b. **#help(math)** >> correcto: Muestra la documentación del módulo.

    c. #list(math) >> incorrecto: no se puede convertir un módulo en lista así.

    d. #math.contents() >> incorrecto: contents() no es una función válida del módulo.

27. Which of the following are expression statements in Python?

    a. **print("Hi")** >> correcto

    b. **x + 3** >> correcto

    c. **len("text")** >> correcto

    d. **"hello" + "world"** >> correcto

28. What are correct statements about local variables?

    a. **They only exist inside the function body** >> correcto

    b. **Their names can be the same as global variables** >> correcto

    c. They are shared across all functions >> incorrecto: Cada función tiene su propio conjunto de variables locales

    d. They are declared with var keyword >> incorrecto: En Python no existe var; solo se usa la asignación directa

29. What can be used to convert between types?

    a. **int("5")** >> correcto

    b. **float("3.14")** >> correcto

    c. **str(5.5)** >> correcto

    d. toString(5) >> incorrecto: No es válida en Python

30. What does the following code print?

        def example():
        
        pass
        
        
        
        print(example())

    a. **None** >> correcto

    b. 0

    c. '' >> No hay retorno de cadena vacía.

    d. Error