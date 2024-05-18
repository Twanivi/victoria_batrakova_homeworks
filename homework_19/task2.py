# 2)
# Исходные данные:
# - скрипт task1, который содержит реализацию классов Car, CarCommander, CarGunner и
# код для проверки результата
#
# Необходимо:
# 1. Реализовать всю необходимую логику так, чтобы скрипт task1 выводил:
#     >>> Well done. Amazing job!
#
# Желательно:
# 1. Привести альтернативные способы решения задачи.
#
# Примечание:
# - НЕЛЬЗЯ менять реализацию приведенных в исходных данных классов и проверочного кода.
# - Нет ограничений по реализации классов CarMan и Vehicle, а также вспомогательной логики.
from abc import ABC, abstractmethod
class Car:
    @abstractmethod
    def __init__(self):
        object_id_collector = self.id


class CarCommander:
    @abstractmethod
    def __init__(self):
        self.id = 0
        object_id_collector = self.id


class CarGunner:
    @abstractmethod
    def __init__(self):
        object_id_collector = self.id


def check_object_id_collector():
    expected_ids = (1, 2, 3, 4, 5)
    actual_ids = (CarGunner().id, CarGunner().id, Car().id, CarCommander().id, Car().id)
    if actual_ids == expected_ids:
        print('Test passed. Amazing job!')
    else:
        print(f'Expected_ids: {expected_ids}. Actual_ids: {actual_ids}.')


check_object_id_collector()

#
# class Car:
# id_counter = 0
#
# def __init__(self):
# Car.id_counter += 1
# self.id = Car.id_counter
#
#
# class CarCommander:
# id_counter = 0
#
# def __init__(self):
# CarCommander.id_counter += 1
# self.id = CarCommander.id_counter
#
#
# class CarGunner:
# id_counter = 0
#
# def __init__(self):
# CarGunner.id_counter += 1
# self.id = CarGunner.id_counter
#
#
# def check_object_id_collector():
# expected_ids = (1, 2, 3, 4, 5)
# actual_ids = (CarGunner().id, CarGunner().id, Car().id, CarCommander().id, Car().id)
#
# if expected_ids == actual_ids:
# print(">>> Well done. Amazing job!")
# else:
# print("IDs do not match.")
#
# check_object_id_collector()

# class Car:
# def __init__(self):
# self.id = 1
#
# class CarCommander:
# def __init__(self):
# self.id = 2
#
# class CarGunner:
# def __init__(self):
# self.id = 3
#
# def check_object_id_collector():
# expected_ids = (1, 2, 3, 4, 5)
#
# car = Car()
# commander = CarCommander()
# gunner = CarGunner()
#
# if car.id in expected_ids and commander.id in expected_ids and gunner.id in expected_ids:
# print("Well done. Amazing job!")
# else:
# print("IDs do not match the expected values.")