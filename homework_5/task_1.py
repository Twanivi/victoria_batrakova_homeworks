# 1)Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное,
# то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

list = [15, 48, 'hello', 6, 19, 'world']
vowels_hello = 0
consonants_hello = 0
vowels_world = 0
consonants_world = 0

for i in range(len(list)):
    if type(list[i]) == int:
        if list[i] % 2 == 0:
            a = list[i] // 10
            b = list[i] % 10
            print(f'сумма четного числа: {a + b}')
        else:
            list[i] = 1
print(list)

for i in list[2]:
    if i == 'a' or i == 'o' or i == 'u' or i == 'e' or i == 'i':
        vowels_hello += 1
    else:
        consonants_hello +=1
print(f'В слове "hello" {vowels_hello} гласных и {consonants_hello} согласных')

for i in list[-1]:
    if i == 'a' or i == 'o' or i == 'u' or i == 'e' or i == 'i':
        vowels_world += 1
    else:
        consonants_world +=1
print(f'В слове "world" {vowels_world} гласных и {consonants_world} согласных')
