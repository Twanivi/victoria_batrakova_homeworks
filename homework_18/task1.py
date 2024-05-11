# 1)
# Экземляр класса задается тройкой координат в трехмерном пространстве (x,y,z).
# Обязательно должны быть реализованы методы:
# – сложение векторов оператором `+` (метод __add__),
# – вычитание векторов оператором `-` (метод __sub__),
# – скалярное произведение оператором `*` (метод __mul__),
# – умножение на скаляр оператором `*` (метод __mul__),
# – векторное произведение оператором `@` (метод __matmul__)
# метод read - считывает координаты с клавиатуры
# метод display - Выводит на экран координаты
# Пример
# v1 = Vector3D(4, 1, 2)
# v1.display()
# v2 = Vector3D()
# v2.read()
# v3 = Vector3D(1, 2, 3)
# v4 = v1 + v2
# v4.display()
# a = v4 * v3
# print(a)
# v4 = v1 * 10
# v4.display()
# v4 = v1 @ v3
# v4.display()

class Vector3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


    def read(self):
        self.x = int(input('Введите значение x: '))
        self.y = int(input('Введите значение y: '))
        self.z = int(input('Введите значение x: '))

    def display(self):
        print(f"Координаты - {self.x}, {self.y}, {self.z}")

    def __add__(self, rhs):
        if isinstance(rhs, Vector3D):
            return Vector3D((self.x + rhs.x), (self.y + rhs.y), (self.z + rhs.z))
        else:
            raise ValueError
    def __sub__(self, rhs):
        if isinstance(rhs, Vector3D):
            return Vector3D((self.x - rhs.x), (self.y - rhs.y), (self.z - rhs.z))
        else:
            raise ValueError

    def __mul__(self, rhs):
        if isinstance(rhs, Vector3D):
            return self.x * rhs.x + self.y * rhs.y + self.z * rhs.z
        else:
            return Vector3D(self.x * rhs, self.y * rhs, self.z * rhs)

    def __matmul__(self, rhs):
        if isinstance(rhs, Vector3D):
            return Vector3D(self.x * rhs.x + self.y * rhs.y + self.z * rhs.z)
        else:
            return Vector3D(self.x * rhs, self.y * rhs, self.z * rhs)


v1 = Vector3D(4, 1, 2)
v1.display()
v2 = Vector3D()
v2.read()
v3 = Vector3D(1, 2, 3)
v4 = v1 + v2
v4.display()
a = v4 * v3
print(a)
v4 = v1 * 10
v4.display()
v4 = v1 @ v3
v4.display()