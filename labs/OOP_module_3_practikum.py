# # Модуль 2. Практическая работа

# ## Игра с геометрическими фигурами

# Создайте классы Circle, Rectangle и Square, которые реализуют интерфейс IShape
# Создайте класс Game, который описывает логику игры (singleton class)

# В классах Circle, Rectangle и Square необходимо описать:
#   конструктор, который принимает в качестве параметров необходимые значения. Для Круга таковым является радиус,
#    для Прямоугольника - размеры двух его сторон, для Квадрата - размер сторон.
#   методы, которые определены в интерфейсе IShape
#   метод get_description должен возвращать произвольную строку вида Я - имя_фигуры параметры

# В классе Game необходимо описать логику игру:
#
#   Пользователю называется количество геометрических фигур участвующих в игре
#   Пользователю предлагается начать игру. В случае отказа, печатается строка Спасибо за участие!
#   Случайным образом создаётся объект - экземпляр одного из классов
#   Созданному объекту в конструктор передаются необходимые параметры со случайными значениями
#   Пользователю по очереди задаются вопросы касающиеся площади и периметра фигуры, на которые он должен ответить
#   В зависимости от правильности ответа пользователя печатается строка Правильно! или Ошибка! с правильным ответом
#   После каждой пары вопросов пользователю предлагается продолжить игру

# Как это должно работать
#
#   >>> Привет! Мы геометрические фигуры и у нас есть 2 вопроса.
#   >>> Играем? Y/N: y
#   >>> Я - окружность с радиусом 7
#   >>> Укажите мою площадь: 153.86
#   >>> Правильно!
#   >>> Укажите мой периметр: 100
#   >>> Ошибка! Правильный ответ: 43.96
#   >>> Играем? Y/N: y
#   >>> Я - прямоугольник со сторонами 7 и 1
#   >>> Укажите мою площадь: 7
#   >>> Правильно!
#   >>> Укажите мой периметр: 16
#   >>> Правильно!
#   >>> Играем? Y/N: n
#   >>> Спасибо за участие!

import abc

from random import randint, choice
from math import pi


class IShape(abc.ABC):
    """Интерфейс для реализации геометрических фигур"""

    @abc.abstractmethod
    def get_perimeter(self):
        """Возвращает периметр фигуры"""
        pass

    @abc.abstractmethod
    def get_area(self):
        """Возвращает площадь фигуры"""
        pass

    @abc.abstractmethod
    def get_description(self):
        """Возвращает произвольное описание фигуры"""
        pass


class Circle(IShape):
    def __init__(self):
        self.__radius = randint(1, 10)
        self.__name = "Круг"

    @property
    def radius(self):
        return self.__radius

    def get_perimeter(self):
        """Возвращает периметр фигуры"""
        return 2 * pi * self.radius

    def get_area(self):
        """Возвращает площадь фигуры"""
        return 2 * pi * (self.radius * self.radius)

    def get_description(self):
        """Возвращает произвольное описание фигуры"""
        return f"Я - {self.__name}, параметры: r = {self.radius}"


class Rectangle(IShape):
    def __init__(self):
        self.__a = randint(1, 10)
        self.__b = randint(1, 10)
        self.__name = "Прямоугольник"

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    def get_perimeter(self):
        """Возвращает периметр фигуры"""
        return (self.a + self.b) * 2

    def get_area(self):
        """Возвращает площадь фигуры"""
        return self.a * self.b

    def get_description(self):
        """Возвращает произвольное описание фигуры"""
        return f"Я - {self.__name}, параметры: a = {self.a}, b = {self.b}"


class Square(IShape):
    def __init__(self):
        self.__a = randint(1, 10)
        self.__name = "Квадрат"

    @property
    def a(self):
        return self.__a

    def get_perimeter(self):
        """Возвращает периметр фигуры"""
        return self.a * 4

    def get_area(self):
        """Возвращает площадь фигуры"""
        return self.a * self.a

    def get_description(self):
        """Возвращает произвольное описание фигуры"""
        return f"Я - {self.__name}, параметры: a = {self.a}"


class Game:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance

    def greetings(self):
        return "Привет! Мы геометрические фигуры и у нас есть 2 вопроса."

    def do_u_wanna_play(self):
        if input("Играем? y/n: ") == "y":
            return True
        else:
            return False

    def figure_choosing(self):
        return choice((Circle(), Rectangle(), Square()))

    def questions(self, figure):
        def area_question():
            if int(input("Укажите мою площадь: ")) == figure.get_area():
                return "Правильно!"
            else:
                return f"Ошибка! Правильный ответ: {figure.get_area()}"

        def perimeter_question():
            if int(input("Укажите мой периметр: ")) == figure.get_perimeter():
                return "Правильно!"
            else:
                return f"Ошибка! Правильный ответ: {figure.get_perimeter()}"

        print(figure.get_description())

        print(area_question())
        print(perimeter_question())

    def play(self):
        print(self.greetings())
        while True:
            if self.do_u_wanna_play():
                figure = self.figure_choosing()
                self.questions(figure)
            else:
                print("Спасибо за участие!")
                break


if __name__ == "__main__":
    Game().play()