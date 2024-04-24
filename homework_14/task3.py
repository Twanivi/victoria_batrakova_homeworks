# 3) В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить
# количество в ней символов.

with open('text_task2-3.txt', encoding='utf-8') as file:
    line = file.readlines()
    line = [i.rstrip() for i in line]
    print(line)
    print(f'Количество строк: {len(line)}')
    for i in line:
        print(f'Количество элементов в строке: {len(i)}')
