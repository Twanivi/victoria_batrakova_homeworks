# 1) Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
import random
x = [random.randint(1, 100) for i in range(10)]
print(x)

y = []
for i in range(len(x) - 1):
    n = x[i]
    i += 1
    m = x[i]
    if m > n:
        y.append(m)
print(f'Элементы списка, которые больше предыдущего элемента: {y}')
