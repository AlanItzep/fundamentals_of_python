1. What is the output of the following code?

         s = "hello"
         print(s[1:4])

   a. **ell**>> correcto

   b. hel

   c. hell

   d. ello

2. What is the value of count after this code runs?

         count = 0
         for c in "banana":
            if c == "a":
               count += 1

   a. 1

   b. 2

   c. **3** >> correcto

   d. 0

3. Which of the following loops are infinite?

   a. **while True: pass** >> infito

   b. **while 1 == 1: print("loop")** >> infinito

   c. while False: print("never")

   d. **while "abc": print("run")** >> infinito



4. Which of the following statements correctly describe what happens inside this loop?

         for ch in "abc":
            print(ch * 2, end="")

   a. **Each character is duplicated before being printed** >> correcto

   b. The loop iterates over 6 characters

   c. The end="" argument prevents newlines

   d. The string is printed in reverse

5. Which statements are true about the following loop?

         i = 0
         while i < 3:
            i += 1
            if i == 2:
               continue
            print(i)

   a. **It prints 1 and 3** >> correcto

   b. It prints 1 and 2

   c. **The continue skips print(i) when i is 2** >> correcto

   d. The final value of i is 3

6. Which lines result in a TypeError?

   a. **"3" + 3** >> error

   b. "3" * 3

   c. 3 + int("3")

   d. **"abc" - "a"** >> error



7. Which of the following are syntactically valid for loops?

   a. **for letter in "hello": pass** >> valido

   b. for 1 in "abc": pass

   c. **for ch in '': print("ok")** >> valido

   d. for ch in 123: print(ch)

8. What is the value of result after this code?

         result = ""
         for c in "sun":
            result += c.upper()

         result = ""
         for c in "sun":
            result += c.upper()

   a. result is unchanged (strings are immutable)

   b. "Sun"

   c. "sun"

   d. **"SUN"** >> correct

9. What does the following code print?

         text = "abc"
         for i in range(len(text)):
            print(text[i])

   a. Prints a b c on a line
   
   b. Prints abc on a line
   
   c. **Prints each character on a new line** >> correcto
   
   d. Raises an error

10. What is the final value of i?

         i = 0
         while i < 5:
            if i == 3:
               break
            i += 1

      a. 2

      b. **3** >> correcto

      c. 4

      d. 5
   
11. Which loops terminate?

      a. while "": print("x") >> el bucle nunca se ejecuta

      b. while 0: print("x") >> el bucle nunca se ejecuta

      c. while False == True: print("x") >> el bucle nunca se ejecuta

      d. **while True: break** >> Se ejecuta una vez y luego termina

12. Which of the following prints Found!?

         for ch in "creative":
            if ch == "a":
               print("Found!")

      a. **Yes, it prints once** >> correcto

      b. No, it never prints

      c. It prints multiple times

      d. It gives an error
   
13. Which of the following range() calls generate exactly 5 numbers?

      a. **range(0, 5)** >> correcto

      b. **range(1, 6)** >> correcto 

      c. **range(5)** >> correcto

      d. **range(10, 0, -2)** >> correcto (10 8 6 4 2)
   
14. Which statements are true about range(start, stop, step)?

      a. **The step argument can be negative** >> true 

      b. **start is inclusive and stop is exclusive** >> true 

      c. range(0, 10, -1) raises an error >> no genera nada porque es contradictorio: no puedes ir desde 0 hacia 10 con pasos negativos. Es como intentar llegar a un número mayor yendo hacia atrás.

      d. range(5, 5) creates an empty range >> el valor final nunca se incluye. Entonces range(5, 5) genera una secuencia vacía porque no hay números entre 5 (incluido) y 5 (excluido).
   
15. Which of these range() usages result in an empty sequence?

      a. **range(3, 3)** >> vacia

      b. **range(10, 5)** >> vacia

      c. **range(5, 10, -1)** >> vacia

      d. range(10, 5, -1)
   
16. Which of the following are valid ways to iterate over all the indices of a string s?

      a. **for i in range(len(s))** >> valid

      b. **for i in range(0, len(s), 1)** >> valid

      c. **for i in range(len(s) - 1)** >> valid

      d. **for i in s:** >> valid

17. Which are valid string methods?

      a. **upper()** >> valid

      b. uppercase()

      c. sort()

      d. **isdigit()** >> valid

18. How many total iterations does the inner loop perform?

         for i in range(3):
            for j in range(2):
               print(i + j)

      a. 2

      b. 3

      c. 5

      d. **6** >> correcto
   
19. When does this loop end?

         s = "abc"
         i = 0
         while i < len(s):
            i += 1

      a. **After 3 iterations** >> correcto

      b. After infinite iterations

      c. Never ends

      d. It breaks automatically
   
20. Which statements about the following loop are true?

      for ch in "hello":
         if ch == "l":
            continue
         print(ch, end="")

      a. **The loop skips printing some characters** >> True

      b. **The continue causes some iterations to skip print()** >> True

      c. The loop runs only twice

      d. The print() runs for all characters
   
21. What is the value of i after the loop ends?

         for i in range(3):
            pass


      a. 3

      b. **2** >> correct

      c. NoneType

      d. It is an undefined variable
   
22. What does the following do?

         i = 0
         while i < 3:
            pass
            i = i + 1
            continue
         print(i)


      a. **Prints 3** >> correcto

      b. Prints 2

      c. Prints 0

      d. Prints nothing
   
23. Which are True?

      a. **A string is iterable** >> true

      b. **You can use for x in "abc"** >> true

      c. Strings are mutable

      d. "abc"[0] = "A" is valid
   
24. Which expressions are valid?

   a. **"a" in "cat"** >> valido

   b. **"z" not in "buzz"** >> valido

   c. **"12" in "1234"** >> valido

   d. 1 in "1234"
   
25. Which snippets create an infinite loop?

      a. **while True: continue** >> infinito

      b. **while 1: print("x")** >> infinito

      c. for ch in "": print(ch)

      d. **while " ": pass** >> infinito
   

26. Which statements about the following while loop are correct?

         i = 0
         while i < 5:
            print(i)
            i += 2

      a. The loop condition is evaluated 3 times >> falso: Se evalúa 4 veces (3 veces True, 1 vez False)

      b. **The loop iterates over even values of i** >> verdadero: Imprime: 0, 2, 4 (todos pares)

      c. The loop runs infinitely

      d. **The loop terminates when i becomes 5 or greater** >> verdadero
   
27. When does this loop end?

         n = 0
         while "loop":
            n += 1
            break
            n += 2


      a. Never

      b. Immediately

      c. **After one iteration** >> correcto 

      d. After string becomes empty
   
28. Final value of count?

         count = 0
         for c in "aabaa":
            if c == "a":
               count += 1
            else:
               count -= 1


      a. 5

      b. **3** >> correcto

      c. 2

      d. 1
   
29. What is the value of text[1:] when text = "python"?


      a. **"ython"** >> correcto

      b. "python"

      c. "n"

      d. "pytho"
   
30. Which statements about the following for...else loop are correct?

         code = 0
         for ch in "hello":
            if ch == "z":
               code = 1
               break
         else:
            code = 2


      a. The final value of code is 0
      
      b. The final value of code is 1
      
      c. **The final value of code is 2** >> correcto
      
      d. The else block is executed
   