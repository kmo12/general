from random import randint
import inspect

# Поле, по которому будем двигаться
general_field = [
    [3, 4, 3, 2, 1],
    [3, 3, 3, 2, 1],
    [2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1]
]
# Стартовые точки по осям
start_point_y = 3
start_point_x = 3


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
        self.__field = field
        self.__point_x = point_x
        self.__point_y = point_y

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

    # Блок защиты от записи атрибутов field, point_x, point_y для теста защиты от записи атрибутов
    def get_main_nav_data(self, num_get=0):
        if num_get == 1:
            return self.__field
        elif num_get == 2:
            return self.__point_x
        elif num_get == 3:
            return self.__point_y
    field = property(get_main_nav_data(1))
    point_x = property(get_main_nav_data(2))
    point_y = property(get_main_nav_data(3))


Navigation = Navigation(general_field, start_point_y, start_point_x)

list_of_directions = (Navigation.top_left,
                      Navigation.top_top,
                      Navigation.top_right,
                      Navigation.right,
                      Navigation.bottom_right,
                      Navigation.bottom_bottom,
                      Navigation.bottom_left,
                      Navigation.left)


print(Navigation.center)

Navigation.nav_admin_print(1)


def which_way():
    current_decision = Navigation.center
    prev_current_decision = current_decision

    while True:
        # prev_current_decision = current_decision
        for i in list_of_directions:
            if i[0] or i[0] == 0:
                if i[0] > current_decision[0]:
                    print(f"Старая позиция: {current_decision=}")
                    current_decision = i
                    print(f"Новая позиция: {current_decision=}")
        else:
            if prev_current_decision == current_decision:
                break

    print(current_decision)


which_way()