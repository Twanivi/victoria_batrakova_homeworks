# 3) Создать 4 фрукта.
# Апельсин, яблоко, мандарин, банан
# У всех фруктов есть сорт, список витаминов, цена, имя
# У апельсина, мандарина, банана есть метод очистить
# У яблока метод порезать
# У банана есть характеристика: кол-во калия
# Создать 4 объекта фрукта и использовать все доступные методы и характеристики
# При вызове метода очистить, должно писаться имя фрукта
# Например:
# `apple = Apple("sort", [a,b,c], 120, "apple")`
#
# `apple.clear()`
#
# `>>"apple очищен"`

class Fruit:
    def __init__(self, sort, vitamins, cost, name):
        self.sort = sort
        self.vitamins = vitamins
        self.cost = cost
        self.name = name

    def clear(self):
        return f'{self.name} был очищен'

class Apple(Fruit):
    def cut(self):
        return f'{self.name} было порезано'

class Banana(Fruit):
    def __init__(self, sort, vitamins, cost, name, potassium):
        super().__init__(sort, vitamins, cost, name)
        self.potassium = potassium


apple = Apple('Голден Делишес', ['B1', 'B2', 'B3 (PP)', 'B4', 'B5', 'B6', 'B9'], 120, 'Яблоко')
print(apple.name, apple.sort, apple.vitamins, apple.cost)
print(apple.cut())
orange = Fruit('Washington Navel', [ 'А', 'group В', 'group D', 'group Р'], 130, 'Апельсин')
print(orange.name, orange.sort, orange.vitamins, orange.cost)
print(orange.clear())
mandarin = Fruit('Клементин', [ 'C', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B9'], 125, 'Мандарин')
print(mandarin.name, mandarin.sort, mandarin.vitamins, mandarin.cost)
print(mandarin.clear())
banana = Banana( 'Giant Cavendish', ['C', 'A', 'B1'], 100, 'Банан', 20)
print(banana.name, banana.sort, banana.vitamins, banana.cost, banana.potassium)
print(banana.clear())
