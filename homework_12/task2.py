# 2) Создайте функцию для вывода таблицы умножения для указанного числа
def table_of_multiply(num1):
    for i in range(1, 10):
        result = i * num1
        print(f'{i} * {num1} = {result}')


num1 = int(input('Введите число: '))
table_of_multiply(num1)