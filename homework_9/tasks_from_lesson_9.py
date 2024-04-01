# 3) Вам необходимо создать 2 множества а затем из двух этих множеств получить третье множество
# таким образом, чтобы новое множество содержало только те элементы,
# которые есть в обоих исходных множествах.
set1 = {i ** 1 for i in range(10)}
set2 = {i ** 2 for i in range(10)}
print(set1)
print(set2)
set3 = set1 & set2
print(set3)


# 4) Напишите программу, которая проверяет, является ли одно множество подмножеством другого множества.
set1 = {i ** 1 for i in range(10)}
set2 = {i ** 2 for i in range(4)}
print(set1)
print(set2)
answer = False
if set2.issubset(set1):
    answer = True
if answer:
    print(f'Множество set2 {set2} является подмножеством set1 {set1}')
else:
    print(f'Множество set2 {set2} не является подмножеством set1 {set1}')


# 5) Напишите программу, которая будет генерировать множество,
# а на выходе программа  возвращает список, содержащий все элементы этого множества, умноженные на 2.
set1 = {i ** 1 for i in range(10)}
print(set1)
list2 = list(set1)
for i in set1:
    list2[i] = i * 2
print(list2)


# 6) Создайте два множества из списка слов "apple", "banana", "orange", "grape", "kiwi" и "banana".
# Выведите на экран разность этих множеств.
set1 = {"apple", "banana", "orange", "grape"}
set2 = {"kiwi", "banana"}
print(set1.symmetric_difference(set2))


# 7) Напишите программу, которая удаляет все дубликаты из списка и создает из него множество.
import random
even_numbers = [random.randint(0, 10) for i in range(10)]
print(even_numbers)
remove_copy_elements = list(set(even_numbers))
print(remove_copy_elements)


# 8. Сгенерируйте два множества. Программа должна вернуть новое множество,
# содержащее все элементы из первого множества, которых нет во втором.
set1 = {i ** 1 for i in range(10)}
set2 = {i ** 2 for i in range(10)}
print(set1)
print(set2)
set3 = set1 - set2
print(set3)
