# 2) Создайте класс Робот
#     создайте 2 типа оружия: меч, автомат
#     Создайте 2 типа амуниции: броня, шлем
#     Добавьте оружию и амуниции свои характеристики(например урон, прочность)
#     Создайте своего робота с каким либо оружием
#     (может быть несколько и брони может быть несколько. Так же может быть ничего)
#     Выведите весь арсенал робота на экран

class Robot:
    def __init__(self, name, weapons, ammunitions):
        self.name = name
        self.weapons = weapons
        self.ammunitions = ammunitions


class Ammunition:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


class Weapons:
    def __init__(self, name, damage, strength):
        self.name = name
        self.damage = damage
        self.strength = strength



armor = Ammunition('Armor', 50)
helmet = Ammunition('Helmet', 25)
sword = Weapons('Sword', 20, 40)
automate = Weapons('Automate', 40, 30)
robot1 = Robot('My robot', [sword], [armor, helmet] )
print(f'Робот {robot1.name} в арсенале имеет: ')
for weapon in robot1.weapons:
    print(f'{weapon.name}: урон = {weapon.damage}, прочность = {weapon.strength}')
for ammunition in robot1.ammunitions:
    print(f'{ammunition.name}: прочность = {ammunition.strength}')

