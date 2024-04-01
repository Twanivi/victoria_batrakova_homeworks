# 7) Создать множество. Создать неизменяемое множество. Выполнить операцию объединения
# созданных множеств. Выполнить операцию пересечения созданных множеств.

set1 = {i ** 2 for i in range(10)}
for_froze = ('no change', 4, 0)
set2 = frozenset(for_froze)
set3 = set()
set4 = set()
print(set1)
print(set2)
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)
