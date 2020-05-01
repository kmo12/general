from random import randint
from timeit import Timer


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


def module(a):
    return a * -1 if a < 0 else a


class RadixSort:
    def __init__(self, list_for_sort: list):
        self.__main_list = list_for_sort
        self.__num_of_max_symbols = len(str(max(self.__main_list)))

        self.__q = [Queue() for _ in range(10)]

    def get_main_list(self):
        return self.__main_list

    def unsorted_list_ints_to_str(self):
        """
        Example: need 2 symbols each item.
        Def will make:
        [1, 2, 3] -> ['01', '02', '03']
        """
        self.__main_list = \
            list(map(lambda x: str(x).rjust(self.__num_of_max_symbols, "0"),
                     self.__main_list))

    def queue_checker(self):
        for i in range(10):
            print(f"q{i}: {self.__q[i]}")

    def in_queue_sorter(self, symbol_position):
        # Этот метод собирает от main_list данные и сортирует их по q0, q1 и пр.
        for num in self.__main_list:
            for i in range(10):
                if num[symbol_position] == f"{i}":
                    self.__q[i].enqueue(num)
                    break
        self.__main_list.clear()

    def out_queue_picker(self):
        # Этот метод собирает с q0, q1 и пр. данные и собирает их в self.__main_list
        for queue in self.__q:
            if not queue.is_empty():
                while queue.size() != 0:
                    self.__main_list.append(queue.dequeue())

    def sort(self):
        self.unsorted_list_ints_to_str()

        counter = -1
        while self.__num_of_max_symbols >= module(counter):
            self.in_queue_sorter(counter)
            self.out_queue_picker()
            counter -= 1

        # Возвращаем списку изначальный вид, все элементы переводим в int
        self.__main_list = list(map(int, self.__main_list))
        # print(self.get_main_list())


generator = list(randint(0, 999) for i in range(100000))

radix_sort = RadixSort(generator)

t1 = Timer("RadixSort(generator).sort()", "from __main__ import generator, RadixSort")
t2 = Timer("sorted(generator)", "from __main__ import generator")

print("My RadixSort: {0:.8f}".format(t1.timeit(number=1)))
print("Func 'sorted(): '{0:.8f}".format(t2.timeit(number=1)))