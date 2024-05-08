# 3) Задача на декоратор
#
# метод sum(a, b) принимает 2 числа и возвращает их сумму.
# Написать декоратор, который возвращает ошибку
# если переданы не числовые параметры(например строка)
# пример:
#
# @validate_int_parameters
# def sum(a,b)`
#
# sum(3, "1") => ошибка
# sum(4, 2) = > 6

def validate_int_parameters(func):
    def wrapper(a, b):
        if type(a) == int and type(b) == int:
            return func(a, b)
        else:
            raise ValueError('Введены не числовые значения')
    return wrapper
@validate_int_parameters
def sum(a, b):
    return a + b

print(sum(3, 2))
