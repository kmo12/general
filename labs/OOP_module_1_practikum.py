# Создайте класс Point, который описывает точку с координатами x и y

# В классе необходимо описать:
#
# Конструктор, который принимает в качестве параметров значение для координат x и y
# Метод move_to, который принимает в качестве параметров новые значения для координат x и y
# Метод move_by, принимает в качестве параметров новые значения для координат x и y, относительно текущих значений
# Свойство для изменения и получения значений координат x и y
#
#
# Необходимое условия, которые надо учесть:
#
# При приведении объекта к строке должна возвращаться строка
#  "Я - точка: координата_х х координата_у"
#
#
# Как должно работать:
#     point = Point(10, 20)
#     print(point)  # Я - точка: 10 х 20
#
#     point.move_to(100, 200)
#     print(point.x, " : ", point.y)  # 100 : 200
#
#     point.move_by(10, 20)
#     print(point.x, " : ", point.y)  # 110 : 220
#
#     point.x = 30
#     point.y = 40
#     print(point)  # Я - точка: 30 х 40


class Point(object):
    __counter = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.__counter += 1

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x
    x = property(get_x, set_x)

    # getter
    @property
    def y(self):
        return self.__y

    # setter
    @y.setter
    def y(self, y):
        self.__y = y

    # getter
    @property
    def counter(self):
        return self.__counter

    def __repr__(self):
        return f"Я - точка: {self.__x} x {self.__y}"

    def move_to(self, x, y):
        self.__x = x
        self.__y = y

    def move_by(self, x, y):
        self.__x += x
        self.__y += y


# print(getattr(Point, "x").fget)

# point = Point(1, 5)
# print(point)
#
# point.y = 20
# point.x = 10
#
# print(point)
#
# point.move_to(100, 200)
# print(point)
#
# point.move_by(10, 20)
# print(point.x, " : ", point.y)
#
# point2 = Point(1000, 30)
# print(point2)
# print(point2.counter)