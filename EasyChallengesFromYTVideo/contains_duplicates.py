# Дан массив целых чисел
# Нужна функция, которая проверит:
# если есть дубли внутри: выдаст True
# если нет дублей: выдаст False

# Если
#       example_list = [1, 2, 3, 1]
# то
#       contains_duplicates(example_list) = True
#           True

# Если
#       example_list = [1, 2, 3]
# то
#       contains_duplicates(example_list) = False
#           False

# Если
#       example_list = []
# то
#       contains_duplicates(example_list) = False
#           False

example_list = [1, 2, 3, 1]


# def contains_duplicates(func_example_list):
#     func_example_list_list = list(func_example_list)
#     func_example_list_set = set(func_example_list)
#
#     if len(func_example_list_list) > len(func_example_list_set):
#         return True
#     else:
#         return False


# print(contains_duplicates(example_list))


def contains_duplicates(func_example_list):
    return len(list(func_example_list)) != len(set(func_example_list))


print(contains_duplicates(example_list))