def age(day_birth, month_birth, year_birth, day_today, month_today, year_today):
    years = 0
    if month_today <= month_birth and day_today < day_birth:
        years = (year_today - year_birth) - 1
    else:
        years = (year_today - year_birth)
    return years

def complete_year(year, century):
    full_year = ((century-1)*100)+year
    return full_year

def age_21(day_birth, month_birth, year_birth, day_today, month_today, year_today):
    year_birth_internal = 0
    year_today_internal = 0

    if 0 <= year_birth <= 99:
        year_birth_internal = complete_year(year_birth, 21)
    else: 
        year_birth_internal = year_birth
    
    if 0 <= year_today <= 99:
         year_today_internal = complete_year(year_today, 21)
    else:
        year_today_internal = year_today
    
    return age(day_birth, month_birth, year_birth_internal, day_today, month_today, year_today_internal)

def compare_dates(d1, m1, y1, d2, m2, y2):
    if y1 < y2:
        result = -1
    elif y1 > y2:
        result = 1
    else:
        if m1 < m2:
            result = -1
        elif m1 > m2:
            result = 1
        else:
            if d1 < d2:
                result = -1
            elif d1 > d2:
                result = 1
            else: 
                result = 0
    return result

def is_earlier(d1, m1, y1, d2, m2, y2):
    result = compare_dates(d1, m1, y1, d2, m2, y2)
    match result:
        case -1:
            return True
        case 1 | 0:
            return False
        case _:
            return False

def is_equal(d1, m1, y1, d2, m2, y2):
    result = compare_dates(d1, m1, y1, d2, m2, y2)
    match result:
        case 0:
            return True
        case 1 | 1:
            return False
        case _:
            return False

def is_later(d1, m1, y1, d2, m2, y2):
    result = compare_dates(d1, m1, y1, d2, m2, y2)
    match result:
        case 1:
            return True
        case -1 | 0:
            return False
        case _:
            return False
    

"""
Part 1: Compute Age
"""
# print(age(10, 4, 1990, 23, 5, 2013))
# print(age(10, 4, 1990, 5, 3, 2013))

"""
Part 2: Complete Year from Century
"""
#print(complete_year(57, 20))
#print(complete_year(16, 21))

"""
Part 3: Compute Age with Flexible Year Format
"""
#print(age_21(10, 4, 1990, 23, 5, 13))
#print(age_21(10, 4, 3, 5, 3, 2013))

"""
Part 4: Compare Two Dates
"""
#print(compare_dates(10, 4, 1917, 8, 2, 1923))
#print(compare_dates(10, 4, 1917, 8, 4, 1917))
#print(compare_dates(10, 4, 1917, 10, 4, 1917))

"""
Part 5: Boolean Date Comparison Functions
"""

print(is_earlier(10, 4, 1917, 8, 2, 1923))
print(is_equal(10, 4, 1917, 8, 2, 1923))
print(is_later(10, 4, 1917, 8, 2, 1923))
print("*****")
print(is_earlier(10, 4, 1917, 8, 4, 1917))
print(is_equal(10, 4, 1917, 8, 4, 1917))
print(is_later(10, 4, 1917, 8, 4, 1917))
print("*****")
print(is_earlier(10, 4, 1917, 10, 4, 1917))
print(is_equal(10, 4, 1917, 10, 4, 1917))
print(is_later(10, 4, 1917, 10, 4, 1917))