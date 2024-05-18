# Практическая часть:
#
# 1) Требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого создайте класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
#     - Ура, можно построить треугольник!
#     - С отрицательными числами ничего не выйдет!
#     - Жаль, но из этого треугольник не сделать.

class TriangleChecker:

    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a < 0 or self.b < 0 or self.c < 0:
            raise ValueError('С отрицательными числами ничего не выйдет!')
        elif (self.a and self.b and self.c) < 3:
            raise ValueError('Жаль, но из этого треугольник не сделать')
        else:
            return 'Ура, можно построить треугольник!'


triangle = TriangleChecker(4, 8, 6)
print(triangle.is_triangle())
triangle2 = TriangleChecker(0, 1, 1)
print(triangle2.is_triangle())
triangle4 = TriangleChecker(44, -8, 6)
print(triangle4.is_triangle())

# 2) Задача
#
#     Есть Помидор со следующими характеристиками:
#         1. Индекс
#         2. Стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный)
#     Помидор может:
#         1. Расти (переходить на следующую стадию созревания)
#         2. Предоставлять информацию о своей зрелости
#     Есть Куст с помидорами, который:
#         1. Содержит список томатов, которые на ней растут
#     И может:
#         1. Расти вместе с томатами
#         2. Предоставлять информацию о зрелости всех томатов
#         3. Предоставлять урожай
#     И также есть Садовник, который имеет:
#         1. Имя
#         2. Растение, за которым он ухаживает
#     И может:
#         1. Ухаживать за растением
#         2. Собирать с него урожай
#
# Задание:
#
#     Класс Tomato
#         1. Создайте класс Tomato
#         2. Создайте статический атрибут states, который будет содержать все стадии созревания помидора
#         3. Создайте метод __init__(), внутри которого будут определены два приватных атрибута:
#            1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
#         4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
#         5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
#
#     Класс TomatoBush
#         1. Создайте класс TomatoBush
#         2. Определите метод __init__(), который будет принимать в качестве параметра количество томатов
#            и на его основе будет создавать список объектов класса Tomato.
#            Данный список будет храниться внутри атрибута tomatoes.
#         3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап
#            созревания
#         4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
#         5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
#
#     Класс Gardener
#         1. Создайте класс Gardener
#         2. Создайте метод __init__(), внутри которого будут определены два атрибута: 1) name - передается параметром,
#            является публичным и 2) _plant - принимает объект класса TomatoBush, является приватным
#         3. Создайте метод work(), который заставляет садовника работать,
#            что позволяет растению становиться более зрелым
#         4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
#            Если нет - метод печатает предупреждение.
#         5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.
#
#     Тесты (main)
#         1. Вызовите справку по садоводству
#         2. Создайте объекты классов TomatoBush и Gardener
#         3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
#         4. Попробуйте собрать урожай
#         5. Если томаты еще не дозрели, продолжайте ухаживать за ними
#         6. Соберите урожай

class Tomato:

    states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}
    def __init__(self, index):
        self._index = index
        self._state = self.states['Отсутствует']

    def grow(self):
        if self._state < 3:
            self._state += 1
    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False

class TomatoBush:

    def __init__(self, count):
        self.tomatoes = [Tomato(index) for index in range(1, count + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print('Урожай собран!')
            self._plant.give_away_all()
        else:
            print('Томаты еще не созрели')

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству:')
        print('1. Не забывайте регулярно поливать и подкармливать растения')
        print('2. Определите правильное расстояние между растениями, чтобы они не мешали друг другу в росте')
        print('3. Удалите поврежденные листья и плоды, чтобы предотвратить распространение болезней')


Gardener.knowledge_base()

bush = TomatoBush(4)
gardener = Gardener('Lola', bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()

#
# 3) Создайте систему управления банковскими счетами, которая позволяет создавать,
#    управлять и выполнять операции с банковскими счетами различных клиентов.
#     1. Реализуйте класс Client, представляющий клиента банка. Класс должен иметь атрибуты name (имя клиента) и
#        id (уникальный идентификатор клиента).
#     2. Реализуйте класс BankAccount, представляющий банковский счет.
#        Класс должен иметь атрибуты account_number (номер счета), balance (баланс счета) и
#        client (объект типа Client, которому принадлежит счет). Класс также должен иметь методы deposit(amount) и
#        withdraw(amount), которые позволяют пополнить или снять деньги со счета.
#     3. Реализуйте класс Bank, представляющий банк. Класс должен иметь атрибут accounts, который является словарем,
#        где ключами являются номера счетов, а значениями - объекты типа BankAccount.
#        Класс также должен иметь методы create_account(client, initial_balance) для создания нового счета и
#        get_account(account_number) для получения счета по его номеру.
#     4. Добавьте в класс Bank методы для выполнения переводов между счетами
#        (transfer(sender_account, receiver_account, amount)), а также для получения общего баланса клиента
#        (get_total_balance(client)), который включает сумму денег на всех его счетах.
#     5. Реализуйте обработку ошибок, например, недостаточно средств на счете при снятии денег или
#        отсутствие счета при переводе.
#

                   # Не получилось решить :(
class Client:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class BankAccount:
    client = Client(name, id)
    def __init__(self, client, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
        self.client = client

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            ValueError('Insufficient balance')

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, client, initial_balance):
        self.account_number = len(self.accounts) + 1
        new_account = BankAccount(client, initial_balance)
        self.accounts[self.account_number] = new_account
        return self.account_number

    def get_account(self, account_number):
        return self.accounts.get(self.account_number)

    def transfer(self, sender_account, receiver_account, amount):
        sender = self.get_account(sender_account)
        receiver = self.get_account(receiver_account)
        if sender and receiver:
            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                return True
            else:
                return ValueError('Insufficient balance')
        else:
            return ValueError('account not found')


    def get_total_balance(self, client):
        total_balance = 0
        for account in self.accounts.values():
            if account.client == client:
                total_balance += account.balance
            return total_balance

#
# 4) Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
#    По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов:
#    getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
#    Метод getName нужен для получения данных об имени конкретного студента,
#    метод getAge нужен для получения данных о возрасте конкретного студента,
#    метод setGroupNumberнужен для получения данных о номере группы конкретного студента.
#    Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию,
#    метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
#    В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.

class Student:
    def __init__(self, name='Ivan', age=18, groupNumber='10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self):
        self.name = self.name
        self.age = self.age
        return f'Имя студента - {self.name}, возраст студента - {self.age}'

    def setGroupNumber(self):
        self.groupNumber = self.groupNumber
        return f'группа студента - {self.groupNumber}'


student1 = Student('Lilit', 18, '10B')
student2 = Student()
student3 = Student('Nicolay', 20, '10A')
student4 = Student('Misha', 19, '10B')
student5 = Student('Sara', 21, '10A')
print(student1.setNameAge(), student1.setGroupNumber())
print(student2.setNameAge(), student2.setGroupNumber())
print(student3.setNameAge(), student3.setGroupNumber())
print(student4.setNameAge(), student4.setGroupNumber())
print(student5.setNameAge(), student5.setGroupNumber())
#
# 5) Класс «Волшебник» (Wizard)
# Экземпляр класса при инициализации принимает аргументы:
# – имя;
# – рейтинг;
# – на какой возраст выглядит.
# Класс должен обеспечивать функциональность:
# – change_rating(value) – изменять рейтинг на значение value; не может стать больше 100 и
# меньше 1, изменяется только до достижения экстремального значения; при увеличении
# рейтинга уменьшается возраст на abs(value) // 10, но только до 18, дальше не уменьшается;
# при уменьшении рейтинга возраст соответственно увеличивается;
# – к экземпляру класса можно прибавить строку: (wd += string), значение рейтинга
# увеличивается на ее длину, а возраст, соответственно, уменьшается на длину // 10, условия
# изменения такие же;
# – экземпляр класса можно вызвать с аргументом-числом; возвращает значение: (аргумент
# - возраст) * рейтинг;
# __str__() – возвращает строку:
# “Wizard <name> with <rating> rating looks <age> years old”
# – экземпляры класса можно сравнивать: сначала по рейтингу, затем по возрасту, затем по
# имени по алфавиту; для этого нужно реализовать методы сравнения: <, >, <=, >=, ==, !=.

class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, value):
        if self.rating + value < 100:
            self.rating += value
            if self.age > 18:
                self.age = abs(value) // 10
            else:
                self.age = 18
        elif self.rating - value > 1:
            self.rating -= value
            self.age = abs(value) * 10
        else:
            ValueError('Вы достигли экстремального значения')

    def __add__(self, string):
        if self.rating + len(string) < 100:
            self.rating += len(string)
            if self.age > 18:
                self.age = len(string) // 10
            else:
                self.age = 18
        else:
            ValueError('Вы достигли экстремального значения')

    def __call__(self, argument):
        return (argument - self.age) * self.rating


    def __str__(self):
        return f'Wizard {self.name} with {self.rating} rating looks {self.age} years old'

    def __lt__(self, other):
        return (self.rating, self.age, self.name) < (other.rating, other.age, other.name)


wd = Wizard("Gideon", 37, 20)
wd.change_rating(10)
print(wd)
wd + 'hello'
print(wd)
print(wd(50))

wd2 = Wizard("Lucius", 64, 18)
wd3 = Wizard("Merlin", 99, 25)
print(wd2 < wd3, wd2 > wd3)
print(wd2, wd3, sep='\n')
#

# 6) Класс «Сотрудник компании» Worker
# Экземпляр класса при инициализации принимает аргументы: имя, должность и стаж работы сотрудника,
# метод print_info() выводит информацию о сотруднике в формате: «Имя: Василий Должность: Системный администратор
# Стаж: 3 года» При выводе стажа нужно учитывать, что «года» должно заменяться на «лет» или «год» в зависимости от числа.
# worker1 = Worker("Алексей", "Программист", 17)
# worker1.print_info()
# worker2 = Worker("Анна", "Маркетолог", 2)
# worker2.print_info()
# worker3 = Worker("Дмитрий", "Аналитик", 1)
# worker3.print_info()

class Worker:
    def __init__(self, name, position, work_experience):
        self.name = name
        self.position = position
        self.work_experience = work_experience

    def print_info(self):
        print(f'Имя: {self.name}.')
        print(f'Должность: {self.position}.')
        n = self.work_experience % 10
        nn = self.work_experience % 100 // 10
        year = 'лет'
        if nn != 1:
            if n == 1:
                year = 'год'
            elif n in [2, 3, 4]:
                year = 'года'
        print(f'Стаж: {self.work_experience} {year}.')


worker1 = Worker("Алексей", "Программист", 17)
worker1.print_info()
worker2 = Worker("Анна", "Маркетолог", 2)
worker2.print_info()
worker3 = Worker("Дмитрий", "Аналитик", 1)
worker3.print_info()
#
#
# 7) Класс ПЕРСОНА, экземпляр класса инициализируется аргументами фамилия, дата
# рождения и содержит методы, позволяющие вывести информацию о персоне, а также определить ее возраст.
# Дочерние классы: АБИТУРИЕНТ (фамилия, дата рождения, факультет),
# СТУДЕНТ(фамилия, дата рождения, факультет, курс), ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
# содержат свои методы вывода информации.
# Создайте список из n персон, выведите полную информацию из базы, а также
# организуйте поиск персон, чей возраст попадает в заданный диапазон.
#
from abc import ABC, abstractmethod


class Persona(ABC):

    def __init__(self, surname, age, faculty):
        self.surname = surname
        self.age = age
        self.faculty = faculty

    @abstractmethod
    def get_info(self):
        print('Информация о персоне...')

    def get_age(self):
        return self.age


class Abiturient(Persona):
    def __init__(self, surname, age, faculty):
        super().__init__(surname, age, faculty)
        self.faculty = faculty

    def get_info(self):
        return f'Абитуриент: {self.surname}\nДата рождения: {self.age}\nФакультет: {self.faculty}'


class Student(Persona):

    def __init__(self, surname, age, faculty, course):
        super().__init__(surname, age, faculty)
        self.course = course

    def get_info(self):
        return f'Студент: {self.surname}\nДата рождения: {self.age}\nФакультет: {self.faculty}\nКурс: {self.course}'


class Prepodavatel(Persona):

    def __init__(self, surname, age, faculty, position, experience):
        super().__init__(surname, age, faculty)
        self.faculty = faculty
        self.position = position
        self.experience = experience

    def get_info(self):
        return f'Преподаватель: {self.surname}\nДата рождения: {self.age}\nФакультет: {self.faculty}\nДолжность: {self.position}\nСтаж: {self.experience}'


persons = []

persons.append(Abiturient("Езерская", 2004, "программное обеспечние"))
persons.append(Student("Ивановская", 2004, "программное обеспечние", "4"))
persons.append(Prepodavatel("Романов", 1970, "Программное обеспечение", "Учитель", "30 лет"))

for person in persons:
    print(person.get_info())

left = int(input('Введите начало промежутка года рождения: '))
right = int(input("Введите конец промежутка года рождения: "))
print("Персоны, удовлетворяющие заданному условию: ")
for person in persons:
    if left <= person.get_age() <= right:
        print(f'Фамилия {person.surname}, Год рождения: {person.get_age()}')

#
#
# 8**) Шахматный король ходит по горизонтали, вертикали и диагонали,
#
#  но только на 1 клетку. Даны две различные клетки шахматной доски,
#
# определите, может ли король попасть с первой клетки на вторую одним ходом.
#
#
#  Пример
#  Cell 1 coordinates:
#  >>4, 4
#  Cell 2 coordinated:
#  >>5, 5
#  YES
#  Конь
#  Определите, может ли конь попасть с первой клетки на вторую одним ходом.
#  Ладья
#  Определите, может ли ладья попасть с первой клетки на вторую одним ходом.
#  Ферзь
#  Определите, может ли ферзь попасть с первой клетки на вторую одним ходом.
#  Слон
#  определите, может ли слон попасть с первой клетки на вторую одним ходом.

class Chess:


    def is_king_can_move(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2
        a1, b1 = self.cell1
        a2, b2 = self.cell2
        if abs(a1 - a2) <= 1 and abs(b1 - b2) <= 1:
            return 'Yes'
        else:
            return 'No'

    def is_rook_can_move(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2
        a1, b1 = self.cell1
        a2, b2 = self.cell2
        if a1 == a2 or b1 == b2:
            return 'Yes'
        else:
            return 'No'

    def is_elephant_can_move(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2
        a1, b1 = self.cell1
        a2, b2 = self.cell2
        if abs(a1 - a2) == abs(b1 - b2):
            return 'Yes'
        else:
            return 'No'

    def is_queen_can_move(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2
        a1, b1 = self.cell1
        a2, b2 = self.cell2
        if abs(a1 - a2) == abs(b1 - b2) or a1 == a2 or b1 == b2:
            return 'Yes'
        else:
            return 'No'

    def is_horse_can_move(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2
        a1, b1 = self.cell1
        a2, b2 = self.cell2
        da = abs(a1 - a2)
        db = abs(b1 - b2)
        if da == 1 and db == 2 or da == 2 and db == 1:
            return 'Yes'
        else:
            return 'No'


game_1 = Chess()
# Пример реализации
print('=======КОРОЛЬ=======')
print(game_1.is_king_can_move([2, 2], [2, 3]))
print(game_1.is_king_can_move([2, 2], [3, 2]))
print(game_1.is_king_can_move([2, 2], [3, 3]))
print(game_1.is_king_can_move([2, 2], [1, 1]))
print(game_1.is_king_can_move([2, 2], [2, 4]))
print(game_1.is_king_can_move([2, 2], [4, 4]))
print('=======ЛАДЬЯ=======')
print(game_1.is_rook_can_move([2, 2], [2, 5]))
print(game_1.is_rook_can_move([2, 2], [4, 2]))
print(game_1.is_rook_can_move([2, 2], [3, 3]))
print(game_1.is_rook_can_move([2, 2], [1, 4]))
print('=======СЛОН=======')
print(game_1.is_elephant_can_move([2, 2], [4, 4]))
print(game_1.is_elephant_can_move([2, 4], [3, 3]))
print(game_1.is_elephant_can_move([2, 3], [4, 1]))
print(game_1.is_elephant_can_move([2, 4], [4, 4]))
print(game_1.is_elephant_can_move([2, 2], [2, 5]))
print('=======ФЕРЗЬ=======')
print(game_1.is_queen_can_move([2, 3], [4, 5]))
print(game_1.is_queen_can_move([1, 3], [1, 1]))
print(game_1.is_queen_can_move([4, 4], [1, 4]))
print(game_1.is_queen_can_move([2, 2], [4, 3]))
print('=======КОНЬ========')
print(game_1.is_horse_can_move([1, 2], [3, 3]))
print(game_1.is_horse_can_move([4, 4], [2, 3]))
print(game_1.is_horse_can_move([3, 1], [1, 2]))
print(game_1.is_horse_can_move([4, 4], [2, 1]))
print(game_1.is_horse_can_move([3, 1], [1, 5]))