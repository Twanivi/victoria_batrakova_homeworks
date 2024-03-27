# 3) Дан список чисел. Определите, сколько в этом списке элементов, которые больше
# двух своих соседей, и выведите количество таких элементов. Крайние элементы
# списка никогда не учитываются, поскольку у них недостаточно соседей.

import random
x = [random.randint(-100, 100) for i in range(10)]
print(x)
biggest_numbers = 0
for i in range(1, len(x) - 1):
    if x[i - 1] < x[i] and x[i] > x[i + 1]:
        biggest_numbers += 1
print(biggest_numbers)