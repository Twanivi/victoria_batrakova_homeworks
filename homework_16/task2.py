# 2) Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента.
# Класс студен описан следующим образом:
#
# class Student:
#     def __init__(self, name, money):
#        self.name = name
#        self.money = money

class Student:
    def __init__(self, name, money):
       self.name = name
       self.money = money

    def student_money(self):
        print(f'У студента {self.name} - {self.money} рублей')


student1 = Student('Иванов', 1500)
student1.student_money()
student2 = Student('Петров', 1300)
student2.student_money()
student3 = Student('Козлова', 1000)
student3.student_money()
