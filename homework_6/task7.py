# 7) Вася начал тренироваться бегать. В первый день день он пробежал 1 км.
# Каждый последующий день он увеличивал пройденное расстояние на 10% от предыдущего дня.
# Сколько дней Васе понадобится, чтобы пробежать в сумме хотя бы 10 км?

distance_of_one_day = 1
distance = 10
day = 1
add_distance = 0.1

while distance_of_one_day <= distance:
    distance_of_one_day += add_distance
    day += 1
    add_distance += 0.1
print(f'На {day} день пробег спортсмена составит {distance_of_one_day} км')

