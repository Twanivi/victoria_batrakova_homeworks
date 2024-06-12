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

class Vehicle:
    id = 1
    @classmethod
    def counter(cls):
        cls.id = Vehicle.id
        Vehicle.id += 1

    def __new__(cls, *args, **kwargs):
        cls.counter()
        return super().__new__(cls)

class CarMan(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self):
        object_id_collector = self.id


class CarCommander(Vehicle):
    def __init__(self):
        object_id_collector = self.id


class CarGunner(Vehicle):
    def __init__(self):
        object_id_collector = self.id


def check_object_id_collector():
    expected_ids = (1, 2, 3, 4, 5)
    actual_ids = (CarGunner().id, CarGunner().id, Car().id, CarCommander().id, Car().id)
    assert actual_ids == expected_ids, 'Expected_ids: {}. Actual_ids: {}.'.format(expected_ids, actual_ids)
    print('Test passed. Amazing job!')


check_object_id_collector()



