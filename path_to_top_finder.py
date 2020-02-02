from random import randint

# Поле, по которому будем двигаться
general_field = [
    [2, 3, 3, 3, 2, 2, 2, 1, 2, 0],
    [2, 3, 4, 4, 2, 2, 2, 2, 2, 0],
    [2, 3, 4, 5, 2, 2, 2, 1, 1, 0],
    [2, 3, 4, 4, 2, 2, 2, 1, 1, 0],
    [2, 3, 3, 2, 2, 2, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 0]
]
# Стартовые точки по осям (Можно сделать рандомными)
start_point_y = 7
start_point_x = 9


def is_destination_available(field, point_y, point_x):
    """
    Проверка точки по "координате" на доступность
    :param field:
    :param point_y:
    :param point_x:
    :return: None, если точка по координатам не найдена.
    Если точка меньше нуля: отдаёт None.
    Если найдена и больше нуля: отдаёт координату.
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


# Проверка, нужно ли рассматривать точку для передвижения на неё
# if isinstance(nav_testing[2][0], (int, float)):
#     pass

class Navigation:
    """
    Навигация:
    Обращение к определённой позиции выдаст: (значение в точке; точка Y; точка X)

    :param field: general лист
    :param point_x: "координата" по вложенным листам второго уровня ([][]) внутри general листа
    :param point_y: "координата" по вложенным листам первого уровня([]) внутри general листа
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

    def which_way(self, current_decision_param, list_of_directions_param):
        for i in list_of_directions_param:
            if isinstance(i[0], (int, float)):
                # Сюда дополнительными if можно прописывать функционал поведения и выбора след. точки
                if i[0] > current_decision_param[0]:
                    current_decision_param = i
                    print(f"Найдена точка больше: {current_decision_param}")
                    return current_decision_param

        else:
            # TODO Иногда робот может посчитать, что нашёл самую высокую точку. Ошибка в методе определения такой точки
            #  (Последней точкой проверки является Navigation.left, по ней идёт сравнение, если не найдена точка выше.
            #  (Ошибка появилась из-за else в цикле for функции Navigation().which_way())
            if current_decision_param[0] == i[0]:
                print("Имеющаяся и все соседние точки оказались равны")

                while True:
                    rand_list_of_directions_param = list_of_directions_param[randint(0, 7)]
                    if not rand_list_of_directions_param[0] is None:  # \

                        # TODO Нужно починить. Идея такова: нужно сделать,
                        #  чтобы робот не уходил на ранд.точки, которые меньше изначальной
                        # and not current_decision_param[0] < rand_list_of_directions_param[0]:

                        current_decision_param = rand_list_of_directions_param
                        print(f"Берём случайную точку: {current_decision_param}\n------")
                        # Выходим из функции, не дав провести добавление True для завершения общих поисков
                        return current_decision_param

            # Чтобы дать понять, что мы нашли самую высокую точку, добавляем четвёртый элемент в список
            # и проверяем его наличие на выходе
            current_decision_param = list(current_decision_param)
            current_decision_param.append(True)
            return current_decision_param


# Берём начальные данные с верха страницы и начинаем поиск
# (Простой Navigation = Navigation() выглядел хорошо, но конфликтовал и давал сбой в дальнейшем вызове в while)
Navigation_var = Navigation(general_field, start_point_y, start_point_x)

current_decision = Navigation_var.center

list_of_directions = (Navigation_var.top_left,
                      Navigation_var.top_top,
                      Navigation_var.top_right,
                      Navigation_var.right,
                      Navigation_var.bottom_right,
                      Navigation_var.bottom_bottom,
                      Navigation_var.bottom_left,
                      Navigation_var.left)

current_decision = Navigation_var.which_way(current_decision, list_of_directions)

while True:
    Navigation_var = Navigation(general_field, current_decision[1], current_decision[2])

    list_of_directions = (Navigation_var.top_left,
                          Navigation_var.top_top,
                          Navigation_var.top_right,
                          Navigation_var.right,
                          Navigation_var.bottom_right,
                          Navigation_var.bottom_bottom,
                          Navigation_var.bottom_left,
                          Navigation_var.left)

    current_decision = Navigation_var.which_way(current_decision, list_of_directions)

    if len(current_decision) == 4:
        # del current_decision[-1]
        break

print(f"Готово! Самая высокая точка: {current_decision=}")
