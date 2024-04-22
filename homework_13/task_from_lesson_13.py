# 3) Напишите программу, которая принимает на вход список чисел в одной строке и
# выводит на экран в одну строку значения, которые встречаются в нём более одного раза.

input_numbers = list(input('Введите числа: '))
print(input_numbers)
new_list = list(set(filter(lambda i: input_numbers.count(i) > 1, input_numbers)))
print(new_list)
new_str = ''.join(new_set)
print(new_str)
