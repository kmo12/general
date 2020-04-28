from random import randint, choice


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
    
    # Cheat for debugging
    def __str__(self):
        return f"{self.__data}"


def name_picker(amount=5) -> list:
    """
    Will return amount of random guy's names
    """
    real_names = ["Tom", "Bruce", "Ivan", "Jeremy", "John",
                  "Mark", "Steve", "Sven", "Lesly", "Gordon",
                  "Paul", "Peter", "Stevie", "Brian", "Stan",
                  "Frank", "Antony", "Matt", "Robert", "Woody"]
    return [real_names.pop(real_names.index(choice(real_names))) for x in range(amount)]


def hot_potato(players_amount=5, end_num=3):
    """
    Script will show you, what position you need to take to not leave the game
      with entered conditions.
    :param players_amount: int. How many players in game
    :param end_num: int. How many passes must be completed before guy
                            who ended with ball will leave
    :return: str. Info: Who was the last guy, which didn't leave,
                        and what was his number in queue at the beginning
                          of the game
    """
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


print(hot_potato())
