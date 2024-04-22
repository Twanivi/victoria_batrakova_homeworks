# 4) Функция, вычисляющая среднее арифметическое элементов списка.
# Список должен состоять из случайных чисел, длинной 10 элементов.
import random


def average(list1):
    result = sum(list1) / len(list1)
    print(result)


list1 = [random.randint(1, 100) for i in range(10)]
print(list1)
average(list1)
#
# 5) Создайте функцию, добавьте в неё локальное значение.
# Сделайте так, чтобы другая функция принимала это значение в качестве аргумента.
def multiply():
    num1 = 2
    return num1
def inner(num2):
    num2 = int(input('Введите второе число: '))
    return num1 * num2

def multiply(num1):
    return num1(4)


def inner(num2):
    return num2 * 2


print(multiply(inner))
#
#
# 6) Функция для определения того, каким является число: положительным, отрицательным или нулем
def type_of_number(num1):
    if num1 > 0:
        print(f'Число {num1} является положительным')
    elif num1 < 0:
        print(f'Число {num1} является отрицательным')
    else:
        print(f'Число {num1} является нулём')


num1 = int(input('Введите число: '))
type_of_number(num1)
