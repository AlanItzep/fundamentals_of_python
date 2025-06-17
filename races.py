def seconds(hour, minute, second):
    return hour * 3600 + minute * 60 + second

def hms(seconds):
    hours = seconds // 3600
    reamining = seconds % 3600 
    minutes = reamining // 60
    seconds = reamining % 60
    return hours, minutes, seconds

#print(hms(3600))
def diff_s(h1,m1,s1,h2,m2,s2):
    seconds_1 = seconds(h1,m1,s1)
    seconds_2 = seconds(h2,m2,s2)
    return abs(seconds_1 - seconds_2)

def diff_hms(h1,m1,s1,h2,m2,s2):
    seconds_1 = seconds(h1,m1,s1)
    seconds_2 = seconds(h2,m2,s2)
    result = abs(seconds_1 - seconds_2)
    return hms(result)

def avg_s(h1, m1, s1, h2, m2, s2, h3, m3, s3):
    seconds_1 = seconds(h1,m1,s1)
    seconds_2 = seconds(h2,m2,s2)
    seconds_3 = seconds(h3,m3,s3)
    result = round(int((seconds_1+seconds_2+seconds_3) / 3))
    return result

def avg_hms(h1, m1, s1, h2, m2, s2, h3, m3, s3):
    avg_in_seconds = avg_s(h1, m1, s1, h2, m2, s2, h3, m3, s3)
    return hms(avg_in_seconds)

"""
horas_1 = int(input("Introduce las horas iniciales: "))
minutos_1 = int(input("Introduce los minutos iniciales: "))
segundos_1 = int(input("Introduce los segundos iniciales: "))

horas_2 = int(input("Introduce las horas finales: "))
minutos_2 = int(input("Introduce los minutos finales: "))
segundos_2 = int(input("Introduce los segundos finales: "))
"""
"""
Part 1: Time Difference in Seconds
"""
# print(diff_s(3, 23, 17, 3, 34, 1)) # 0 , 11 , 16
# print(diff_s(3, 23, 17, 3, 23, 16))
# print(diff_s(3, 23, 17, 3, 24, 17))
# print(diff_s(4, 0, 0, 3, 56, 31))
# print(f"La diferencia en segundos es: {diff_s(horas_1, minutos_1, segundos_1, horas_2, minutos_2, segundos_2)}")

"""
Part 2: Time Difference in h:m:s
"""
# print(diff_hms(3, 23, 17, 3, 34, 1))
# print(diff_hms(3, 23, 17, 3, 23, 16))
# print(diff_hms(3, 23, 17, 3, 24, 17))
# print(diff_hms(4, 0, 0, 3, 56, 31))

"""
Part 3: Average Time of Three Races in Seconds
"""
# print(avg_s(3, 44, 13, 3, 51, 20, 4, 1, 14))
# print(avg_s(3, 44, 13, 3, 44, 13, 3, 44, 13))
# print(avg_s(3, 50, 10, 4, 0, 10, 3, 55, 10))
# print(avg_s(3, 59, 14, 4, 1, 14, 4, 0, 14))

"""
Part 4: Average Time of Three Races in h:m:s
"""
print(avg_hms(3, 44, 13, 3, 51, 20, 4, 1, 14))
print(avg_hms(3, 44, 13, 3, 44, 13, 3, 44, 13))
print(avg_hms(3, 50, 10, 4, 0, 10, 3, 55, 10))
print(avg_hms(3, 59, 14, 4, 1, 14, 4, 0, 14))