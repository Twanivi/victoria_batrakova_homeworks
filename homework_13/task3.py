# 3) Написать 12 функций по переводу:
#
# 1. Дюймы в сантиметры
# 2. Сантиметры в дюймы
# 3. Мили в километры
# 4. Километры в мили
# 5. Фунты в килограммы
# 6. Килограммы в фунты
# 7. Унции в граммы
# 8. Граммы в унции
# 9. Галлон в литры
# 10. Литры в галлоны
# 11. Пинты в литры
# 12. Литры в пинты

# 1)
def inch_to_cm(inch):
    cm = inch * 2.54
    return  cm


inch = int(input('Введите значение в сантиметрах: '))
print(inch_to_cm(inch))

# 2)
def cm_to_inch(cm):
    inch = cm / 2.54
    return  inch


cm = int(input('Введите значение в дюймах: '))
print(cm_to_inch(cm))

# 3)
def miles_to_km(miles):
    km = miles * 1.609
    return km

miles =  int(input('Введите значение в милях: '))
print(miles_to_km(miles))

# 4)
def km_to_miles(km):
    miles = km / 1.609
    return miles

km =  int(input('Введите значение в километрах: '))
print(km_to_miles(km))

# 5)
def pounds_to_kg(pounds):
    kg = pounds / 2.2
    return kg

pounds =  int(input('Введите значение в фунтах: '))
print(pounds_to_kg(pounds))

# 6)
def kg_to_pounds(kg):
    pounds = kg * 2.2
    return pounds

kg =  int(input('Введите значение в килограммах: '))
print(kg_to_pounds(kg))

# 7)
def ounces_to_grams(ounces):
    grams = ounces * 28.35
    return grams

ounces =  int(input('Введите значение в унциях: '))
print(ounces_to_grams(ounces))

# 8)
def grams_to_ounces(grams):
    ounces = grams / 28.35
    return ounces

grams = int(input('Введите значение в граммах: '))
print(grams_to_ounces(grams))

# 9)
def gallon_to_liters(gallon):
    liters = gallon * 4.55
    return liters

gallon = int(input('Введите значение в галлонах: '))
print(gallon_to_liters(gallon))

# 10)
def liters_to_gallon(liters):
    gallon = liters / 4.55
    return gallon

liters = int(input('Введите значение в литрах: '))
print(liters_to_gallon(liters))

# 11)
def pints_to_liters(pints):
    liters = pints * 0.568261
    return liters

pints = int(input('Введите значение в пинтах: '))
print(pints_to_liters(pints))

# 12)
def liters_to_pints(liters):
    pints = liters / 0.568261
    return pints

liters = int(input('Введите значение в литрах: '))
print(liters_to_pints(liters))
