# 1. Используя стандартные арифметические операции представьте самое большое целое число из цифр 4, 4, 4
#    и приведите его значение.
# print(4 ** 4 ** 4)
#
# 2. Написать программу для вычисления значения выражений. Проверить правильность выполнения задания
#    с помощью тестовых значений.
#
# a.
# import math
# a = int(input('Введите значение α: '))
# b = int(input('Введите значение β: '))
# y = int(input('Введите значение γ: '))
# result = (1 / 4) * math.ceil(math.sin(a + b - y) + math.sin(b + y - a) + math.sin(y + a - b) - math.sin(a + b + y))
# print(f'При значении α = {a}, значении β = {b} и значении γ = {y}, результатом будет {result}')

#
# 3. Создать пустую переменную. Проверить ее на истинность и ложность. Объясните полученный результат.
# x = None
# if bool(x) == False:
#     print('Переменная x пустая')
# else:
#     print('Переменная x не пустая')
# Объяснение: ‘0’, », [], {}, (), None являются ложными значениями. Таким образом,
#              если переменная содержит одно из этих значений, она считается пустой

# 4. В строке “Иван Иванов” поменяйте
# местами слова. Может быть предоставлена любая строка с именем и фамилией. Например, “Петр Иванов” = > “Иванов Петр”
# x = 'Иван Иванов'
# y = x[5::1] + x[4] + x[:5:1]
# print(y)
#
# 5. Создать список с числами от 1 до 50 используя генератор списков.
# x = [i for i in range(1, 51)]
# print(x)
#
# 6. Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
#    кроме одного: [1, 5, 2, 9, 2, 9, 1] = > 5
# x = [1, 5, 2, 9, 2, 9, 1]
# for i in x:
#     if x.count(i) == 1:
#         print(f'Число не имеющее пары = {i}')
#
# 7. Дан список[student1, student2, student3] с помощью цикла for добавить к каждому элементу списка
#    слово “_good”.Вывести на экран.
# list1 = ['student1', 'student2', 'student3']
# list2 = []
# for i in list1:
#     i += ' good'
#     list2.append(i)
# print(list2)
#
# 8. Вывести на экран числа от 0 до 50, кроме 35.
# x = [i for i in range(0, 51)]
# for i in x:
#     if i == 35:
#         x.remove(i)
# print(x)
#
# 9. Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”]. В новый список добавить элементы,
#    которые содержат пробел.
# list1 = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
# list2 = []
# for i in list1:
#     if ' ' in i:
#         list2.append(i)
# print(list2)
#
# 10. В классе N школьников. На уроке физкультуры тренер говорит «на первый - второй рассчитайтесь».
#     Выведите, что скажут ученики.
#     Входные данные: Вводится одно целое число — количество человек в классе.
#     Входные данные: Выведите последовательность чисел 1 и 2, в том порядке, как будут говорить школьники.
# n = int(input('Введите количество ученков в классе: '))
# for i in range(n):
#     if i % 2 == 0:
#         print(1)
#     else:
#         print(2)
# #
# 11. Дан список чисел, необходимо удалить все вхождения числа 20 из него.
# import random
# x = [random.randint(15, 21) for i in range(10)]
# print(x)
# for i in x:
#     if i == 20:
#         x.remove(i)
# print(x)
#
# 12. С клавиатуры вводится десятизначное число. Вывести на экран четные числа входящие в данное число.
#     Например, 1234567892  2 4 6 8 2
# x = int(input('Введите десятизначное значение: '))
# list_x = [int(i) for i in str(x)]
# for i in list_x:
#     if i % 2 == 0:
#         print(i)
# #
# 13. Необходимо удалить пустые строки из списка строк. Пример списка:
#     [‘1’, ‘2’, ‘3’, ‘4’, ’hello’, ‘’, ‘good’, ‘’, ‘’, ‘5’, ‘6’, ‘7’]
# list1 = ['1', '2', '3', '4', 'hello', '', 'good', '', '', '5', '6', '7']
# while '' in list1:
#     list1.remove('')
# print(list1)
#
# 14. Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и
#     самое длинное.
# text = input('Введите предложение: ').lower().split()
# text_dict = {}
# for item in text:
#     if item in text_dict:
#         text_dict[item] += 1
#     else:
#         text_dict[item] = 1
# print(text_dict)
# max_value = 1
# key_max_value = []
# longest = ''
# longest_words = []
# for key, value in text_dict.items():
#     if value > max_value:
#         key_max_value = [key]
#         max_value = value
#     elif value == max_value:
#         key_max_value.append(key)
# for i in text:
#     if len(i) > len(longest):
#         longest_words = [i]
#         longest = i
#     elif len(i) == len(longest):
#         longest_words.append(i)
# print(f"Наиболее часто встречающееся слово: {key_max_value}")
# print(f"Самое длинное слово: {longest_words}")

#
# 15 *.Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и
#      C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
#      Например, в строке "acggtgttat" процентное содержание символов G и C равно 4 / 10 ⋅ 100 = 40.0
#      где 4 - это количество символов G и C, а 10 - это длина строки.
# dna = input('Введите генетический код: ').lower()
# count = 0
# percent = 0
# for i in dna:
#     if (i == 'c') or (i == 'g'):
#         count += 1
#         percent = (count/len(dna))*100
# print (f'Процентное содержание символов в dna = {percent}')

#
# 16 *.Дезоксирибонуклеиновая кислота (ДНК) представляет собой химическое вещество, находящееся в ядре клеток
#      и несущее «инструкции» по развитию и функционированию живых организмов.
#      В цепочках ДНК символы «А» и «Т» дополняют друг друга, как «С» и «G».
#      Вам нужно вернуть другую дополнительную сторону. Нить ДНК никогда не бывает пустой или ДНК вообще не существует.
#      Пример: (ввод --> вывод)
#      “АТТGС" --> "ТААСG"
#      “GТАТ" --> "САТА"

# dna_list = list(dna)
# reverse_dna = []
# for i in range(0, len(dna_list) - 1):
#     if dna_list[i] == 'A':
#         reverse_dna.append('T')
#     elif dna_list[i] == 'T':
#         reverse_dna.append('A')
#     elif dna_list[i] == 'C':
#         reverse_dna.append('G')
#     elif dna_list[i] == 'G':
#         reverse_dna.append('C')
#     i += 1
#     print(i)
# print(reverse_dna)
# new = ''
# for i in dna:
#     if i == 'A':
#         new += 'T'
#     if i == 'T':
#         new += 'A'
#     if i == 'C':
#         new += 'G'
#     if i == 'G':
#         new += 'C'
#     print(i)
#     print(new)

# ls = list(dna)
# dna[i], dna[j] = dna[j], dna[i]

# dna = "".join(ls)

# print(dna)

# dna = input("Введите ДНК: ")
# complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
# dna_list = list(dna)
# for i in range(len(dna_list)):
#     dna_list[i] = complement[dna_list[i]]
# complement_dna = ''.join(dna_list)
# print("Дополнительная сторона ДНК:", complement_dna)

dna = input('Введите генетический код: ').lower()
print(dna)
i = dna.index('a')
j = dna.find('t')
print(i, j)