# 2) Создайте словарь d = {'1': 0, ‘2’: 0, '3': 0} тремя способами.
# Выведите полученный словарь на экран
    # 1 способ
d = {str(key): key * 0 for key in range(1, 4)}
print(d)

    # 2 способ
d = dict([('1', 0), ('2', 0), ('3', 0)])
print(d)

    # 3 способ
d = dict.fromkeys(['1', '2', '3'], 0)
print(d)
