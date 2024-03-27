# 4) Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс
# этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.

import random
x = [random.randint(1, 100) for i in range(10)]
print(x)
index_of_max = 0

for i in range(1, len(x)):
    if x[i] > x[index_of_max]:
        index_of_max = i
print(f'Наибольший элемент списка: {x[index_of_max]} с индексом {index_of_max}')
