# 2) Создать текстовый файл, записать в него построчно
# данные, которые вводит пользователь. Окончанием ввода
# пусть служит пустая строка

with open('text_task2-3.txt', 'w') as file:
    print('Для завершения введите пустую строку')
    while True:
        input_text = input('Введите текст: ')
        if input_text == '':
            break
        file.write(input_text + '\n')