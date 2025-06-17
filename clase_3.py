"""
1. What is the output of the following code?
s = "hello"
print(s[1:4])
"""
#ell>> correcto
#hel
#hell
#ello
"""
2. What is the value of count after this code runs?
count = 0
for c in "banana":
   if c == "a":
      count += 1
"""
#1
#2
#3 >> correcto
#0

"""
3. Which of the following loops are infinite?
"""
# while True: pass >> infito
# while 1 == 1: print("loop") >> infinito
# while False: print("never")
# while "abc": print("run") >> infinito

"""
4. Which of the following statements correctly describe what happens inside this loop?

for ch in "abc":
   print(ch * 2, end="")
"""
#Each character is duplicated before being printed >> correcto
#The loop iterates over 6 characters
#The end="" argument prevents newlines
#The string is printed in reverse

"""
5. Which statements are true about the following loop?

i = 0
while i < 3:
   i += 1
   if i == 2:
      continue
   print(i)
"""
#It prints 1 and 3 >> correcto
#It prints 1 and 2
#The continue skips print(i) when i is 2 >> correcto
#The final value of i is 3

"""
6. Which lines result in a TypeError?
"""
#"3" + 3 >> error
#"3" * 3
#3 + int("3")
#"abc" - "a" >> error

"""
7. Which of the following are syntactically valid for loops?
"""
#for letter in "hello": pass >> valido
#for 1 in "abc": pass
#for ch in '': print("ok") >> valido
#for ch in 123: print(ch)

"""
8. What is the value of result after this code?
result = ""
for c in "sun":
   result += c.upper()
"""
result = ""
for c in "sun":
   result += c.upper()
#result is unchanged (strings are immutable)
#"Sun"
#"sun"
#"SUN" >> correct

"""
9. What does the following code print?

text = "abc"
for i in range(len(text)):
   print(text[i])

"""
#Prints a b c on a line
#Prints abc on a line
#Prints each character on a new line >> correcto
#Raises an error

"""
10. What is the final value of i?

i = 0
while i < 5:
   if i == 3:
      break
   i += 1
"""
# 2
# 3 >> correcto
# 4
# 5

"""
11. Which loops terminate?
"""
#while "": print("x") >> el bucle nunca se ejecuta
#while 0: print("x") >> el bucle nunca se ejecuta
#while False == True: print("x") >> el bucle nunca se ejecuta
#while True: break >> Se ejecuta una vez y luego termina

"""
12. Which of the following prints Found!?
for ch in "creative":
   if ch == "a":
      print("Found!")

"""
#Yes, it prints once >> correcto
#No, it never prints
#It prints multiple times
#It gives an error

"""
13. Which of the following range() calls generate exactly 5 numbers?
"""
#range(0, 5) >> correcto
#range(1, 6) >> correcto 
#range(5) >> correcto
#range(10, 0, -2) >> correcto (10 8 6 4 2)

"""
14. Which statements are true about range(start, stop, step)?
"""
#The step argument can be negative >> true 
#start is inclusive and stop is exclusive >> true 
#range(0, 10, -1) raises an error >> no genera nada porque es contradictorio: no puedes ir desde 0 hacia 10 con pasos negativos. Es como intentar llegar a un número mayor yendo hacia atrás.
#range(5, 5) creates an empty range >> el valor final nunca se incluye. Entonces range(5, 5) genera una secuencia vacía porque no hay números entre 5 (incluido) y 5 (excluido).

"""
15. Which of these range() usages result in an empty sequence?
"""
#range(3, 3) >> vacia
#range(10, 5) >> vacia
#range(5, 10, -1) >> vacia
#range(10, 5, -1)

"""
16. Which of the following are valid ways to iterate over all the indices of a string s?
"""
#for i in range(len(s)) >> valid
#for i in range(0, len(s), 1) >> valid
#for i in range(len(s) - 1) >> valid
#for i in s: >> valid

"""
17. Which are valid string methods?
"""
#upper() >> valid
#uppercase()
#sort()
#isdigit() >> valid

"""
18. How many total iterations does the inner loop perform?

for i in range(3):
   for j in range(2):
      print(i + j)
"""
#2
#3
#5
#6 >> correcto

"""
19. When does this loop end?

s = "abc"
i = 0
while i < len(s):
   i += 1
"""
#After 3 iterations >> correcto
#After infinite iterations
#Never ends
#It breaks automatically

"""
20. Which statements about the following loop are true?

for ch in "hello":
   if ch == "l":
      continue
   print(ch, end="")
"""
#The loop skips printing some characters >> True
#The continue causes some iterations to skip print() >> True
#The loop runs only twice
#The print() runs for all characters

"""
21. What is the value of i after the loop ends?

for i in range(3):
   pass
"""

#3
#2 >> correct
#NoneType
#It is an undefined variable

"""
22. What does the following do?

i = 0
while i < 3:
   pass
   i = i + 1
   continue
print(i)
"""

#Prints 3 >> correcto
#Prints 2
#Prints 0
#Prints nothing

"""
23. Which are True?
"""

#A string is iterable >> true
#You can use for x in "abc" >> true
#Strings are mutable
#"abc"[0] = "A" is valid

"""
24. Which expressions are valid?
"""

#"a" in "cat" >> valido
#"z" not in "buzz" >> valido
#"12" in "1234" >> valido
#1 in "1234"

"""
25. Which snippets create an infinite loop?
"""

#while True: continue >> infinito
#while 1: print("x") >> infinito
#for ch in "": print(ch)
#while " ": pass >> infinito

"""
26. Which statements about the following while loop are correct?

i = 0
while i < 5:
   print(i)
   i += 2
"""
#The loop condition is evaluated 3 times >> falso: Se evalúa 4 veces (3 veces True, 1 vez False)
#The loop iterates over even values of i >> verdadero: Imprime: 0, 2, 4 (todos pares)
#The loop runs infinitely
#The loop terminates when i becomes 5 or greater >> verdadero

"""
27. When does this loop end?

n = 0
while "loop":
   n += 1
   break
   n += 2
"""

#Never
#Immediately
#After one iteration >> correcto 
#After string becomes empty

"""
28. Final value of count?

count = 0
for c in "aabaa":
    if c == "a":
        count += 1
    else:
        count -= 1
"""

#5
#3 >> correcto
#2
#1

"""
29. What is the value of text[1:] when text = "python"?
"""

#"ython" >> correcto
#"python"
#"n"
#"pytho"

"""
30. Which statements about the following for...else loop are correct?

code = 0
for ch in "hello":
    if ch == "z":
        code = 1
        break
else:
    code = 2
"""

#The final value of code is 0
#The final value of code is 1
#The final value of code is 2 >> correcto
#The else block is executed