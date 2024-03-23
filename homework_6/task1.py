# 1) Казино. Компьютер генерирует числа от 1 до 10 и от 1 до двух соответственно.
# Цифры от 1 до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный, 2-черный).
# Пользователю дается 5 попыток угадать номер и цвет(Пример. Вводим с клавиатуры: 3 красный)
# В случае неудачи, вывести на экран правильную комбинацию.

from random import randint
start = True
chance = 0
while start:
    number_of_guess = randint(1, 11)
    number_of_color = randint(1, 3)
    number_from_user = int(input('Угадайте число от 1 до 10: '))
    color_from_user = input('Угадайте цвет (красный или чёрный): ')
    chance += 1
    if number_of_color == 2:
        number_of_color = 'черный'
    else:
        number_of_color = 'красный'
    if number_of_guess == number_from_user and number_of_color == color_from_user.lower():
        print(f'Поздравляем, Вы угадали. Загаданное число было {number_of_guess}, а цвет {number_of_color}')
        start = False
    else:
        print(f'Вы не угадали. Загаданное число было {number_of_guess}, а цвет {number_of_color}')
    if chance == 5:
        break
        print(f'Вы использовали все попытки')

