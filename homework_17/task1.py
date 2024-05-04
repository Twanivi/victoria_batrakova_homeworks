# 1) Создайте класс Students, содержащий поля:
# фамилия и инициалы,
# номер группы,
# успеваемость (список из пяти элементов).
#
# Создать класс School:
#
# Добавить возможность для добавления студентов в школу
#
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
#
# Добавить возможность вывода учеников заданной группы
#
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)

class Students:
    def __init__(self, surname, number_of_group, progress):
        self.surname = surname
        self.number_of_group = number_of_group
        self.progress = progress


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def numbers_5_or_6(self):
        for student in self.students:
            if all(rating in [5, 6] for rating in student.progress):
                print(f'Студент {student.surname} группы №{student.number_of_group} имеет оценки 5 или 6')

    def students_of_group(self, number_of_groupe):
        for student in self.students:
            if student.number_of_group == number_of_groupe:
                print(f'Студент группы {number_of_groupe}: {student.surname}')

    def automatic_pass(self):
        for student in self.students:
            if (sum(student.progress) / len(student.progress)) >= 7:
                print(f'Студент {student.surname} получает автомат')


school = School()
student1 = Students('Иванов И.И.', 2, [6, 5, 5, 6, 6])
student2 = Students('Петров П.П.', 1, [6, 7, 6, 7, 8])
student3 = Students('Козлова А.А.', 1, [5, 6, 9, 8, 8])
student4 = Students('Уварова И.У.', 2, [3, 4, 5, 3, 3])
student5 = Students('Миронов О.О.', 2, [9, 8, 8, 9, 9])
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)
school.add_student(student4)
school.add_student(student5)

school.numbers_5_or_6()
number_of_group = int(input('Введите номер группы: '))
school.students_of_group(number_of_group)
school.automatic_pass()
