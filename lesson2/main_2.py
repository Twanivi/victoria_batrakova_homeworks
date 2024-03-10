# сложение
name = 'Victoria'
element = 'hello '
print(element + name)
# print(element + ' ' + name)

# умножение строк
city = 'Minsk'
print(city * 5)
print(len(city))

x = 'hello world'
print(len(x))
print(x[0])
print(x[-1])
print(x[0:5])
print(x[:5])
print(x[:5:1])
print(x[:5:2])
print(x[-1:-12:-1])
print(x[::-1])
print(x[3:5:4])


x = 'hello my name is Petya'
# 1) my
# 2) name is Petya
# 3) P
# 4) is hello
# 5) ll
# 6) _name_
# 7) перевернуть строку
# 8) si ym eman

result_1 = x[6:8]
print(result_1)
result_2 = x[9:]
print(result_2)
result_3 = x[-5]
print(result_3)
result_4 = x[-8:-5] + x[:5]
print(result_4)
result_5 = x[2:4]
print(result_5)
result_6 = x[8:14]
print(result_6)
result_7 = x[::-1]
print(result_7)
result_8 = x[-7:-9:-1] + x[-14:-17:-1] + x[-9:-14:-1]
print(result_8)

# При заданном целом числе n посчитайте n + nn + nnn
n = int(input('Введите число: '))
n_str = str(n)
nn_str = n_str * 2
nnn_str = n_str * 3
result = n + int(nn_str) + int(nnn_str)
print('Итого: ', result)
