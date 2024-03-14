# 1) Определить, является ли год високосным.

# первый способ
# import calendar
# year = int(input('Введите год: '))
#
# if calendar.isleap(year):
#     print(f'{year} год високосный.')
# else:
#     print(f'{year} год не високосный.')

# второй способ
year = int(input('Введите год: '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f'{year} год високосный.')
else:
    print(f'{year} год не високосный.')

