# 2) Файл содержит числа и буквы. Каждый записан в отдельной строке. Нужно считать содержимое в список так,
# чтобы сначала шли числа по возрастанию, а потом слова по возрастанию их длины.

with open('text_task1.txt') as file:
     line = file.read().splitlines()
     print(line)
     numbers = []
     letters = []
     for i in line:
        if i.isdigit():
            numbers.append(int(i))
        elif i.isalpha():
            letters.append(i)
numbers.sort()
letters.sort(key=len)
numbers.extend(letters)
print(numbers)
