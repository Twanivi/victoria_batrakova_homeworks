# 4) Разделить строку “Apples, Oranges, Pears, Bananas, Berries” по запятым и
# вывести на экран. Затем объединить элементы с использованием пробела,
# чтобы программа вывела “Apples Oranges Pears Bananas Berries”.

str_base = 'Apples, Oranges, Pears, Bananas, Berries'
str_split = str_base.split(', ')
print(str_split)
str_join = ' '.join(str_split)
print(str_join)
