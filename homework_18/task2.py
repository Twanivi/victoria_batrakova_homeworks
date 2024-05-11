# 2) Класс «Прямоугольный треугольник»
# Класс содержит два действительных числа – стороны треугольника. и включает
# следующие методы:
# увеличение/уменьшение размера стороны на заданное количество процентов;
# вычисление радиуса описанной окружности,
# вычисление периметра,
# определение значений углов.
import math


class RightTriangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.side3 = math.sqrt(self.side1 ** 2 + self.side2 ** 2)

    def increase_side(self, percent):
        self.side1 *= 1 + percent / 100
        self.side2 *= 1 + percent / 100

    def decrease_side(self, percent):
        self.side1 *= 1 - percent / 100
        self.side2 *= 1 - percent / 100

    def radius_of_circumscribed_circle(self):
        radius = math.sqrt(self.side1 ** 2 + self.side2 ** 2) / 2
        return round(radius, 2)

    def perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3

        return round(perimeter, 2)

    def angles(self):
        angle1 = math.degrees(math.atan(self.side1 / self.side2))
        angle2 = math.degrees(math.atan(self.side2 / self.side1))
        angle3 = 90
        return round(angle1), round(angle2), angle3


side1 = int(input('Введите значение первой стороны: '))
side2 = int(input('Введите значение второй стороны: '))
triangle = RightTriangle(side1, side2)
print(f'Периметр треугольника: {triangle.perimeter()}')
print(f'Радиус описанной окружности: {triangle.radius_of_circumscribed_circle()}')
angle1, angle2, angle3 = triangle.angles()
print(f'Значения углов треугольника: a = {angle1}, b = {angle2}, c = {angle3}')
percent_plus = int(input('Введите на сколько процентов увеличить стороны треугольника: '))
triangle.increase_side(percent_plus)
print(f'Новое значение периметра треугольника: {triangle.perimeter()}')
percent_minus = int(input('Введите на сколько процентов уменьшить стороны треугольника: '))
triangle.decrease_side(percent_minus)
print(f'Новое значение периметра треугольника: {triangle.perimeter()}')
