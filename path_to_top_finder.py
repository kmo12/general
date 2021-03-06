
# Общее описание скрипта

from random import randint
import time

# Пример поля, по которому будем двигаться
# general_field = [
#     [2, 3, 3, 3, 2, 2, 2, 1, 2, 0],
#     [2, 3, 4, 4, 2, 2, 2, 2, 2, 0],
#     [2, 3, 4, 5, 2, 2, 2, 1, 1, 0],
#     [2, 3, 4, 4, 2, 2, 2, 1, 1, 0],
#     [2, 3, 3, 2, 2, 2, 1, 1, 1, 1],
#     [2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0, 0, 1, 1, 0, 0]
# ]


def field_generator(sum_y, sum_x, nums):
    if sum_y:
        return [[nums for _ in range(0, sum_x)] for _ in range(0, sum_y)]
    else:
        raise Exception("Field is empty! Y <= 0")


def is_destination_available(field, point_y, point_x):
    """
    Проверка точки по "координате" на доступность

    :param field:general лист (поле, на котором идёт ориентация)
    :param point_y: "координата" по вложенным листам первого уровня([]) внутри general листа
    :param point_x: "координата" по вложенным листам второго уровня ([][]) внутри general листа
    :return: None, если точка по координатам не найдена.
    Если точка меньше нуля: отдаёт None.
    Если найдена и она больше нуля: отдаёт координату.
    """
    if point_y >= 0 and point_x >= 0:
        try:
            field_point = field[point_y][point_x]
        except IndexError:
            return None
        else:
            if field_point >= 0:
                return field_point
            else:
                return None
    else:
        return None


class Navigation:
    """
    Класс получает поле (на котором идёт ориентация) и координаты Y и X.
    После инициализации может отдать "координаты" точек, которые находятся в радиусе 1 от "изначальной".

    :param field: general лист (поле, на котором идёт ориентация)
    :param point_y: "координата" по вложенным листам первого уровня([]) внутри general листа
    :param point_x: "координата" по вложенным листам второго уровня ([][]) внутри general листа
    Лист из всех направлений:
    center
    top_left
    top_top
    top_right
    right
    bottom_right
    bottom_bottom
    bottom_left
    left

    Navigation.nav_admin_print(1): Включение режима отладки
    """

    def __init__(self, field, point_y, point_x):
        self.field = field
        self.point_x = point_x
        self.point_y = point_y

        # Блок с атрибутами навигации
        self.center = (
            is_destination_available(field, point_y, point_x),
            point_y,
            point_x)
        self.top_left = (
            is_destination_available(field, point_y - 1, point_x - 1),
            point_y - 1,
            point_x - 1)
        self.top_top = (
            is_destination_available(field, point_y - 1, point_x),
            point_y - 1,
            point_x)
        self.top_right = (
            is_destination_available(field, point_y - 1, point_x + 1),
            point_y - 1,
            point_x + 1)
        self.right = (
            is_destination_available(field, point_y, point_x + 1),
            point_y,
            point_x + 1)
        self.bottom_right = (
            is_destination_available(field, point_y + 1, point_x + 1),
            point_y + 1,
            point_x + 1)
        self.bottom_bottom = (
            is_destination_available(field, point_y + 1, point_x),
            point_y + 1,
            point_x)
        self.bottom_left = (
            is_destination_available(field, point_y + 1, point_x - 1),
            point_y + 1,
            point_x - 1)
        self.left = (
            is_destination_available(field, point_y, point_x - 1),
            point_y,
            point_x - 1)

    def nav_admin_print(self, admin=0):
        if admin:
            print(f"\
                **************\n\
                {Navigation.center=}\n\
                {Navigation.top_left=}\n\
                {Navigation.top_top=}\n\
                {Navigation.top_right=}\n\
                {Navigation.right=}\n\
                {Navigation.bottom_right=}\n\
                {Navigation.bottom_bottom=}\n\
                {Navigation.bottom_left=}\n\
                {Navigation.left=}\n\
                **************")


def which_way(current_decision_param, list_of_directions_param, log=0):
    """
    Выбираем подходящую точку с координатами из списка с подобными точками по определённым условиям (об этом в :return:)

    :param current_decision_param: исходное положение на поле (list(значение по коорд., Y, X))
    :param list_of_directions_param: список значений от всех направлений вокруг (получается через Navigation)
    :param log: 1/0 - Выведение в print отчёта о шагах
    :return: положение на поле, точку, которая либо больше исходной, либо взята случайно из имеющихся вокруг
     (случайная точка не будет None, и будет не меньше исходной)
    """
    # Переменная для определения самой высокой из имеющихся вокруг
    highest_of_around = 0

    for i in list_of_directions_param:
        if isinstance(i[0], (int, float)):
            # Сюда дополнительными if можно прописывать функционал поведения выбора след. точки

            # Узнаём самую высокую точку из имеющихся вокруг
            if i[0] > highest_of_around:
                highest_of_around = i[0]

            if i[0] > current_decision_param[0]:
                current_decision_param = i

                if log:
                    print(f"Найдена точка больше: {current_decision_param}")

                return current_decision_param

    else:
        # Иногда робот мог посчитать, что нашёл самую высокую точку раньше времени.
        #  Ошибка была в методе определения такой точки (Последней точкой проверки являлась Navigation.left,
        #  по ней шло сравнение, если не найдена точка выше.
        #  Исправлено с помощью ..or current_decision_param[0] == highest_of_around
        if current_decision_param[0] == i[0] or current_decision_param[0] == highest_of_around:
            if log:
                print("Имеющаяся и все соседние точки оказались равны")

            while True:
                rand_item_from_list_of_directions_param = list_of_directions_param[randint(0, 7)]

                if not rand_item_from_list_of_directions_param[0] is None \
                        and rand_item_from_list_of_directions_param[0] >= current_decision_param[0] \
                        and rand_item_from_list_of_directions_param not in prev_positions:
                    current_decision_param = rand_item_from_list_of_directions_param

                    if log:
                        print(f"Берём случайную точку: {current_decision_param}\n------")

                    # Добавляем нынешнюю позицию в список "всех предыдущих"
                    # Эффект "короткой памяти" добавлен, чтобы не попадать в ловушки
                    if len(prev_positions) > 2:
                        del prev_positions[0]
                    prev_positions.append(current_decision_param)

                    # Выходим из функции, не дав провести добавление True для завершения общих поисков
                    return current_decision_param

        # Чтобы дать понять, что мы нашли самую высокую точку, добавляем четвёртый элемент в список
        #  и проверяем его наличие на выходе
        current_decision_param = list(current_decision_param)
        current_decision_param.append(True)

        if log:
            print(f"Все предыдущие точки:\n"
                  f"{prev_positions}")

        return current_decision_param


def highest_point_finder(general_field, start_point_y, start_point_x, log=0):
    # Счётчик шагов, затраченных на получение результата
    steps_counter = 0

    global prev_positions
    prev_positions = list()

    # Берём данные о стартовой точке и поле и начинаем поиск
    navigation = Navigation(general_field, start_point_y, start_point_x)

    current_decision = navigation.center

    list_of_directions = (navigation.top_left,
                          navigation.top_top,
                          navigation.top_right,
                          navigation.right,
                          navigation.bottom_right,
                          navigation.bottom_bottom,
                          navigation.bottom_left,
                          navigation.left)

    current_decision = which_way(current_decision, list_of_directions, log)

    while True:
        navigation = Navigation(general_field, current_decision[1], current_decision[2])

        list_of_directions = (navigation.top_left,
                              navigation.top_top,
                              navigation.top_right,
                              navigation.right,
                              navigation.bottom_right,
                              navigation.bottom_bottom,
                              navigation.bottom_left,
                              navigation.left)

        current_decision = which_way(current_decision, list_of_directions, log)
        steps_counter += 1

        # Чтобы понять, что мы нашли самую высокую точку, мы в which_way() добавляли четвёртый элемент в список
        #  и теперь проверяем его наличие на выходе
        if len(current_decision) == 4:
            del current_decision[-1]
            break

    if log:
        print(f"Готово! Самая высокая точка: {current_decision}\n"
              f""
              f"Результат получен за {steps_counter} шага")

    return current_decision, steps_counter


if __name__ == "__main__":
    # Задаём величину поля (пример, как будет выглядеть поле, есть в начале страницы path_to_top_finder.py)
    field_size_y = 10
    field_size_x = 10

    # Генерируем поле, заполняя его нулями
    general_field = field_generator(field_size_y, field_size_x, 0)

    # Выбираем самую высокую точку на поле
    general_field[8][8] = 1

    # Стартовые точки по осям (Можно сделать рандомными):
    # rand_point_y = randint(0, field_size_y - 1)
    # rand_point_x = randint(0, field_size_x - 1)
    start_point_y = 1
    start_point_x = 1

    # Возможность визуализации поля перед началом работы
    # for element in general_field:
    #     print(element)

    # print(f"Поле: {field_size_x} x {field_size_y}")
    # print(f"Случайная точка установлена на: x:{80}, y:{80}")

    # Берём таймаут для быстрого просмотра вводных данных
    # time.sleep(2)

    counter = 0
    max_num = 0
    min_num = 0
    num_of_trys = 10
    for _ in range(num_of_trys):
        work = highest_point_finder(general_field, start_point_y, start_point_x)[1]
        print(work)

        counter += work

        if work > max_num:
            max_num = work
        elif work < min_num or min_num == 0:
            min_num = work
    else:
        print(f"Среднее значение: {int(counter / num_of_trys)}\n"
              f"({max_num=})\n"
              f"{min_num=}")
