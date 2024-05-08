# 1) Реализовать калькулятор с 4 методами:
# Сумма, вычитание , умножение, деление.
# Метод принимает 2 аргумента и возвращает результат.
# Невалидные данные должны быть обработаны(в классе написать проверку на валидность данных)

class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def invalid_number(self):
        if int(self.x) == int and int(self.y) == int:     #не понимаю, почему не срабатывает эта проверка
            self.x = int(self.x)
            self.y = int(self.y)
            return self.x, self.y
        else:
            raise ValueError('Ошибка! Значения должны быть числовыми')


    def sum_X_Y(self):
        return f'Сумма = {self.x + self.y}'

    def difference(self):
        return f'Разность = {self.x - self.y}'

    def multiply(self):
        return f'Результат умножения чисел = {self.x * self.y}'

    def divide(self):
        return f'Результат деления чисел = {self.x / self.y}'


while True:
    operator = input('Введите оператор (+, -, *, /): ')
    if operator in ('+', '-', '*', '/'):
        x = input('Введите первое число: ')
        y = input('Введите второе число: ')
        use_calculator = Calculator(x, y)
        use_calculator.invalid_number()
        if operator == '+':
            print(use_calculator.sum_X_Y())
        elif operator == '-':
            print(use_calculator.difference())
        elif operator == '*':
            print(use_calculator.multiply())
        elif operator == '/':
            if y == 0:
                print( 'На ноль делить нельзя')
                break
            else:
                print(use_calculator.divide())
    elif int(operator) == 0:
        break
    else:
        print('Введён неправильный оператор')
