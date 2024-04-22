# 2)На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список,
# в котором содержатся только те числа, которые больше 5 по модулю.
def more_than_five(lst):
    new_list = list(filter(lambda x: (abs(x) > 5), lst))
    return new_list

print(more_than_five([-11, 4, -2, 90, 400, 0, -5]))
