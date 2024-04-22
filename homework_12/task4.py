# 4) Простейший калькулятор с введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: "Деление на ноль"
# Ноль использовать в качестве завершения программы (сделать как отдельную

def sum_of_number(num1, num2):
    return num1 + num2

def difference_of_number(num1, num2):
    return num1 - num2

def multiply_of_number(num1, num2):
    return num1 * num2

def division_of_number(num1, num2):
    return num1 / num2

def zero_of_number(num2):
    return "На ноль делить нельзя"

while True:
    operator = input('Ведите действие (+, -, *, /): ')
    if operator in ('+', '-', '*', '/'):
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        if operator == '*':
            print(multiply_of_number(num1, num2))
        elif operator == '+':
            print(sum_of_number(num1, num2))
        elif operator == '-':
            print(difference_of_number(num1, num2))
        elif operator == '/':
            if num2 == 0:
                print(zero_of_number(num2))
                break
            else:
                print(division_of_number(num1, num2))
    elif int(operator) == 0:
        break
    else:
        print('Введен неверный знак')