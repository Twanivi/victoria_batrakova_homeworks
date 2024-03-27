# 6) В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент
# этого списка.

import random
x = [random.randint(1, 100) for i in range(10)]
print(x)

index_of_min = 0
index_of_max = 0
for i in range(1, len(x)):
    if x[i] > x[index_of_max]:
        index_of_max = i
    if x[i] < x[index_of_min]:
        index_of_min = i
x[index_of_min], x[index_of_max] = x[index_of_max], x[index_of_min]
print(x)
