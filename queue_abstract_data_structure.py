from random import randint, choice


class Queue:
    #   push(item) - enqueue
    #   pop() - dequeue
    #   peek() - front
    #   is_empty()
    #   size()
    #   back()

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

    def __str__(self):
        return f"{self.__data}"


def name_picker(amount=5):
    real_names = ["Tom", "Bruce", "Ivan", "Jeremy", "John",
                  "Mark", "Steve", "Sven", "Lesly", "Gordon",
                  "Paul", "Peter", "Stevie", "Brian", "Stan",
                  "Frank", "Antony", "Matt", "Robert", "Woody"]
    return [real_names.pop(real_names.index(choice(real_names))) for x in range(1, amount + 1)]


def hot_potato(players_amount=5, end_num=3):
    players_list = name_picker(players_amount)
    players = Queue()

    for i in range(players_amount):
        players.enqueue(players_list[i])

    while players.size() > 1:
        for _ in range(end_num):
            first_guy = players.dequeue()
            next_guy = players.front()
            print(f"{first_guy} passed a potato to {next_guy}")
            players.enqueue(first_guy)
        print(f"{players.dequeue()} gone away")

    return f"-------------\n" \
           f"There was {len(players_list)} guys.\n" \
           f"Every {end_num} did gone away.\n\n" \
           f"Last guy is {players.front()},\n" \
           f"his position was {players_list.index(players.front()) + 1}"

    # return print(players)


print(hot_potato())
