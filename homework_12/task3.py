# 3) Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число - кол-во нечётных цифр.
# Строка - количество букв.
# Сделать проверку со всеми этими


def type_of_result(result):
    if isinstance(result, tuple):
        return sum([len(i) for i in result])
    elif isinstance(result, list):
        list1 = []
        new_str = ''
        for i in result:
            if str(i).isalpha() or str(i).isdigit():
                list1.append(str(i))
        new_str = ''.join(list1)
        return len(new_str)
    elif isinstance(result, int):
        return len([i for i in str(result) if i in '13579'])
    elif isinstance(result, str):
        return len(result)
    else:
        return 'Неопределенный тип данных'


print(type_of_result(('thyjt', 'оорнфва', 'ELKJHJK')))
print(type_of_result([5, 10, 'rtyy45$%^', 'eryy', 555]))
print(type_of_result(22578))
print(type_of_result('ukythsfa'))
print(type_of_result(None))
