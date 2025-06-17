"""
1. String Queries
What are the values of the variables a, b, c, d, e, f, g, and length after executing the following code?
"""
"""
s = "abcdef"
a = s[3] #d
b = s[5] #f
c = s[0] #a
length = len(s) #6
d = s[length - 1] # f
e = s[length - 4] #c
f = s[-1] #f
g = s[-4] #c 
print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}, f: {f} g: {g}")
# a: d, b: f, c: a, d: f, e: c, f: f g: c
"""
"""
2. NIF Letter
Design the function nif_letter(dni) that takes an integer representing a DNI number and returns a string with the corresponding NIF (DNI + letter). 
The letter is determined by the remainder of dividing the DNI by 23, using the string "TRWAGMYFPDXBNJZSQVHLCKE".
"""

def nif_letter(dni):
    chain = "TRWAGMYFPDXBNJZSQVHLCKE"
    product = dni%23
    letter = chain[product]
    final_nif = str(dni) + letter
    return final_nif


"""
3. Expanding Years
Design the function expand_years(text) that returns the same string but replacing all 2-digit years (preceded by “year” or “Year”) with full 4-digit years from the 20th century.
"""

def expand_years(text):
    words = text.split()
    words_modified = []

    for word in words:
        if word.isdigit() and 0 <= int(word) <= 99:
            words_modified.append(str(1900 + int(word)))
        else:
            words_modified.append(word)
    return ' '.join(words_modified)


"""
4. Currency Strings
Design the following functions:

extract_currency(string): Returns the 3-letter currency from a string like "235 EUR", or an empty string if the input is empty.

extract_amount(string): Returns the integer amount from a string like "235 EUR", or -1 if the input is empty.

calculate_expense(employee_expense): Receives an expense string like "PM:120 USD" and returns a float with the value converted to euros. Conversion: 1 USD = 0.9 EUR, 1 AUD = 0.65 EUR. Directors (D) have zero cost. Employee types: D (director), PM (project manager), T (technician).

convert_expense(employee_expense): Returns a string like "108 EUR" with the rounded integer value converted to euros.
"""

def extract_currency(amount):
    space_character = amount.find(" ")
    if space_character != -1:
        currency = amount[(space_character+1):]
        return currency
    else:
        return ""
    
def extract_amount(amount):
    space_character = amount.find(" ")
    if space_character != -1:
        quantity = int(amount[:space_character])
        return quantity
    else:
        return int(space_character)
    
def calculate_expense(employee_expense):
    USD = 0.9 #EUR
    AUD = 0.65 #EUR
    points_sep = employee_expense.find(":")
    amount = employee_expense[points_sep+1:]
    employee_type = employee_expense[:points_sep]
    if employee_type != "D":
        if extract_currency(amount) == "USD":
            quantity_usd = int(extract_amount(amount)) * USD
            return quantity_usd
        elif extract_currency(amount) == "AUD":
            quantity_aud = int(extract_amount(amount)) * AUD
            return quantity_aud
        elif extract_currency(amount) == "EUR":
            quantity_eur = 0.0
            return quantity_eur
    else:
        ## tarifa especial
        return 0.0

def convert_expense(employee_expense): 
    rounded_euros = str(round(calculate_expense(employee_expense))) + " EUR"
    return rounded_euros

#print(extract_currency("235 EUR"))
#print(extract_currency(""))

#print(extract_amount("1029 USD"))
#print(extract_amount(""))

#print(calculate_expense("D:230 EUR"))
#print(calculate_expense("PM:120 USD"))
#print(calculate_expense("T:110 AUD"))

#print(convert_expense("D:230 EUR"))
#print(convert_expense("PM:120 USD"))
#print(convert_expense("T:110 AUD"))


"""
5. Reverse a String
Design the function reverse1(text) that returns the reversed version of the input string by iterating over its characters.

Design the function reverse2(text) that does the same using slicing only (no loop).
"""

def reverse1(text):
    text_reversed = ""
    for char in text:
        text_reversed = char + text_reversed
    return text_reversed

def reverse2(text):
    reversed_text = text[::-1]
    return reversed_text

#print(reverse1("It rains and shines"))
#print(reverse1("dog"))

#print(reverse2(""))
#print(reverse2("a"))

"""
6. Common Characters
Design the function common_chars(s1, s2) that returns a string containing characters that are in both inputs, without duplicates, and in the order they appear in s1.
"""
"""
def common_chars(s1, s2):
    chars_in_common = ""
    for char in s1:
        if char in s2 and char not in chars_in_common: 
            chars_in_common += char
        else:
            ""
    return chars_in_common

print(common_chars("sausages", "salsa"))
print(common_chars("orange", "pepper"))
print(common_chars("potato", "aubergine"))
"""

"""
7. Alphabetical Order
Design the function is_alphabetical(s) that returns True if the lowercase letters in the string are in alphabetical order.
"""
"""
def is_alphabetical(s):
    lowercase_letters = [char for char in s if char.islower()]
    return lowercase_letters == sorted(lowercase_letters)

print(is_alphabetical("abcdef"))
print(is_alphabetical("adfrget"))
"""


"""
8. Counting Letters
Design the function count_case(text) that returns two values, the number of uppercase letters , and the number of lowercase letters in the input string.

Design the function vowel_percentage(text) that returns the percentage of vowels over the total number of letters in the input string (including spaces and punctuation).
"""

"""
def count_case(text):
    lowercase_letters = [char for char in text if char.islower()]
    is_number= [char for char in text if char.isdecimal()]
    len_lowercase_letters = len(lowercase_letters+is_number)
    uppercase_letters = [char for char in text if char.isupper()]
    len_upperase_letters = len(uppercase_letters)
    return len_upperase_letters, len_lowercase_letters

def vowel_percentage(text):
    lentext_total= len(text)
    vocales = "aeiouAEIOU"  # Lista de vocales (mayúsculas y minúsculas)
    cantidad_vocales = 0
    for caracter in text:
        if caracter in vocales:
            cantidad_vocales += 1
    print(cantidad_vocales)
    resultado = (cantidad_vocales * 100) / lentext_total 
    return resultado

#print(count_case("NASA launched the James Webb Space Telescope in 2021"))
#print(count_case("The theory of relativity was published in 1905"))
#print(round(vowel_percentage("NASA launched the James Webb Space Telescope in 2021"), 2)) ##>> valores de resultado diferentes
#print(round(vowel_percentage("The theory of relativity was published in 1905"), 2)) ##>> valores de resultado diferentes
"""

"""
9. Password Validation
Design the function contains_uppercase(text) that returns True if the string contains any uppercase letters.

Design the function check_password(new, old) that returns:

1 if both passwords are the same

2 if the new password has less than 8 characters

3 if the new password has no uppercase letters

In all other cases, we will consider the password valid and return 0.
"""
"""
def contains_uppercase(text):
    result = [char for char in text if char.isupper()]
    return bool(result)

def check_password(new, old):
    new_pass_len = len(new)
    new_pass_upper = contains_uppercase(new)
    if new == old:
        return 1
    elif new_pass_len < 8:
        return 2
    elif new_pass_upper != True:
        return 3
    else:
        return 0

print(contains_uppercase("05687xsdD"))
print(check_password("myStrongPassword", "myStrongPassword"))
print(check_password("aNewOne", "myStrongPassword"))
print(check_password("thenewone", "myStrongPassword"))
print(check_password("theNewOne", "myStrongPassword"))
"""

"""
10. Validate e-Mail Address
Write a function is_valid_email(email) that returns True if the string is a valid email address, and False otherwise.

Use only basic tools covered so far: string slicing, string methods, conditionals, logical operators, and functions.

The function must check all of the following:

General requirements:

* The email contains exactly one @ symbol.
* It does not contain any spaces.
* Both parts of the address (nickname and domain) are non-empty.

Nickname (before the @):

* Cannot end with a dot .

Domain (after the @):

* Must contain at least one dot .
* Must not start with a digit, dot . or hyphen -
* Must not end with a hyphen
* The Top-Level Domain (TLD, after the last .) must be at least two characters long
* The domain may contain digits and hyphens, but only letters are allowed in the TLD

"""
"""
def is_valid_email(email):
    # Revisar que al menos tenga un arroba
    if email.count("@") != 1:
        return False
    
    # Encontrar la posicion de la arroba
    arroba_position = email.find("@")

    # Splitear la parte del nickname y del dominio usando slicing
    nickname = email[:arroba_position]
    domain_complete = email[arroba_position + 1:]

    # Revisar espacios
    if " " in email:
        return False
    
    # Revisar que el nickname y el dominio no este vacio
    if not nickname or not domain_complete:
        return False
    
    # Revisar el nickname no termine con punto
    if nickname[-1] == ".":
        return False
    
    # Encontrar la posicion del punto en el dominio
    first_dot_position = domain_complete.find(".")
    
    # Splitear el dominio entero entre dominio y tdl
    domain = domain_complete[:first_dot_position]
    tdl = domain_complete[first_dot_position + 1:]

    # Revisar si el dominio empieza por numero, punto o guion y que no este vacio
    if domain and (domain[0].isdigit() or domain[0] == "." or domain[0] == "-"):
        return False
    
    # Revisar que el dominio no termine con guion
    if domain and domain[-1] == "-":
        return False
    
    # Revisar que tdl es mayor a dos caracteres y que solo contenga caracteres
    if len(tdl) < 2 or not tdl.isalpha():
        return False

    return True
    

# print(is_valid_email("alan@example.com"))
# print(is_valid_email("john@example.c"))
# print(is_valid_email("john@123domain.com"))
# print(is_valid_email("john@.example.com"))
# print(is_valid_email("john@example-.com"))
# print(is_valid_email("john@example123.com"))
# print(is_valid_email("john.@example.com"))
# print(is_valid_email("john@domain.9g"))
# print(is_valid_email("john@domain.g1"))
"""
"""
11. Add Line Numbers to a Multiline String
Design the function number_lines(text) that receives a string containing multiple lines (separated by newline characters \n), 
and returns a new string where each line is prefixed with its corresponding line number, starting at 1, followed by a colon and a space.

Implement two versions of the function:

One using a for loop with range

Another using a while loop
"""
"""
def number_lines(text):
    new_text = ""
    line_start = 0
    line_number = 1
    for line in range(len(text)): 
        if text[line] == '\n':
            new_text += f"{line_number}: {text[line_start:line+1]}"
            line_start = line + 1
            line_number += 1
    
    if line_start < len(text):
        new_text += f"{line_number}: {text[line_start:]}"

    return new_text
"""
"""
def number_lines(text):
    new_text = ""
    line_start = 0
    line_number = 1

    character = 0

    while character < len(text):
        if text[character] == '\n':
            new_text += f"{line_number}: {text[line_start:character+1]}"
            line_start = character + 1
            line_number += 1
        character += 1
    
    if line_start < len(text):
        new_text += f"{line_number}: {text[line_start:]}"

    return new_text
"""

# print(number_lines("First line\nSecond line\nThird line"))
# 1: First line
# 2: Second line
# 3: Third line

# print(number_lines("Alpha\nBeta"))
#1: Alpha
#2: Beta

# print(number_lines(""))
#(an empty string)
"""
12. Remove Parenthesized Comments from a String
Design the function remove_comments(text) that receives a string and returns a new string with all content enclosed in parentheses removed, including the parentheses themselves.

You may assume that parentheses do not nest (i.e., you will not find a parenthesis inside another pair of parentheses).
"""
def remove_comments(text):
    new_text = ""
    inside_comment = False
    skip_next_char = False

    for i in range(len(text)):
        char = text[i]

        if skip_next_char:
            skip_next_char = False
            continue

        if char == "(":
            inside_comment = True
            # No eliminamos el espacio aquí. La limpieza de espacios al final es más segura.
        elif char == ")":
            inside_comment = False
            # Si hay un espacio inmediatamente después del ')' en el texto original,
            # marcamos la bandera para saltarlo en la siguiente iteración.
            if i + 1 < len(text) and text[i + 1] == " ":
                skip_next_char = True
        else:
            if not inside_comment:
                new_text += char
    
    # --- Post-procesamiento de espacios ---
    # Esta parte es crucial para asegurar el formato correcto de los espacios.
    
    # 1. Eliminar espacios iniciales
    while len(new_text) > 0 and new_text[0] == ' ':
        new_text = new_text[1:]
    
    # 2. Eliminar espacios finales
    while len(new_text) > 0 and new_text[-1] == ' ':
        new_text = new_text[:-1]
        
    # 3. Colapsar múltiples espacios en uno solo
    # y también corregir espacios antes de la puntuación.
    
    final_cleaned_text = ""
    last_char_was_space = False
    
    # Definimos los caracteres de puntuación que no deben tener un espacio delante
    punctuation_no_pre_space = ".,!?;:" 

    for char in new_text:
        if char == ' ':
            if not last_char_was_space: # Añadir el espacio solo si el último no fue un espacio
                final_cleaned_text += ' '
            last_char_was_space = True
        elif char in punctuation_no_pre_space:
            # Si el caracter actual es puntuación y el último caracter añadido fue un espacio,
            # eliminamos ese espacio antes de añadir la puntuación.
            if len(final_cleaned_text) > 0 and final_cleaned_text[-1] == ' ':
                final_cleaned_text = final_cleaned_text[:-1]
            final_cleaned_text += char
            last_char_was_space = False # La puntuación no se considera un "espacio"
        else:
            final_cleaned_text += char
            last_char_was_space = False
            
    return final_cleaned_text
    
#print(remove_comments("Python (a powerful language) is fun."))
#print(remove_comments("This is (just) a test (really)."))
#print(remove_comments("No comments here."))
#print(remove_comments("(start) Only text."))

"""
13. Adjust All Numbers in a Text
Design the function adjust_numbers(text, delta) that receives a string containing words and integer numbers, and a second argument delta (an integer). 
The function should return a new string where all integer numbers found in the text have been increased by delta. 
Words and punctuation should remain unchanged.

You can assume that:

All numbers are positive integers.

A number always appears surrounded by spaces**, or between a space and a period (dot).

You do not need to handle decimal, negative, or comma-separated numbers.
"""

def adjust_numbers(text, delta):
    new_text = ""
    skip_until_index = -1

    for i in range(len(text)):
        if i < skip_until_index:
            continue

        char = text[i]

        if char.isdigit():
            # encontramos el inicio del numero
            current_number_str = ""
            temp_index = i # se usa j para leer el numero completo sin afectar i todavia 

            # leemos todos los digitos consecutivos
            while temp_index < len(text) and text[temp_index].isdigit():
                current_number_str += text[temp_index]
                temp_index += 1

            # convertivmos, sumamos delta y añadimos al nuevo texto
            original_number = int(current_number_str)
            adjusted_numbers = original_number + delta
            new_text += str(adjusted_numbers)

            # Marcamos hasta qué índice debemos saltar en el bucle principal 'for'.
            # 'j' ya está en el carácter *después* del número.
            skip_until_index = temp_index
        else:
            new_text += char

    return new_text

#print(adjust_numbers("I ran 5 kilometers and drank 2 liters of water.", 1))
#'I ran 6 kilometers and drank 3 liters of water.'
#print(adjust_numbers("Today I have 3 meetings.", 2))
#'Today I have 5 meetings.'
#print(adjust_numbers("No numbers here!", 10))
#'No numbers here!'
#print(adjust_numbers("The event starts at 9 and ends at 14.", 1))
#'The event starts at 10 and ends at 15.'