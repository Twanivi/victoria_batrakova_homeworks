# 4) На вход программы подается словарь a = {1:10, 2:20, 3:30},
# необходимо получить список произведения ключа на значение.

a = {1:10, 2:20, 3:30}
new_list = []
for key, value in a.items():
    new_list.append(key * value)
print(new_list)
