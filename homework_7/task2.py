# 2) Дан список чисел. Если в нем есть два соседних элемента одного знака,
# выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего.
# Если таких пар соседей несколько — выведите первую пару
import random

x = [random.randint(-100, 100) for i in range(10)]
print(x)
pair_of_numbers = []
for i in range(len(x)-1):
    if (x[i] > 0 and x[i+1] > 0) or (x[i] < 0 and x[i+1] < 0):
        pair_of_numbers.append(x[i])
        pair_of_numbers.append(x[i+1])
print(f'Элементы с одинаковым знаком {pair_of_numbers[0], pair_of_numbers[1]}')
