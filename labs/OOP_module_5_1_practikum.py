# Дано:
#
# Д Зина Корзинкина
# М Вася Пупкин
# М Федя Сумкин
# М Вова Морковкин
# Д Катя Петрова
# М Петя Зайцев
# Д Маша Простоквашина
# М Дима Дрезина
# М Коля Лукошкин
# М Миша Косолапов
# Д Наташа Блинова
#
# Необходимо:
#
# создать и описать класс DanceFloor, которому в конструктор передаются данные из "Дано"
# в классе DanceFloor создать и описать метод dance, который должен напечатать информацию о получившихся парах
# и о тех танцорах, которые остались без пары (их количество и имя первого танцора в очереди)
#
# Учтите, что:
# мальчики танцуют только с девочками
# девочки танцуют только с мальчиками
#
# Как это должно работать
# cmd
# >>> process = DanceFloor("dancers.txt")
# >>> process.dance();
# Образовались следующие пары:
# Зина и Вася
# Катя и Федя
# Маша и Вова
# Наташа и Петя
# Мальчиков в очереди: 3 и первый из них — Дима


class Queue:
    def __init__(self):
        self.__data = list()

    def size(self):
        return len(self.__data)

    def front(self):
        if self.size() > 0:
            return self.__data[0]
        return None

    def back(self):
        if self.size() > 0:
            return self.__data[-1]
        return None

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.__data.pop(0)
        return None

    def is_empty(self):
        return len(self.__data) == 0

    def remove(self, item):
        self.__data.remove(item)

    def clear(self):
        self.__data = list()

    def __str__(self):
        return f"{self.__data}"


raw_data = "Д Лена Корзинкина\n" \
           "М Федя Сумкин\n" \
           "Д Кеша Петрова\n" \
           "М Паша Зайцев\n" \
           "М Кирюша Пупкин\n" \
           "М Стас Морковкин\n" \
           "Д Мира Простоквашина\n" \
           "М Кузя Дрезина\n" \
           "М Миша Косолапов\n" \
           "М Равик Лукошкин\n" \
           "Д Катюха Лукошкина\n" \
           "Д Любава Лукошкина\n" \
           "Д Люда Кошкина\n" \
           "Д Мирослава Лукошкина\n" \
           "Д Аня Блинова"


class DanceFloor:
    def __init__(self, dancers_data):
        self.__dancers_data = dancers_data
        self.__queue_guys = Queue()
        self.__queue_girls = Queue()

    def raw_dancers_data_distributor(self):
        s1 = self.__dancers_data.split("\n")
        s2 = list((stroke.split() for stroke in s1))

        for dancer in s2:
            for i in dancer:
                if i == "Д":
                    self.__queue_girls.enqueue(dancer[1])
                else:
                    self.__queue_guys.enqueue(dancer[1])
                break

    def dance(self):
        self.raw_dancers_data_distributor()

        pares = list()
        while not self.__queue_guys.is_empty() and not self.__queue_girls.is_empty():
            pares.append(f"{self.__queue_girls.dequeue()} и {self.__queue_guys.dequeue()}")

        if self.__queue_guys.is_empty() and self.__queue_girls.is_empty():
            lasts = ""
        else:
            male = "male" if self.__queue_guys.size() else ""
            lasts = f"{'Мальчиков' if male else 'Девочек'} в очереди: " \
                    f"{self.__queue_guys.size() or self.__queue_girls.size()}" \
                    f" и {'первый' if male else 'первая'} из них — " \
                    f"{self.__queue_guys.front() if male else self.__queue_girls.front()}"

        print("Образовались следующие пары:")
        for pare in pares:
            print(pare)
        print(lasts) if lasts else None


DanceFloor(raw_data).dance()


def timer_test_map_or_for():
    from timeit import Timer

    def func_map(data):
        r1 = data.split("\n")
        return list(map(lambda x: x.split(), r1))

    def func_for(data):
        r1 = data.split("\n")
        return list((stroke.split() for stroke in r1))

    t1 = Timer("func_map(raw_data)", "from __main__ import func_map, raw_data")
    t2 = Timer("func_for(raw_data)", "from __main__ import func_for, raw_data")

    print("Map: {0:.8f}".format(t1.timeit(number=1)))
    print("For loop: '{0:.8f}".format(t2.timeit(number=1)))
