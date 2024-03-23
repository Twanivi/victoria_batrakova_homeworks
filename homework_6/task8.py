# 8)Необходимо с помощью цикла while вывести данную последовательность чисел:
# 1 2 4 16 32 64 128 256 512

list1 = []
number = 1
while number <= 512:
    print(number)
    list1.append(number)
    if number == 1:
        number += 1
    else:
        number *= 2
