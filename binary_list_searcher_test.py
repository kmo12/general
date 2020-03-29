from timeit import Timer
from random import randint

testing_list = ([randint(0, 999999999) for i in range(100000 + 1)])  # Генерируем огромный список со случайными числами
testing_list[89976] = 596996399  # Чтобы результат поиска был гарантировано возможен


class SearchMethods:
    # тайминги указаны для [randint(0, 999999999) for i in range(100000 + 1)]
    # 0.01s / O(log n)
    @staticmethod
    def linear_search(list_for_sort: list, what_search: int) -> int:
        for index, num in enumerate(list_for_sort):
            if num == what_search:
                return index
        return -1

    # 0.05s / O(log n)
    @staticmethod
    def linear_sorted_search(list_for_sort: list, what_search: int) -> int:
        list_for_sort.sort()
        for index, num in enumerate(list_for_sort):
            if num == what_search:
                return index
            elif num > what_search:
                return -1
        return -1

    # 0.2s / O(log n)
    @staticmethod
    def binary_search(list_for_sort: list, what_search: int, log=False) -> int:
        # Сортируем список чисел, перед началом
        list_for_sort.sort()
        # Определяем наименьший и наибольший индекс в списке
        high_index = len(list_for_sort) - 1
        low_index = 0
        # Во время цикла делим количество индексов, с которыми работаем, пополам до тех пор, пока не получим искомый ключ
        while True:
            mid_index = (high_index + low_index) // 2
            if low_index == mid_index:
                if log:
                    print("-1")
                return -1  # a.k.a ключ не найден
            if what_search < list_for_sort[mid_index]:
                if log:
                    print(f"ключ меньше mid_index\n{low_index, mid_index, high_index}")
                high_index = mid_index
            elif what_search > list_for_sort[mid_index]:
                if log:
                    print(f"ключ больше mid_index\n{low_index, mid_index, high_index}")
                low_index = mid_index
            elif what_search == list_for_sort[mid_index]:
                if log:
                    print(mid_index)
                return mid_index

    
def search_method_time_check(search_method: str, list_with_nums: list, num_for_search: int, log=False) -> print:
    """
    Take SearchMethods.some_search_method(list, num, log) and return:
    Timer(f"SearchMethods.some_search_method({list}, {num}, {log})", "from __main__ import SearchMethods")
    """
    print("{0:.8f}".format(Timer(f"SearchMethods.{search_method}({list_with_nums}, {num_for_search}, {log})",
                                 "from __main__ import SearchMethods").timeit(number=1)))


if __name__ == "__main__":
    search_method_time_check("binary_search", testing_list, 596996399, False)



