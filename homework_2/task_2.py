# 2) Вычислить сумму цифр случайного трёхзначного числа (тут необходимо
# применить работу со строками)

# вариант при запросе у пользователя
# num_3 = input('Введите трёхзначное число: ')
# sum_num_3 = int(num_3[0]) + int(num_3[1]) + int(num_3[2])
# print(sum_num_3)

import random

number = random.randint(100, 999)
print(number)
number_str = str(number)
sum_number = int(number_str[0]) + int(number_str[1]) + int(number_str[2])
print(sum_number)
