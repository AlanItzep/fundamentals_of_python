""" 1. Design an expression that, given three variables with the values of a time expressed in hours, minutes, and seconds, calculates its value expressed in seconds."""
"""
# Solicitar al usuario que introduzca horas, minutos y segundos
horas = int(input("Introduce las horas: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))

# Calcular el total de segundos
total_segundos = horas * 3600 + minutos * 60 + segundos

# Mostrar el resultado
print(f"El tiempo total en segundos es: {total_segundos}")
"""

""" 2. Design an expression that, given a variable with the value of a time expressed in seconds, calculates its value expressed in hours, minutes, and seconds."""
"""
seconds = int(input("Introduce los segundos: "))
dif_h = (seconds % 3600) 
hours = int((seconds - dif_h) / 3600 )
dif_m = dif_h % 60
minutes = int((dif_h - dif_m) / 60)
seconds_f = dif_m
print (f"El tiempo total es: {hours} h y {minutes} mm y {seconds_f} s")
"""

""" 3 Design an expression that, given a variable with a length expressed in meters (integer), decomposes it into Km, Hm, Dm, and m."""
"""
metros = int(input("Introduce los metros: "))
km = metros/1000
hm = metros / 100
dm = metros / 0.1

print (f"Las medidas son las siguiente: {km} Km {hm} Hm {dm} Dm {metros} m")
"""

"""
4. Design an expression that, given a variable with a length expressed in meters (float), decomposes it into Km, Hm, Dm, m, dm, cm, and mm.
"""
"""
metros = float(input("Introduce los metros: "))
km = metros/1000
hm = metros / 100
dam = metros / 10
dm = metros / 0.1
cm = metros / 0.01
mm = metros / 0.001

print (f"Las medidas son las siguiente: {km} Km {hm} Hm {dam} Dm {metros} m {dm} dm {cm} cm {mm} mm ")
"""

"""
5. Design a program that asks the user for a time expressed in hours, minutes, and seconds, and calculates its value expressed in seconds.
"""
"""
# Solicitar al usuario que introduzca horas, minutos y segundos
horas = int(input("Introduce las horas: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))

# Calcular el total de segundos
total_segundos = horas * 3600 + minutos * 60 + segundos

# Mostrar el resultado
print(f"El tiempo total en segundos es: {total_segundos}")
"""
"""
6. Design a program that asks the user for a time expressed in seconds, and calculates its value expressed in hours, minutes, and seconds.
"""
"""
seconds = int(input("Introduce los segundos: "))
dif_h = (seconds % 3600) 
hours = int((seconds - dif_h) / 3600 )
dif_m = dif_h % 60
minutes = int((dif_h - dif_m) / 60)
seconds_f = dif_m
print (f"El tiempo total es: {hours} h y {minutes} mm y {seconds_f} s")
"""
"""
7. Design a program that asks the user for a length expressed in meters (integer) and decomposes it into Km, Hm, Dm, and m.
"""
"""
metros = int(input("Introduce los metros: "))
km = metros/1000
hm = metros / 100
dm = metros / 0.1

print (f"Las medidas son las siguiente: {km} Km {hm} Hm {dm} Dm {metros} m")
"""

"""
8. Design a program that asks the user for a length expressed in meters (float) and decomposes it into Km, Hm, Dm, m, dm, cm, and mm.
"""
"""
metros = float(input("Introduce los metros: "))
km = metros/1000
hm = metros / 100
dam = metros / 10
dm = metros / 0.1
cm = metros / 0.01
mm = metros / 0.001

print (f"Las medidas son las siguiente: {km} Km {hm} Hm {dam} Dm {metros} m {dm} dm {cm} cm {mm} mm ")
"""

"""
9. Design a program that asks the user for the total number of people in a group and the number of people who speak English, and calculates the percentage of people in the group who speak English.
"""
"""
total = float(input("Introduce total de miembros del grupo: "))
t_english = float(input("Introduce numero de miembros que hablan ingles: "))
percentage = (t_english * 100) / total
print (f"El porcentaje de personas que hablan ingles es {percentage} % ")
"""

"""
10. Design a program that asks the user for the gross price of a product and the VAT percentage to be applied, and calculates the final sale price of the product after applying VAT.
"""
"""
gross_price = float(input("El precio bruto del producto: "))
vat = float(input("Introduce el porcentaje aplicado: "))
total_price = gross_price + ((vat * gross_price) /100)
print (f"El precio total del producto es: {total_price} % ")
"""

"""
11. Design a program that asks the user for the price of a bottle of oil at “Superpreu” and the price of the same bottle at “Supertimo”, and calculates the percentage price increase of the product at “Supertimo” relative to “Superpreu”.
"""
superpreu = float(input("El precio del producto en Superpreu: "))
supertimo = float(input("El precio del producto en Supertimo: "))
diferencia = (supertimo * 100) / superpreu
print (f"El producto es: {diferencia} % mas caro ")