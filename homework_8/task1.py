# 1) Дан словарь, ключами которого являются имена студентов, а значениями - их оценки по математике.
# Напишите программу для вычисления средней оценки по математике для всех студентов.

dict1 = {'Иванов': 7, 'Петров': 8, 'Смирнова': 9, 'Лобанова': 6, 'Кузнецов': 4}
sum_of_value = 0
average = 0
for value in dict1.values():
    print(value)
    sum_of_value += value
    average = sum_of_value / len(dict1)
print(average)
