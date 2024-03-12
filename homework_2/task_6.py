# 6) Напиши программу, которая принимает строку от пользователя и выводит
# все слова этой строки в обратном порядке

text = input('Введите текст: ')
# print(text[::-1])
text_split = text.split()
text_split.reverse()
text_join = ' '.join(text_split)
print(text_join)